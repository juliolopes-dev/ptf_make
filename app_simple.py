"""
Interface Web Streamlit para ptf_maker - VERSÃO SIMPLIFICADA
"""
import streamlit as st
import os
from pathlib import Path

# Configuração da página
st.set_page_config(
    page_title="ptf_maker - Gerador de Vídeos",
    page_icon="🎬",
    layout="wide"
)

# Teste se imports funcionam
try:
    from ptf_maker import config
    from ptf_maker.tts import make_tts
    from ptf_maker.media import ensure_images
    from ptf_maker.render import render_video
    from ptf_maker.templates import get_template, list_templates
    IMPORTS_OK = True
except Exception as e:
    IMPORTS_OK = False
    ERROR_MSG = str(e)

# Header
st.title("🎬 ptf_maker - Gerador de Vídeos Profissionais")

if not IMPORTS_OK:
    st.error(f"❌ Erro ao importar módulos: {ERROR_MSG}")
    st.info("Entre em contato com suporte")
    st.stop()

st.success("✅ Sistema inicializado com sucesso!")

# Sidebar - Templates
st.sidebar.title("🎨 Templates")
template_names = list_templates()
selected_template = st.sidebar.selectbox("Escolha um template:", template_names)

# Main content
st.header("📝 Criar Vídeo")

# Input de roteiro
script_text = st.text_area(
    "Digite seu roteiro:",
    height=200,
    placeholder="Seu texto aqui..."
)

# Número de imagens
num_images = st.slider("Número de imagens", 3, 8, 5)

# Botão de gerar
if st.button("🚀 GERAR VÍDEO", type="primary"):
    if not script_text:
        st.warning("Digite um roteiro primeiro!")
    else:
        try:
            # Preparar diretórios
            config.OUT_DIR.mkdir(exist_ok=True)
            config.ASSETS_DIR.mkdir(exist_ok=True)
            
            progress = st.progress(0)
            status = st.empty()
            
            # 1. TTS
            status.text("🎤 Gerando áudio...")
            progress.progress(25)
            
            template_data = get_template(selected_template)
            audio_path = config.OUT_DIR / "audio.mp3"
            make_tts(script_text, str(audio_path), template_data.get('voice', 'pt-BR-AntonioNeural'))
            
            # 2. Imagens
            status.text("🖼️ Baixando imagens...")
            progress.progress(50)
            
            image_paths = ensure_images(
                n=num_images,
                topic=template_data['topic'],
                key=config.PEXELS_KEY,
                force_local=not config.PEXELS_KEY
            )
            
            # 3. Render
            status.text("🎥 Renderizando vídeo...")
            progress.progress(75)
            
            video_path = config.OUT_DIR / "video.mp4"
            
            effects_config = template_data.get('effects', {
                "ken_burns": True,
                "transitions": True,
                "text_animation": "fade"
            })
            
            render_video(
                bg_paths=image_paths,
                audio_mp3=str(audio_path),
                script_text=script_text,
                out_path=str(video_path),
                title=template_data.get('title', 'Vídeo'),
                primary_color=template_data.get('primary_color', '#FFD700'),
                font=template_data.get('font', 'Arial'),
                font_size=template_data.get('font_size', 58),
                effects_config=effects_config
            )
            
            progress.progress(100)
            status.text("✅ Vídeo gerado!")
            
            # Mostrar resultado
            st.success("🎉 Vídeo pronto!")
            st.video(str(video_path))
            
            # Download
            with open(video_path, 'rb') as f:
                st.download_button(
                    "⬇️ BAIXAR VÍDEO",
                    f,
                    file_name="video.mp4",
                    mime="video/mp4"
                )
                
        except Exception as e:
            st.error(f"❌ Erro: {str(e)}")
            st.exception(e)

# Footer
st.markdown("---")
st.markdown("Versão simplificada para debug")
