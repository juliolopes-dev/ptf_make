# ptf_maker - Gerador de Vídeos Profissionais para TikTok

Gerador automatizado de vídeos verticais 1080×1920 para TikTok/Reels a partir de texto. Pipeline completo: **texto → TTS (pt-BR) → b-roll (Pexels) → legendas animadas → música → render MP4**.

## 🚀 NOVO: Recursos Profissionais

✨ **6 Templates Prontos** - Finance, Motivation, Tech, Business, Lifestyle, Education  
🎵 **Música de Fundo** - Mixagem automática com normalização  
🎬 **Efeitos Cinematográficos** - Ken Burns (zoom), transições suaves  
✨ **Legendas Animadas** - Fade, Zoom, Slide  
🎨 **Cores Otimizadas** - Templates psicologicamente escolhidos por nicho  
🌐 **Interface Web** - UI visual com preview integrado (Streamlit)

👉 **Veja [PROFISSIONAL.md](PROFISSIONAL.md) para o guia completo**

## Stack

- **Python 3.10+**
- **MoviePy** - Edição de vídeo
- **edge-tts** - Text-to-Speech em português
- **Pexels API** - Imagens de b-roll
- **FFmpeg** - Codificação de vídeo

## Instalação

### 1. Instalar FFmpeg

**Windows:**
```powershell
# Opção 1: Winget
winget install ffmpeg

# Opção 2: Chocolatey
choco install ffmpeg
```

Adicione o FFmpeg ao PATH do sistema se necessário.

**Verificar instalação:**
```bash
ffmpeg -version
```

### 2. Configurar Python

```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar (Windows)
.venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt
```

### 3. Configurar Pexels API (Opcional)

