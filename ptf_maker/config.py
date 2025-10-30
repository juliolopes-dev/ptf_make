"""Configurações do projeto"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Paths
PROJECT_ROOT = Path(__file__).parent.parent
ASSETS_DIR = PROJECT_ROOT / "assets"
OUT_DIR = PROJECT_ROOT / "out"

# API Keys
def get_pexels_key():
    """Obtém chave Pexels do .env ou Streamlit secrets"""
    # Tentar .env primeiro (local)
    key = os.getenv("PEXELS_KEY", "")
    
    # Se não encontrar, tentar Streamlit secrets (cloud)
    if not key:
        try:
            import streamlit as st
            key = st.secrets.get("PEXELS_KEY", "")
        except:
            pass
    
    return key

PEXELS_KEY = get_pexels_key()

# Defaults de vídeo
DEFAULT_VOICE = "pt-BR-AntonioNeural"
DEFAULT_TITLE = "Por Trás da Fortuna"
DEFAULT_PRIMARY_COLOR = "#FFD700"
DEFAULT_FONT = "Arial"
DEFAULT_FONT_SIZE = 58

# Configurações de vídeo
VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
VIDEO_FPS = 30

# Pexels API
PEXELS_API_URL = "https://api.pexels.com/v1/search"
