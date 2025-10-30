# 🌐 Interface Web - ptf_maker

## 🎨 Interface Visual Profissional

A interface Streamlit oferece uma experiência **visual e intuitiva** para criar vídeos profissionais sem precisar usar a linha de comando.

---

## 🚀 Como Iniciar

### 1. Instalar Streamlit (se ainda não instalou)

```powershell
.venv\Scripts\pip install streamlit
```

### 2. Iniciar Interface Web

```powershell
# Ativar ambiente virtual
.venv\Scripts\activate

# Iniciar Streamlit
streamlit run app.py
```

A interface abrirá automaticamente no navegador em: **http://localhost:8501**

---

## 📱 Recursos da Interface

### ✨ Página Principal - Criar Vídeo

#### 1. **Seleção de Template (Sidebar)**
- 6 templates profissionais clicáveis
- Visualização de cores e descrição
- Template selecionado destacado

#### 2. **Input de Roteiro**
**Duas opções:**
- ✍️ **Escrever diretamente** - Editor de texto integrado
- 📤 **Upload de arquivo** - Drag & drop de arquivo .txt

**Métricas em tempo real:**
- Contador de caracteres
- Duração estimada do vídeo
- Indicador visual (ideal/curto/longo)

#### 3. **Configuração de Imagens**
- Slider para escolher quantidade (3-8 imagens)
- Seleção de animação (Fade/Zoom/Slide)
- Preview das configurações do template

#### 4. **Música de Fundo (Opcional)**
- Upload de arquivo MP3
- Slider de volume (5-50%)
- Indicador se música está ativa

#### 5. **Geração do Vídeo**
- Botão grande e destacado
- Progress bar animada com status
- Etapas mostradas em tempo real:
  - 🎤 Gerando áudio TTS...
  - 🎵 Processando música...
  - 🖼️ Baixando imagens...
  - 🎥 Renderizando vídeo...

#### 6. **Resultado**
- ✅ **Preview integrado** do vídeo gerado
- 📊 **Métricas**: tamanho, resolução, FPS
- ⬇️ **Download direto** MP4 e MP3
- 🎉 Mensagem de sucesso

---

### ⚙️ Configurações Avançadas

#### Personalização Visual:
- Título customizado
- Color picker para cor primária
- Slider de tamanho de fonte

#### Efeitos Visuais:
- Toggle para Ken Burns (zoom)
- Toggle para transições
- Tópico customizado do Pexels

**Nota:** Sobrescreve configurações do template

---

### 📖 Ajuda

#### Guia Rápido:
- Passo a passo ilustrado
- Dicas para vídeos virais
- Recomendações de roteiro

#### FAQ:
- Tempo de geração
- Chave Pexels
- Compatibilidade de música
- Uso comercial

#### Links Úteis:
- Documentação completa
- Exemplos de roteiros
- Recursos externos

---

## 💡 Vantagens da Interface Web

### Para Criadores de Conteúdo:
✅ **Zero conhecimento técnico** necessário  
✅ **Preview antes de baixar**  
✅ **Interface intuitiva** com feedbacks visuais  
✅ **Mobile-friendly** (acesse do celular)  

### Para Produção:
✅ **Mais rápido** que linha de comando  
✅ **Menos erros** (validações integradas)  
✅ **Iteração rápida** (testar templates)  
✅ **Compartilhável** (enviar link para clientes)  

---

## 🎯 Workflow Recomendado

### Criação Rápida (5 minutos):
1. Abrir interface: `streamlit run app.py`
2. Escolher template na sidebar
3. Colar roteiro
4. Clicar "Gerar Vídeo"
5. Preview e download

### Produção em Lote:
1. Preparar 10 roteiros em .txt
2. Abrir interface
3. Para cada roteiro:
   - Upload do arquivo
   - Gerar vídeo
   - Baixar MP4
   - Renomear (video_1.mp4, video_2.mp4...)

### A/B Testing:
1. Mesmo roteiro
2. Testar 3 templates diferentes
3. Testar 3 animações diferentes
4. Publicar e medir engajamento
5. Usar o mais efetivo

