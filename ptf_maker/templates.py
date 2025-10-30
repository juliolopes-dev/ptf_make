"""Templates profissionais pré-configurados"""
from typing import Dict, Any


TEMPLATES = {
    "finance": {
        "title": "💰 Dinheiro & Riqueza",
        "primary_color": "#FFD700",  # Dourado
        "secondary_color": "#2ECC71",  # Verde
        "font": "Arial",
        "font_size": 62,
        "topic": "finance money wealth investment",
        "music_volume": 0.15,
        "effects": {
            "ken_burns": True,
            "transitions": True,
            "text_animation": "fade"
        }
    },
    
    "motivation": {
        "title": "🔥 Motivação Diária",
        "primary_color": "#E74C3C",  # Vermelho vibrante
        "secondary_color": "#F39C12",  # Laranja
        "font": "Arial",
        "font_size": 65,
        "topic": "motivation success achievement inspiration",
        "music_volume": 0.20,
        "effects": {
            "ken_burns": True,
            "transitions": True,
            "text_animation": "zoom"
        }
    },
    
    "tech": {
        "title": "⚡ Tech & Inovação",
        "primary_color": "#3498DB",  # Azul tech
        "secondary_color": "#9B59B6",  # Roxo
        "font": "Arial",
        "font_size": 58,
        "topic": "technology innovation digital future",
        "music_volume": 0.12,
        "effects": {
            "ken_burns": True,
            "transitions": True,
            "text_animation": "slide"
        }
    },
    
    "business": {
        "title": "📊 Negócios & Estratégia",
        "primary_color": "#34495E",  # Cinza escuro
        "secondary_color": "#16A085",  # Verde água
        "font": "Arial",
        "font_size": 60,
        "topic": "business entrepreneur office professional",
        "music_volume": 0.10,
        "effects": {
            "ken_burns": True,
            "transitions": True,
            "text_animation": "fade"
        }
    },
    
    "lifestyle": {
        "title": "✨ Lifestyle & Bem-Estar",
        "primary_color": "#FF6B9D",  # Rosa
        "secondary_color": "#C44569",  # Rosa escuro
        "font": "Arial",
        "font_size": 58,
        "topic": "lifestyle wellness health happiness",
        "music_volume": 0.18,
        "effects": {
            "ken_burns": True,
            "transitions": True,
            "text_animation": "fade"
        }
    },
    
    "education": {
        "title": "📚 Educação & Conhecimento",
        "primary_color": "#2980B9",  # Azul educação
        "secondary_color": "#8E44AD",  # Roxo
        "font": "Arial",
        "font_size": 60,
        "topic": "education learning knowledge study",
        "music_volume": 0.08,
        "effects": {
            "ken_burns": False,
            "transitions": True,
            "text_animation": "fade"
        }
    }
}


def get_template(template_name: str) -> Dict[str, Any]:
    """
    Retorna configurações de um template.
    
    Args:
        template_name: Nome do template
    
    Returns:
        Dicionário com configurações
    """
    template_name = template_name.lower()
    
    if template_name not in TEMPLATES:
        raise ValueError(
            f"Template '{template_name}' não encontrado. "
            f"Disponíveis: {', '.join(TEMPLATES.keys())}"
        )
    
    return TEMPLATES[template_name].copy()


def list_templates() -> list:
    """Retorna lista de templates disponíveis"""
    return list(TEMPLATES.keys())


def merge_template_with_args(template: Dict[str, Any], user_args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Mescla configurações do template com argumentos do usuário.
    Argumentos do usuário têm prioridade.
    
    Args:
        template: Configurações do template
        user_args: Argumentos fornecidos pelo usuário
    
    Returns:
        Configurações mescladas
    """
    config = template.copy()
    
    # Usuário pode sobrescrever qualquer configuração
    for key, value in user_args.items():
        if value is not None:
            config[key] = value
    
    return config
