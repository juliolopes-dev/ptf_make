"""Interface de linha de comando"""
import argparse
import logging
import sys
from pathlib import Path

from . import config
from .tts import make_tts
from .media import ensure_images
from .render import render_video
from .templates import get_template, list_templates, merge_template_with_args

# Audio mixer é opcional (requer pydub com audioop)
try:
    from .audio_mixer import mix_audio_with_music, normalize_audio
    AUDIO_MIXER_AVAILABLE = True
except ImportError:
    AUDIO_MIXER_AVAILABLE = False
    logger = logging.getLogger(__name__)
    logger.warning("Audio mixer não disponível (pydub requer Python < 3.13)")

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)


def main():
    """Ponto de entrada principal do CLI"""
    parser = argparse.ArgumentParser(
        description="ptf_maker - Gerador de vídeos verticais para TikTok"
    )
    
    # Entrada de texto
    script_group = parser.add_mutually_exclusive_group(required=True)
    script_group.add_argument(
        "--script",
        type=str,
        help="Texto do roteiro direto"
    )
    script_group.add_argument(
        "--script-file",
        type=str,
        help="Arquivo com o texto do roteiro"
    )
    
    # Configurações de mídia
    parser.add_argument(
        "--topic",
        type=str,
        default="finance money savings",
        help="Termo de busca para imagens (default: 'finance money savings')"
    )
    parser.add_argument(
        "--images",
        type=int,
        default=4,
        help="Quantidade de imagens (default: 4)"
    )
    parser.add_argument(
        "--no-download",
        action="store_true",
        help="Força uso apenas de imagens locais"
    )
    
    # Configurações de áudio
    parser.add_argument(
        "--voice",
        type=str,
        default=config.DEFAULT_VOICE,
        help=f"Voz do TTS (default: {config.DEFAULT_VOICE})"
    )
    
    # Configurações de branding
    parser.add_argument(
        "--title",
        type=str,
        default=config.DEFAULT_TITLE,
        help=f"Título do vídeo (default: '{config.DEFAULT_TITLE}')"
    )
    parser.add_argument(
        "--primary",
        type=str,
        default=config.DEFAULT_PRIMARY_COLOR,
        help=f"Cor primária em hex (default: {config.DEFAULT_PRIMARY_COLOR})"
    )
    parser.add_argument(
        "--font",
        type=str,
        default=config.DEFAULT_FONT,
        help=f"Fonte para textos (default: {config.DEFAULT_FONT})"
    )
    parser.add_argument(
        "--fontsize",
        type=int,
        default=config.DEFAULT_FONT_SIZE,
        help=f"Tamanho da fonte (default: {config.DEFAULT_FONT_SIZE})"
    )
    
    # Templates profissionais
    parser.add_argument(
        "--template",
        type=str,
        choices=list_templates(),
        help=f"Template profissional: {', '.join(list_templates())}"
    )
    
    # Música de fundo
    parser.add_argument(
        "--background-music",
        type=str,
        help="Caminho para música de fundo (MP3)"
    )
    parser.add_argument(
        "--music-volume",
        type=float,
        default=0.15,
        help="Volume da música de fundo (0.0 a 1.0, default: 0.15)"
    )
    
    # Efeitos visuais
    parser.add_argument(
        "--no-effects",
        action="store_true",
        help="Desabilitar efeitos visuais (zoom, transições)"
    )
    parser.add_argument(
        "--animation",
        type=str,
        choices=["fade", "zoom", "slide"],
        default="fade",
        help="Tipo de animação nas legendas (default: fade)"
    )
    
    args = parser.parse_args()
    
    try:
        # Aplicar template se especificado
        if args.template:
            logger.info(f"🎬 Usando template: {args.template}")
            template_config = get_template(args.template)
            
            # Mesclar com argumentos do usuário
            user_args = {
                "title": args.title if args.title != config.DEFAULT_TITLE else None,
                "primary_color": args.primary if args.primary != config.DEFAULT_PRIMARY_COLOR else None,
                "font": args.font if args.font != config.DEFAULT_FONT else None,
                "font_size": args.fontsize if args.fontsize != config.DEFAULT_FONT_SIZE else None,
                "topic": args.topic if args.topic != "finance money savings" else None,
                "music_volume": args.music_volume if args.music_volume != 0.15 else None,
            }
            
            final_config = merge_template_with_args(template_config, user_args)
            
            # Aplicar configurações do template
            args.title = final_config.get("title", args.title)
            args.primary = final_config.get("primary_color", args.primary)
            args.font = final_config.get("font", args.font)
            args.fontsize = final_config.get("font_size", args.fontsize)
            args.topic = final_config.get("topic", args.topic)
            args.music_volume = final_config.get("music_volume", args.music_volume)
            effects_config = final_config.get("effects", {})
        else:
            effects_config = {
                "ken_burns": not args.no_effects,
                "transitions": not args.no_effects,
                "text_animation": args.animation
            }
        
        # 1. Obter texto do roteiro
        if args.script:
            script_text = args.script
        else:
            script_file = Path(args.script_file)
            if not script_file.exists():
                logger.error(f"Arquivo não encontrado: {args.script_file}")
                sys.exit(1)
            script_text = script_file.read_text(encoding="utf-8")
        
        logger.info(f"Roteiro: {len(script_text)} caracteres")
        
        # 2. Criar diretórios
        config.OUT_DIR.mkdir(exist_ok=True)
        config.ASSETS_DIR.mkdir(exist_ok=True)
        
        # 3. Gerar áudio TTS
        audio_path = config.OUT_DIR / "audio.mp3"
        make_tts(script_text, str(audio_path), args.voice)
        
        # 3.5. Mixar com música de fundo se fornecida
        if args.background_music:
            if not AUDIO_MIXER_AVAILABLE:
                logger.warning("⚠️ Mixagem de áudio não disponível. Use Python 3.10-3.12 para este recurso.")
                logger.info("Continuando sem música de fundo...")
            else:
                music_file = Path(args.background_music)
                if music_file.exists():
                    logger.info("🎵 Mixando com música de fundo...")
                    mixed_audio_path = config.OUT_DIR / "audio_mixed.mp3"
                    mix_audio_with_music(
                        str(audio_path),
                        str(music_file),
                        str(mixed_audio_path),
                        args.music_volume
                    )
                    audio_path = mixed_audio_path
                else:
                    logger.warning(f"Música não encontrada: {args.background_music}")
        elif AUDIO_MIXER_AVAILABLE:
            # Normalizar áudio mesmo sem música
            normalize_audio(str(audio_path))
        
        # 4. Obter imagens
        try:
            image_paths = ensure_images(
                n=args.images,
                topic=args.topic,
                key=config.PEXELS_KEY,
                force_local=args.no_download
            )
        except FileNotFoundError as e:
            logger.error(str(e))
            sys.exit(1)
        
        # 5. Renderizar vídeo com efeitos profissionais
        video_path = config.OUT_DIR / "video.mp4"
        logger.info("🎥 Aplicando efeitos profissionais...")
        render_video(
            bg_paths=image_paths,
            audio_mp3=str(audio_path),
            script_text=script_text,
            out_path=str(video_path),
            title=args.title,
            primary_color=args.primary,
            font=args.font,
            font_size=args.fontsize,
            effects_config=effects_config
        )
        
        logger.info(f"\n✓ Vídeo gerado: {video_path}")
        logger.info(f"✓ Áudio: {audio_path}")
        
    except KeyboardInterrupt:
        logger.info("\nOperação cancelada pelo usuário")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Erro fatal: {e}", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