1. Crie uma conta gratuita em [Pexels](https://www.pexels.com/api/)
2. Copie sua API Key
3. Crie um arquivo `.env` na raiz do projeto:

```bash
cp .env.example .env
```

Edite `.env` e adicione sua chave:
```
PEXELS_KEY=sua_chave_aqui
```

**Nota:** Se não configurar Pexels, o sistema usará imagens locais da pasta `assets/`.

## Uso

### 🌐 Interface Web (RECOMENDADO)

**Opção A: Local (Desenvolvimento)**
```bash
# Iniciar interface visual
streamlit run app.py

# Ou use o script:
.\start_web.ps1
```
Acesse: **http://localhost:8501**

**Opção B: Online - Deploy GRÁTIS (Produção)** ⭐
```bash
# 1. Push para GitHub
git init && git add . && git commit -m "Initial commit"
git remote add origin https://github.com/SEU_USUARIO/ptf-maker.git
git push -u origin main

# 2. Deploy no Streamlit Cloud (grátis)
# Acesse: https://share.streamlit.io
# Click "New app" → Selecione repo → Deploy!
```
Resultado: **https://seu-app.streamlit.app** 🚀

✨ **Recursos da Interface:**
- Preview de vídeo integrado
- Seleção visual de templates
- Upload drag & drop
- Métricas em tempo real
- Download direto

👉 **Ver [DEPLOY_STREAMLIT.md](DEPLOY_STREAMLIT.md) para guia completo de deploy**  
👉 **Ver [INTERFACE_WEB.md](INTERFACE_WEB.md) para guia de uso**

### ⌨️ Linha de Comando (Avançado)

```bash
python -m ptf_maker --script "Seu texto aqui"
```

### Exemplos

**1. Vídeo Profissional com Template (RECOMENDADO):**
```bash
python -m ptf_maker --script-file roteiro.txt --template finance
```

**2. Com Música de Fundo:**
```bash
python -m ptf_maker --script-file roteiro.txt --template motivation --background-music assets/music.mp3
```

**3. Customização Total:**
```bash
python -m ptf_maker --script "Seu texto" --template tech --animation zoom --images 6
```

**4. Render Rápido (sem efeitos):**
```bash
python -m ptf_maker --script-file roteiro.txt --no-effects --no-download
```

## Opções do CLI

### 🎬 Templates (NOVO)
- `--template finance` - Template Finance (Dourado + Verde)
- `--template motivation` - Template Motivação (Vermelho + Laranja)
- `--template tech` - Template Tech (Azul + Roxo)
- `--template business` - Template Negócios (Cinza + Verde Água)
- `--template lifestyle` - Template Lifestyle (Rosa)
- `--template education` - Template Educação (Azul)

### 🎵 Áudio Profissional (NOVO)
- `--background-music arquivo.mp3` - Adicionar música de fundo
- `--music-volume 0.15` - Volume da música (0.0 a 1.0)
- `--voice voz` - Voz do TTS (default: `pt-BR-AntonioNeural`)

### ✨ Efeitos Visuais (NOVO)
- `--animation fade` - Animação de legendas (fade/zoom/slide)
- `--no-effects` - Desabilitar efeitos (render mais rápido)

### Entrada de Texto
- `--script "texto"` - Roteiro direto na linha de comando
- `--script-file arquivo.txt` - Roteiro de um arquivo

### Configurações de Mídia
- `--topic "termo"` - Termo de busca no Pexels
- `--images N` - Número de imagens (default: `4`)
- `--no-download` - Usa apenas imagens locais de `assets/`

### Configurações de Branding
- `--title "Título"` - Título exibido nos primeiros 2.5s
- `--primary "#HEX"` - Cor primária em hexadecimal
- `--font "Nome"` - Nome da fonte (default: `Arial`)
- `--fontsize N` - Tamanho da fonte (default: `58`)

## Estrutura do Projeto

```
ptf_maker/
├── ptf_maker/
│   ├── __init__.py       # Metadados do pacote
│   ├── __main__.py       # Entry point do módulo
│   ├── cli.py            # Interface CLI
│   ├── config.py         # Configurações e constantes
│   ├── tts.py            # Geração de áudio TTS
│   ├── media.py          # Download de imagens (Pexels)
│   ├── captions.py       # Geração de legendas
│   └── render.py         # Renderização do vídeo
├── assets/               # Imagens locais (fallback)
├── out/                  # Saídas (áudio e vídeo)
├── .env                  # Configurações (não comitar)
├── .env.example          # Exemplo de configuração
├── requirements.txt      # Dependências Python
└── README.md            # Este arquivo
```

## Pipeline de Geração

1. **Texto** → Roteiro fornecido via CLI
2. **TTS** → Geração de áudio em pt-BR com edge-tts
3. **B-roll** → Download de imagens do Pexels (ou uso de imagens locais)
4. **Legendas** → Texto dividido em linhas curtas (~38 caracteres)
5. **Render** → Vídeo 1080×1920, 30fps, com título e legendas sincronizadas
6. **Saída** → `out/video.mp4` + `out/audio.mp3`

## Saídas

- **out/audio.mp3** - Áudio TTS gerado
- **out/video.mp4** - Vídeo final renderizado (H.264 + AAC)

## Troubleshooting

### FFmpeg não encontrado
Certifique-se de que o FFmpeg está no PATH:
```bash
where ffmpeg  # Windows
which ffmpeg  # Linux/Mac
```

### Erro de imagens
Se não tiver Pexels configurado:
1. Use `--no-download`
2. Adicione imagens JPG/PNG na pasta `assets/`

### Erro de fonte
Se a fonte especificada não existir, use fontes do sistema:
- Windows: `Arial`, `Calibri`, `Segoe UI`
- Deixe o padrão se não tiver certeza

### API Pexels não funciona
- Verifique se a chave no `.env` está correta
- Teste a chave em: https://www.pexels.com/api/documentation/
- Use `--no-download` como fallback

## Roadmap

- [ ] Suporte a múltiplas vozes TTS
- [ ] Templates de estilo pré-configurados
- [ ] Normalização de loudness do áudio
- [ ] Animações de entrada/saída de legendas
- [ ] Suporte a vídeos de b-roll (não apenas imagens)

## Licença

MIT

## Autor

Por Trás da Fortuna - Gerador de Conteúdo
