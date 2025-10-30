"""Efeitos visuais: animações, transições e movimento"""
import numpy as np
from moviepy.editor import ImageClip
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout


def ken_burns_effect(clip: ImageClip, zoom_ratio: float = 1.2) -> ImageClip:
    """
    Aplica efeito Ken Burns (zoom gradual) em um clipe.
    
    Args:
        clip: Clipe de imagem
        zoom_ratio: Fator de zoom (1.2 = 120% do tamanho original)
    
    Returns:
        Clipe com efeito de zoom
    """
    def zoom(t):
        # Zoom gradual ao longo do tempo
        zoom_factor = 1 + (zoom_ratio - 1) * (t / clip.duration)
        return zoom_factor
    
    return clip.resize(zoom)


def add_smooth_transition(clip: ImageClip, transition_duration: float = 0.5) -> ImageClip:
    """
    Adiciona transições fade in/out suaves.
    
    Args:
        clip: Clipe de imagem
        transition_duration: Duração da transição em segundos
    
    Returns:
        Clipe com transições
    """
    clip = fadein(clip, transition_duration)
    clip = fadeout(clip, transition_duration)
    return clip


def create_animated_text_clip(
    text_img: np.ndarray,
    duration: float,
    animation: str = "fade",
    start_time: float = 0
) -> ImageClip:
    """
    Cria clipe de texto com animação.
    
    Args:
        text_img: Array numpy da imagem de texto
        duration: Duração do clipe
        animation: Tipo de animação ('fade', 'slide', 'zoom')
        start_time: Tempo de início
    
    Returns:
        Clipe de imagem animado
    """
    clip = ImageClip(text_img).set_duration(duration).set_start(start_time)
    
    if animation == "fade":
        # Fade in rápido, fade out no final
        fade_duration = min(0.3, duration / 4)
        clip = fadein(clip, fade_duration)
        if duration > fade_duration * 2:
            clip = fadeout(clip, fade_duration)
    
    elif animation == "zoom":
        # Zoom de entrada
        def zoom_in(t):
            progress = min(t / 0.5, 1)  # Zoom nos primeiros 0.5s
            return 0.5 + 0.5 * progress
        clip = clip.resize(zoom_in)
    
    elif animation == "slide":
        # Slide de baixo para cima
        def slide_up(t):
            if t < 0.3:
                offset = 100 * (1 - t / 0.3)
                return ('center', lambda: 1920 - 200 + offset)
            return ('center', 1720)
        clip = clip.set_position(slide_up)
    
    return clip


def add_highlight_effect(text_img: np.ndarray, highlight_color: tuple = (255, 215, 0)) -> np.ndarray:
    """
    Adiciona efeito de destaque (brilho) em texto.
    
    Args:
        text_img: Imagem do texto
        highlight_color: Cor RGB do destaque
    
    Returns:
        Imagem com efeito de destaque
    """
    # Criar overlay com alpha channel
    overlay = np.copy(text_img)
    
    # Aumentar brilho nas áreas não transparentes
    alpha_mask = overlay[:, :, 3] > 0
    if alpha_mask.any():
        overlay[alpha_mask, :3] = np.clip(
            overlay[alpha_mask, :3] * 1.2,  # 20% mais brilho
            0, 255
        ).astype(np.uint8)
    
    return overlay
