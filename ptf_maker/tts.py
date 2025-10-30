"""Geração de áudio via edge-tts"""
import asyncio
import logging
from pathlib import Path
import edge_tts

logger = logging.getLogger(__name__)


def make_tts(text: str, out_mp3: str, voice: str = "pt-BR-AntonioNeural") -> None:
    """
    Gera áudio TTS usando edge-tts (síncronamente).
    
    Args:
        text: Texto para converter em fala
        out_mp3: Caminho do arquivo de saída MP3
        voice: Voz do TTS
    """
    logger.info(f"Gerando TTS com voz {voice}...")
    
    async def _generate():
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(out_mp3)
    
    try:
        asyncio.run(_generate())
        logger.info(f"Áudio salvo em {out_mp3}")
    except Exception as e:
        logger.error(f"Erro ao gerar TTS: {e}")
        raise
