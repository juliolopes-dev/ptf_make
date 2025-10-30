"""Download e gerenciamento de mídia (Pexels)"""
import logging
import requests
from pathlib import Path
from typing import List
import time

from .config import PEXELS_API_URL, ASSETS_DIR

logger = logging.getLogger(__name__)


def pexels_download(topic: str, n: int, key: str) -> List[str]:
    """
    Baixa imagens retrato do Pexels.
    
    Args:
        topic: Termo de busca
        n: Número de imagens a baixar
        key: Chave API do Pexels
        
    Returns:
        Lista de caminhos das imagens baixadas
    """
    if not key:
        logger.warning("Chave Pexels não fornecida, pulando download")
        return []
    
    ASSETS_DIR.mkdir(exist_ok=True)
    
    headers = {"Authorization": key}
    params = {
        "query": topic,
        "per_page": n,
        "orientation": "portrait"
    }
    
    try:
        logger.info(f"Buscando imagens no Pexels: '{topic}'...")
        response = requests.get(PEXELS_API_URL, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        photos = data.get("photos", [])
        if not photos:
            logger.warning(f"Nenhuma imagem encontrada para '{topic}'")
            return []
        
        downloaded = []
        for idx, photo in enumerate(photos[:n]):
            img_url = photo["src"]["large2x"]
            img_path = ASSETS_DIR / f"pexels_{int(time.time())}_{idx}.jpg"
            
            logger.info(f"Baixando imagem {idx+1}/{n}...")
            img_response = requests.get(img_url, timeout=15)
            img_response.raise_for_status()
            
            with open(img_path, "wb") as f:
                f.write(img_response.content)
            
            downloaded.append(str(img_path))
        
        logger.info(f"{len(downloaded)} imagens baixadas com sucesso")
        return downloaded
        
    except requests.RequestException as e:
        logger.error(f"Erro ao baixar do Pexels: {e}")
        return []


def ensure_images(n: int, topic: str = "", key: str = "", force_local: bool = False) -> List[str]:
    """
    Garante que temos imagens disponíveis, com fallback para assets locais.
    
    Args:
        n: Número de imagens necessárias
        topic: Termo de busca para Pexels
        key: Chave API do Pexels
        force_local: Forçar uso de imagens locais
        
    Returns:
        Lista de caminhos de imagens
    """
    images = []
    
    # Tentar download do Pexels se não forçar local
    if not force_local and key:
        images = pexels_download(topic, n, key)
    
    # Fallback para imagens locais
    if not images:
        logger.info("Buscando imagens locais em assets/...")
        ASSETS_DIR.mkdir(exist_ok=True)
        
        local_images = list(ASSETS_DIR.glob("*.jpg")) + list(ASSETS_DIR.glob("*.png"))
        
        if not local_images:
            raise FileNotFoundError(
                f"Nenhuma imagem disponível. Baixe do Pexels ou adicione imagens em {ASSETS_DIR}"
            )
        
        images = [str(img) for img in local_images[:n]]
        logger.info(f"Usando {len(images)} imagens locais")
    
    # Se temos menos imagens que necessário, repetir
    while len(images) < n:
        images.extend(images[:n - len(images)])
    
    return images[:n]