---

## 🖥️ Atalhos de Teclado

| Atalho | Ação |
|--------|------|
| `Ctrl + R` | Recarregar interface |
| `Ctrl + Shift + R` | Limpar cache |
| `Esc` | Fechar modais |

---

## 🌐 Deploy Online (Opcional)

### Streamlit Cloud (Grátis):

1. **Criar conta** em [share.streamlit.io](https://share.streamlit.io)

2. **Fazer upload** do projeto para GitHub

3. **Conectar repositório** no Streamlit Cloud

4. **Deploy automático** - Interface online!

**Vantagens:**
- Acesso de qualquer lugar
- Compartilhar com clientes
- Sem custo
- HTTPS automático

**Limitações:**
- Recursos limitados (grátis)
- Tempo de processamento maior
- Melhor para demos

---

## 🎨 Customização da Interface

### Cores e Tema:

Edite `.streamlit/config.toml` (criar se não existir):

```toml
[theme]
primaryColor = "#FFD700"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#262730"
font = "sans serif"
```

### Logo Customizado:

No `app.py`, adicione:
```python
st.sidebar.image("assets/logo.png", width=200)
```

---

## 🐛 Troubleshooting

### Interface não abre:
```powershell
# Verificar se Streamlit instalado
.venv\Scripts\pip list | Select-String streamlit

# Reinstalar se necessário
.venv\Scripts\pip install --upgrade streamlit
```

### Erro ao gerar vídeo:
- Verifique se `.env` está configurado
- Teste primeiro no CLI
- Veja logs no terminal do Streamlit

### Preview não funciona:
- Alguns navegadores bloqueiam vídeo
- Tente Chrome ou Edge
- Download ainda funciona

### Música não mixa:
- Python 3.13+ não suporta pydub
- Use Python 3.10-3.12
- Ou continue sem música (efeitos funcionam)

---

## 📊 Comparação: Web UI vs CLI

| Aspecto | Interface Web | CLI |
|---------|---------------|-----|
| **Facilidade** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Velocidade** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Preview** | ✅ Integrado | ❌ Manual |
| **Templates** | ✅ Visual | ⚙️ Parâmetro |
| **Validação** | ✅ Tempo real | ❌ Após erro |
| **Para Iniciantes** | ✅ Perfeito | ⚠️ Intermediário |
| **Automação** | ❌ | ✅ Scripts |
| **Compartilhar** | ✅ Deploy | ❌ |

---

## 🎓 Casos de Uso

### 1. Criador Solo:
**Use:** Interface Web  
**Por quê:** Visual, rápido, preview integrado

### 2. Agência (múltiplos clientes):
**Use:** Interface Web + Deploy  
**Por quê:** Clientes usam sozinhos, branded

### 3. Produção em Massa:
**Use:** CLI com scripts  
**Por quê:** Automação, batch processing

### 4. A/B Testing:
**Use:** Interface Web  
**Por quê:** Fácil testar variações

---

## 🔗 Próximos Passos

1. ✅ **Testar interface** com roteiros de exemplo
2. ✅ **Explorar templates** (todos os 6)
3. ✅ **Fazer primeiro vídeo** e publicar
4. 📊 **Analisar métricas** de engajamento
5. 🎯 **Otimizar** baseado em resultados

---

## 💬 Dicas de Uso

### Primeira Vez:
1. Comece com template **Finance** ou **Motivation**
2. Use roteiro curto (15s)
3. Sem música (mais rápido)
4. Gere e veja o preview
5. Experimente outros templates

### Produção Regular:
1. Prepare roteiros em lote
2. Escolha 1-2 templates principais
3. Adicione música (biblioteca própria)
4. Gere múltiplos vídeos
5. Agende publicações

### Otimização:
1. A/B test templates
2. Varie animações
3. Teste com/sem música
4. Meça engajamento
5. Itere baseado em dados

---

**Interface pronta para uso! 🎉**

Inicie agora com:
```powershell
streamlit run app.py
```
