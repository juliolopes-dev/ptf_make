"""
Interface Web Streamlit para ptf_maker
Gerador Profissional de Vídeos para TikTok/Reels
"""
import streamlit as st
import os
from pathlib import Path
import time
from ptf_maker import config
from ptf_maker.tts import make_tts
from ptf_maker.media import ensure_images
from ptf_maker.render import render_video
from ptf_maker.templates import get_template, list_templates

# Configuração da página
st.set_page_config(
    page_title="ptf_maker - Gerador de Vídeos",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        background: linear-gradient(90deg, #FFD700, #FFA500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 1rem 0;
    }
    .template-card {
        padding: 1rem;
        border-radius: 10px;
        border: 2px solid #ddd;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.3s;
    }
    .template-card:hover {
        border-color: #FFD700;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .success-box {
        padding: 1rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        color: #155724;
    }
    .stProgress > div > div > div > div {
        background-color: #FFD700;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🎬 ptf_maker - Gerador de Vídeos Profissionais</h1>', unsafe_allow_html=True)
st.markdown("### Crie vídeos virais para TikTok e Reels em minutos!")

# Sidebar - Templates
st.sidebar.title("🎨 Templates Profissionais")
st.sidebar.markdown("Escolha um template otimizado para seu nicho:")

# Informações dos templates com emojis
template_info = {
    "finance": {"emoji": "💰", "name": "Finance", "color": "#FFD700", "desc": "Investimentos, Dinheiro"},
    "motivation": {"emoji": "🔥", "name": "Motivação", "color": "#E74C3C", "desc": "Superação, Mindset"},
    "tech": {"emoji": "⚡", "name": "Tech", "color": "#3498DB", "desc": "Tecnologia, IA"},
    "business": {"emoji": "📊", "name": "Business", "color": "#34495E", "desc": "Negócios, Estratégia"},
    "lifestyle": {"emoji": "✨", "name": "Lifestyle", "color": "#FF6B9D", "desc": "Bem-estar, Vida"},
    "education": {"emoji": "📚", "name": "Educação", "color": "#2980B9", "desc": "Conhecimento, Ensino"}
}

# Seleção de template
selected_template = None
for template_key, info in template_info.items():
    if st.sidebar.button(
        f"{info['emoji']} {info['name']}\n{info['desc']}", 
        key=template_key,
        use_container_width=True
    ):
        selected_template = template_key
        st.session_state.template = template_key

# Manter template selecionado
if 'template' not in st.session_state:
    st.session_state.template = 'finance'

current_template = st.session_state.template
template_data = get_template(current_template)

# Mostrar template selecionado
st.sidebar.markdown("---")
st.sidebar.success(f"✅ Template: **{template_info[current_template]['name']}**")

# Main content - Tabs
tab1, tab2, tab3 = st.tabs(["📝 Criar Vídeo", "⚙️ Configurações Avançadas", "📖 Ajuda"])

with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📝 Roteiro do Vídeo")
        
        # Opção de input
        input_method = st.radio(
            "Como você quer fornecer o roteiro?",
            ["Escrever diretamente", "Upload de arquivo"],
            horizontal=True
        )
        
        if input_method == "Escrever diretamente":
            script_text = st.text_area(
                "Digite seu roteiro:",
                height=200,
                placeholder="Gancho: Você sabia que...\n\nConteúdo principal...\n\nCall-to-action no final!",
                help="Dica: 15-25 segundos é ideal. Use frases curtas!"
            )
        else:
            uploaded_file = st.file_uploader(
                "Faça upload do arquivo de roteiro (.txt)",
                type=['txt']
            )
            if uploaded_file:
                script_text = uploaded_file.read().decode('utf-8')
                st.text_area("Preview do roteiro:", script_text, height=200, disabled=True)
            else:
                script_text = ""
        
        # Contador de caracteres
        if script_text:
            char_count = len(script_text)
            estimated_duration = char_count / 15  # ~15 chars por segundo
            
            col_a, col_b, col_c = st.columns(3)
            col_a.metric("Caracteres", char_count)
            col_b.metric("Duração estimada", f"{estimated_duration:.1f}s")
            
            if 10 <= estimated_duration <= 30:
                col_c.success("✅ Duração ideal!")
            elif estimated_duration < 10:
                col_c.warning("⚠️ Muito curto")
            else:
                col_c.error("❌ Muito longo")
    
    with col2:
        st.subheader("🎨 Template Selecionado")
        
        info = template_info[current_template]
        st.markdown(f"""
        <div style='padding: 1rem; background-color: {info['color']}22; border-radius: 10px; border-left: 4px solid {info['color']}'>
            <h2 style='margin: 0;'>{info['emoji']} {info['name']}</h2>
            <p style='margin: 0.5rem 0;'>{info['desc']}</p>
            <p style='margin: 0; font-size: 0.9rem; opacity: 0.8;'>
                Cor: {template_data['primary_color']}<br>
                Efeitos: {'✅' if template_data['effects']['ken_burns'] else '❌'} Zoom | 
                {'✅' if template_data['effects']['transitions'] else '❌'} Transições
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Número de imagens
        num_images = st.slider(
            "🖼️ Número de imagens",
            min_value=3,
            max_value=8,
            value=5,
            help="Mais imagens = vídeo mais dinâmico"
        )
        
        # Animação
        animation_type = st.selectbox(
            "✨ Animação das legendas",
            ["fade", "zoom", "slide"],
            index=0,
            help="Fade = Suave | Zoom = Impacto | Slide = Dinâmico"
        )

    st.markdown("---")
    
    # Música (opcional)
    st.subheader("🎵 Música de Fundo (Opcional)")
    
    col_music1, col_music2 = st.columns([3, 1])
    
    with col_music1:
        music_file = st.file_uploader(
            "Upload de música MP3",
            type=['mp3'],
            help="Músicas instrumentais funcionam melhor. Requer Python 3.10-3.12"
        )
    
    with col_music2:
        if music_file:
            music_volume = st.slider(
                "Volume (%)",
                min_value=5,
                max_value=50,
                value=15,
                help="15-20% é ideal"
            )
        else:
            music_volume = 15
            st.info("Sem música")
    
    st.markdown("---")
    
    # Botão de gerar
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    
    with col_btn2:
        generate_button = st.button(
            "🚀 GERAR VÍDEO PROFISSIONAL",
            type="primary",
            use_container_width=True,
            disabled=not script_text
        )
    
    # Geração do vídeo
    if generate_button and script_text:
        try:
            # Preparar diretórios
            config.OUT_DIR.mkdir(exist_ok=True)
            config.ASSETS_DIR.mkdir(exist_ok=True)
            
            # Progress bar
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # 1. TTS
            status_text.text("🎤 Gerando áudio TTS...")
            progress_bar.progress(20)
            
            audio_path = config.OUT_DIR / "audio.mp3"
            make_tts(script_text, str(audio_path), template_data.get('voice', 'pt-BR-AntonioNeural'))
            
            # 2. Música (se fornecida)
            if music_file:
                status_text.text("🎵 Processando música...")
                progress_bar.progress(30)
                
                music_path = config.ASSETS_DIR / "temp_music.mp3"
                with open(music_path, 'wb') as f:
                    f.write(music_file.getbuffer())
                
                try:
                    from ptf_maker.audio_mixer import mix_audio_with_music
                    mixed_audio_path = config.OUT_DIR / "audio_mixed.mp3"
                    mix_audio_with_music(
                        str(audio_path),
                        str(music_path),
                        str(mixed_audio_path),
                        music_volume / 100
                    )
                    audio_path = mixed_audio_path
                    st.success("✅ Música mixada!")
                except ImportError:
                    st.warning("⚠️ Mixagem de áudio não disponível (Python 3.13+). Continuando sem música...")
            
            # 3. Imagens
            status_text.text("🖼️ Baixando imagens do Pexels...")
            progress_bar.progress(50)
            
            image_paths = ensure_images(
                n=num_images,
                topic=template_data['topic'],
                key=config.PEXELS_KEY,
                force_local=not config.PEXELS_KEY
            )
            
            # 4. Renderização
            status_text.text("🎥 Renderizando vídeo com efeitos profissionais...")
            progress_bar.progress(70)
            
            video_path = config.OUT_DIR / "video.mp4"
            
            effects_config = {
                "ken_burns": template_data['effects']['ken_burns'],
                "transitions": template_data['effects']['transitions'],
                "text_animation": animation_type
            }
            
            render_video(
                bg_paths=image_paths,
                audio_mp3=str(audio_path),
                script_text=script_text,
                out_path=str(video_path),
                title=template_data['title'],
                primary_color=template_data['primary_color'],
                font=template_data['font'],
                font_size=template_data['font_size'],
                effects_config=effects_config
            )
            
            progress_bar.progress(100)
            status_text.text("✅ Vídeo gerado com sucesso!")
            
            # Mostrar resultado
            st.markdown("---")
            st.success("### 🎉 Vídeo Pronto!")
            
            # Preview do vídeo
            st.video(str(video_path))
            
            # Informações do vídeo
            video_size = video_path.stat().st_size / (1024 * 1024)  # MB
            
            col_info1, col_info2, col_info3 = st.columns(3)
            col_info1.metric("Tamanho", f"{video_size:.1f} MB")
            col_info2.metric("Resolução", "1080×1920")
            col_info3.metric("FPS", "30")
            
            # Download
            with open(video_path, 'rb') as f:
                st.download_button(
                    "⬇️ BAIXAR VÍDEO MP4",
                    f,
                    file_name="video_profissional.mp4",
                    mime="video/mp4",
                    use_container_width=True
                )
            
            # Também baixar áudio
            with open(audio_path, 'rb') as f:
                st.download_button(
                    "⬇️ Baixar Áudio MP3",
                    f,
                    file_name="audio.mp3",
                    mime="audio/mp3",
                    use_container_width=True
                )
            
        except Exception as e:
            st.error(f"❌ Erro ao gerar vídeo: {str(e)}")
            st.exception(e)

with tab2:
    st.subheader("⚙️ Configurações Avançadas")
    
    col_adv1, col_adv2 = st.columns(2)
    
    with col_adv1:
        st.markdown("### 🎨 Personalização Visual")
        
        custom_title = st.text_input(
            "Título customizado",
            value=template_data['title'],
            help="Aparece nos primeiros 2.5s"
        )
        
        custom_color = st.color_picker(
            "Cor primária",
            value=template_data['primary_color'],
            help="Cor do título e destaques"
        )
        
        font_size = st.slider(
            "Tamanho da fonte",
            min_value=40,
            max_value=80,
            value=template_data['font_size']
        )
    
    with col_adv2:
        st.markdown("### 🎬 Efeitos Visuais")
        
        enable_ken_burns = st.checkbox(
            "Efeito Ken Burns (zoom)",
            value=True,
            help="Zoom gradual nas imagens"
        )
        
        enable_transitions = st.checkbox(
            "Transições suaves",
            value=True,
            help="Fade in/out entre imagens"
        )
        
        custom_topic = st.text_input(
            "Tópico de busca Pexels",
            value=template_data['topic'],
            help="Palavras-chave para buscar imagens"
        )
    
    st.info("💡 **Dica:** Alterações aqui sobrescrevem as configurações do template selecionado.")

with tab3:
    st.subheader("📖 Como Usar")
    
    st.markdown("""
    ## 🚀 Guia Rápido
    
    ### 1. Escolha um Template
    Na barra lateral, selecione o template que combina com seu nicho:
    - **💰 Finance** - Investimentos, dinheiro
    - **🔥 Motivação** - Superação, mindset (mais viral!)
    - **⚡ Tech** - Tecnologia, IA
    - **📊 Business** - Negócios, estratégia
    
    ### 2. Escreva o Roteiro
    - **15-25 segundos** é ideal
    - Comece com um **gancho forte**
    - Use **frases curtas**
    - Termine com **call-to-action**
    
    ### 3. Adicione Música (Opcional)
    - Músicas **instrumentais** funcionam melhor
    - Volume **15-20%** é ideal
    - Fontes: [Pixabay](https://pixabay.com/music/), [YouTube Audio Library](https://studio.youtube.com/channel/UC/music)
    
    ### 4. Gere e Baixe
    - Clique em **"Gerar Vídeo"**
    - Aguarde ~2-3 minutos
    - **Preview** antes de baixar
    - Download direto em **MP4**
    
    ---
    
    ## 💡 Dicas para Vídeos Virais
    
    ### Roteiro:
    ✅ Gancho impactante nos primeiros 3s  
    ✅ Use números e dados concretos  
    ✅ Quebre em frases de 38 caracteres  
    ✅ Call-to-action claro no final  
    
    ### Visual:
    ✅ 4-6 imagens de alta qualidade  
    ✅ Template matching com nicho  
    ✅ Cores vibrantes chamam atenção  
    
    ### Publicação:
    ✅ Horários de pico (19h-22h)  
    ✅ 5-7 hashtags relevantes  
    ✅ Responda comentários nas primeiras 2h  
    
    ---
    
    ## ❓ FAQ
    
    **P: Quanto tempo leva para gerar?**  
    R: 2-3 minutos em média (depende da quantidade de imagens)
    
    **P: Preciso de chave Pexels?**  
    R: Não obrigatório, mas recomendado para mais variedade de imagens
    
    **P: Música não funciona?**  
    R: Requer Python 3.10-3.12. Com Python 3.13+ funciona sem música
    
    **P: Posso usar comercialmente?**  
    R: Sim! Imagens do Pexels são livres para uso comercial
    
    ---
    
    ## 🔗 Links Úteis
    
    - [Documentação Completa](./PROFISSIONAL.md)
    - [Exemplos de Roteiros](./exemplos/)
    - [GitHub](https://github.com)
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #888;'>Feito com ❤️ por ptf_maker | "
    "Versão Profissional com Efeitos Cinematográficos</div>",
    unsafe_allow_html=True
)
