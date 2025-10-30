"""Renderização do vídeo final com efeitos profissionais"""
import logging
from pathlib import Path
from typing import List, Dict, Any
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import (
    ImageClip, AudioFileClip, CompositeVideoClip, 
    concatenate_videoclips
)

from .config import VIDEO_WIDTH, VIDEO_HEIGHT, VIDEO_FPS
from .captions import split_lines
from .effects import ken_burns_effect, add_smooth_transition, create_animated_text_clip

# Monkey patch para compatibilidade com Pillow 10+
if not hasattr(Image, 'ANTIALIAS'):
    Image.ANTIALIAS = Image.Resampling.LANCZOS

logger = logging.getLogger(__name__)


def create_text_image(text: str, width: int, height: int, font_size: int, 
                     color: str, font_name: str = "Arial", 
                     stroke_color: str = "black", stroke_width: int = 2) -> np.ndarray:
    """Cria uma imagem com texto usando PIL"""
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype(f"{font_name}.ttf", font_size)
    except:
        try:
            font = ImageFont.truetype(f"C:\\Windows\\Fonts\\{font_name}.ttf", font_size)
        except:
            font = ImageFont.load_default()
    
    # Calcular posição centralizada
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Desenhar stroke
    if stroke_width > 0:
        for adj_x in range(-stroke_width, stroke_width + 1):
            for adj_y in range(-stroke_width, stroke_width + 1):
                draw.text((x + adj_x, y + adj_y), text, font=font, fill=stroke_color)
    
    # Desenhar texto principal
    draw.text((x, y), text, font=font, fill=color)
    
    return np.array(img)


def render_video(
    bg_paths: List[str],
    audio_mp3: str,
    script_text: str,
    out_path: str,
    title: str = "Por Trás da Fortuna",
    primary_color: str = "#FFD700",
    font: str = "Arial",
    font_size: int = 58,
    effects_config: Dict[str, Any] = None
) -> None:
    """
    Renderiza vídeo final com imagens, áudio, legendas e efeitos profissionais.
    
    Args:
        bg_paths: Lista de caminhos das imagens de fundo
        audio_mp3: Caminho do arquivo de áudio
        script_text: Texto do roteiro para legendas
        out_path: Caminho do vídeo de saída
        title: Título do vídeo (aparece nos primeiros 2s)
        primary_color: Cor primária em hex
        font: Nome da fonte
        font_size: Tamanho da fonte
        effects_config: Configuração de efeitos visuais
    """
    # Configuração padrão de efeitos
    if effects_config is None:
        effects_config = {
            "ken_burns": True,
            "transitions": True,
            "text_animation": "fade"
        }
    logger.info("Iniciando renderização do vídeo...")
    
    # Carregar áudio
    audio = AudioFileClip(audio_mp3)
    duration = audio.duration
    
    # Calcular duração por imagem
    clip_duration = duration / len(bg_paths)
    
    # Criar clipes de imagem com efeitos
    video_clips = []
    for img_path in bg_paths:
        img_clip = (ImageClip(img_path)
                   .set_duration(clip_duration)
                   .resize(height=VIDEO_HEIGHT))
        
        # Recortar para centralizar 1080×1920
        w, h = img_clip.size
        x_center = w / 2
        img_clip = img_clip.crop(
            x_center=x_center,
            width=VIDEO_WIDTH,
            height=VIDEO_HEIGHT
        )
        
        # Aplicar efeito Ken Burns (zoom gradual)
        if effects_config.get("ken_burns", True):
            img_clip = ken_burns_effect(img_clip, zoom_ratio=1.15)
        
        # Adicionar transições suaves
        if effects_config.get("transitions", True):
            img_clip = add_smooth_transition(img_clip, transition_duration=0.4)
        
        video_clips.append(img_clip)
    
    # Concatenar clipes
    base_video = concatenate_videoclips(video_clips, method="compose")
    base_video = base_video.set_audio(audio)
    
    # Criar título (primeiros 2s) com animação
    title_img = create_text_image(
        title, 
        VIDEO_WIDTH - 100, 
        150, 
        font_size + 12, 
        primary_color, 
        font, 
        "black", 
        3
    )
    
    # Aplicar animação ao título
    animation = effects_config.get("text_animation", "fade")
    title_clip = create_animated_text_clip(
        title_img,
        duration=min(2.5, duration),
        animation=animation,
        start_time=0
    )
    title_clip = title_clip.set_position(("center", 80))
    
    # Criar legendas animadas
    caption_lines = split_lines(script_text, max_chars=38)
    caption_duration = duration / len(caption_lines)
    
    caption_clips = []
    animation = effects_config.get("text_animation", "fade")
    
    for idx, line in enumerate(caption_lines):
        # Destacar palavras-chave (primeira palavra em cor diferente)
        caption_img = create_text_image(
            line,
            VIDEO_WIDTH - 80,
            140,
            font_size + 2,
            "white",
            font,
            "black",
            3
        )
        
        # Criar clipe com animação
        caption = create_animated_text_clip(
            caption_img,
            duration=caption_duration,
            animation=animation,
            start_time=idx * caption_duration
        )
        caption = caption.set_position(("center", VIDEO_HEIGHT - 220))
        
        caption_clips.append(caption)
    
    # Compor vídeo final
    final_video = CompositeVideoClip(
        [base_video, title_clip] + caption_clips,
        size=(VIDEO_WIDTH, VIDEO_HEIGHT)
    )
    
    # Exportar
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    
    logger.info(f"Exportando vídeo para {out_path}...")
    final_video.write_videofile(
        out_path,
        fps=VIDEO_FPS,
        codec="libx264",
        audio_codec="aac",
        temp_audiofile="temp-audio.m4a",
        remove_temp=True,
        logger=None
    )
    
    logger.info("Vídeo renderizado com sucesso!")
    
    # Liberar recursos
    audio.close()
    base_video.close()
    final_video.close()
