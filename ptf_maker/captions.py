"""Geração de legendas"""
from typing import List


def split_lines(text: str, max_chars: int = 38) -> List[str]:
    """
    Divide texto em linhas curtas para legendas.
    
    Args:
        text: Texto completo do roteiro
        max_chars: Máximo de caracteres por linha
        
    Returns:
        Lista de linhas de legenda
    """
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        word_length = len(word) + (1 if current_line else 0)
        
        if current_length + word_length > max_chars and current_line:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += word_length
    
    if current_line:
        lines.append(" ".join(current_line))
    
    return lines
