# Guia Rápido - ptf_maker

## ✅ Instalação Completa (Já Feito)

```powershell
# 1. Criar ambiente virtual
python -m venv .venv

# 2. Instalar dependências
.venv\Scripts\pip install -r requirements.txt

# 3. Configurar chave Pexels (Já configurado no .env)
```

## 🎬 Gerar Vídeo

### Comando Básico (Com Pexels)
```powershell
.venv\Scripts\python -m ptf_maker --script-file exemplo.txt --topic "finance money savings" --images 4
```

### Opções Disponíveis

**Com arquivo de roteiro:**
```powershell
.venv\Scripts\python -m ptf_maker --script-file meu_roteiro.txt --topic "business success" --images 5
```

**Com texto direto:**
```powershell
.venv\Scripts\python -m ptf_maker --script "Seu texto aqui" --topic "motivation" --images 3
```

**Customizar branding:**
```powershell
.venv\Scripts\python -m ptf_maker --script-file exemplo.txt --title "Meu Canal" --primary "#FF0000" --fontsize 65
```

**Usar imagens locais (sem Pexels):**
```powershell
# Adicione imagens JPG/PNG na pasta assets/
.venv\Scripts\python -m ptf_maker --script-file exemplo.txt --no-download
```

## 📂 Saídas

Após executar, você encontrará:
- `out/video.mp4` - Vídeo final 1080×1920
- `out/audio.mp3` - Áudio TTS
- `assets/pexels_*.jpg` - Imagens baixadas do Pexels

## 🎨 Personalização

### Temas de Busca (--topic)
- Finanças: `"finance money savings budget"`
- Motivação: `"motivation success achievement"`
- Negócios: `"business entrepreneur office"`
- Tecnologia: `"technology innovation digital"`

### Cores Primárias (--primary)
- Dourado: `#FFD700` (padrão)
- Vermelho: `#FF0000`
- Azul: `#0066FF`
- Verde: `#00FF00`
- Roxo: `#9B59B6`

### Vozes TTS (--voice)
- `pt-BR-AntonioNeural` (masculina - padrão)
- `pt-BR-FranciscaNeural` (feminina)
- `pt-BR-ThalitaNeural` (feminina jovem)

## 🔧 Scripts Úteis

### Limpar saídas
```powershell
Remove-Item -Recurse -Force out\*
Remove-Item -Force assets\pexels_*.jpg
```

### Ver ajuda completa
```powershell
.venv\Scripts\python -m ptf_maker --help
```

## ⚠️ Notas Importantes

1. **Pillow**: Fixado em versão 10.4.0 para compatibilidade
2. **ImageMagick**: NÃO é necessário (código usa PIL diretamente)
3. **FFmpeg**: Incluído no moviepy via imageio-ffmpeg
4. **Pexels**: 200 requisições/hora, 20.000/mês no plano grátis

## 📊 Status do Último Teste

✅ **SUCESSO** - Vídeo gerado em: `C:\Users\julio\Desktop\gerar_video\out\video.mp4`
- Áudio: 147 KB
- Vídeo: 1.6 MB
- Duração: ~18s
- Resolução: 1080×1920
- FPS: 30
