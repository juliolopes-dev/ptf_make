"""Mixagem de áudio: TTS + música de fundo"""
import logging
from pathlib import Path
from pydub import AudioSegment
from pydub.effects import normalize

logger = logging.getLogger(__name__)


def mix_audio_with_music(
    voice_path: str,
    music_path: str,
    output_path: str,
    music_volume: float = 0.15
) -> str:
    """
    Mixa áudio de voz com música de fundo.
    
    Args:
        voice_path: Caminho do áudio TTS
        music_path: Caminho da música de fundo
        output_path: Caminho do áudio final
        music_volume: Volume da música (0.0 a 1.0)
    
    Returns:
        Caminho do áudio mixado
    """
    logger.info(f"Mixando áudio com música (volume: {music_volume*100}%)...")
    
    # Carregar áudios
    voice = AudioSegment.from_mp3(voice_path)
    music = AudioSegment.from_mp3(music_path)
    
    # Normalizar voz para -14 LUFS (padrão redes sociais)
    voice = normalize(voice)
    
    # Ajustar música para duração da voz
    if len(music) < len(voice):
        # Repetir música se for menor
        loops_needed = (len(voice) // len(music)) + 1
        music = music * loops_needed
    
    # Cortar música para duração exata
    music = music[:len(voice)]
    
    # Reduzir volume da música
    music = music - (20 * (1 - music_volume))  # Conversão para dB
    
    # Fade in/out na música
    music = music.fade_in(1000).fade_out(2000)
    
    # Mixar
    mixed = voice.overlay(music)
    
    # Normalizar resultado final
    mixed = normalize(mixed)
    
    # Exportar
    mixed.export(output_path, format="mp3", bitrate="192k")
    logger.info(f"Áudio mixado salvo em {output_path}")
    
    return output_path


def normalize_audio(audio_path: str, output_path: str = None) -> str:
    """
    Normaliza áudio para padrão de redes sociais.
    
    Args:
        audio_path: Caminho do áudio original
        output_path: Caminho de saída (opcional)
    
    Returns:
        Caminho do áudio normalizado
    """
    if not output_path:
        output_path = audio_path
    
    logger.info("Normalizando áudio...")
    audio = AudioSegment.from_mp3(audio_path)
    normalized = normalize(audio)
    normalized.export(output_path, format="mp3", bitrate="192k")
    
    return output_path
