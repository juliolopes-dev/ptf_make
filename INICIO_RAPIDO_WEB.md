# 🚀 Início Rápido - Interface Web

## Em 3 Passos Para Seu Primeiro Vídeo!

### ⚡ Passo 1: Instalar Streamlit

```powershell
.venv\Scripts\pip install streamlit
```

### ⚡ Passo 2: Iniciar Interface

```powershell
# Opção 1: Script automático (MAIS FÁCIL)
.\start_web.ps1

# Opção 2: Comando manual
streamlit run app.py
```

### ⚡ Passo 3: Criar Vídeo

1. **Navegador abre automaticamente** em `http://localhost:8501`

2. **Escolha template** na barra lateral:
   - 💰 Finance (recomendado para começar)

3. **Cole seu roteiro** ou faça upload de arquivo

4. **Clique "GERAR VÍDEO"**

5. **Aguarde 2-3 minutos** ☕

6. **Preview + Download** 🎉

---

## 📱 O Que Você Verá

```
┌─────────────────────────────────────────────┐
│  🎬 ptf_maker - Gerador de Vídeos          │
├─────────────────────────────────────────────┤
│                                             │
│  Sidebar:                                   │
│  🎨 Templates                               │
│  [ 💰 Finance        ]  ← Clique aqui      │
│  [ 🔥 Motivação      ]                      │
│  [ ⚡ Tech           ]                      │
│                                             │
│  Principal:                                 │
│  📝 Roteiro:                                │
│  ┌─────────────────────────────────────┐   │
│  │ Digite aqui...                      │   │
│  │                                     │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  🖼️ Imagens: [5]                           │
│  ✨ Animação: [Fade ▼]                     │
│                                             │
│  [ 🚀 GERAR VÍDEO PROFISSIONAL ]           │
│                                             │
└─────────────────────────────────────────────┘
```

---

## ✅ Checklist Rápido

Antes de gerar:
- [ ] Ambiente virtual ativado
- [ ] Streamlit instalado
- [ ] Chave Pexels configurada (opcional)
- [ ] Roteiro pronto (15-25s)

Durante geração:
- [ ] Progress bar visível
- [ ] Aguardar conclusão (não feche)

Após gerar:
- [ ] Preview do vídeo
- [ ] Baixar MP4
- [ ] Testar em celular
- [ ] Publicar!

---

## 💡 Dicas Primeira Vez

### Roteiro Teste:
```
💰 Você sabia que 70% dos milionários não herdaram fortuna?

Eles usaram 3 regras simples:

1. Investir 10% todo mês
2. Nunca gastar mais do que ganham
3. Multiplicar renda com side hustles

Comece hoje. Seu eu do futuro agradece!
```

### Configuração Simples:
- **Template:** Finance
- **Imagens:** 5
- **Animação:** Fade
- **Música:** Sem (mais rápido)

### Tempo Esperado:
- TTS: ~30s
- Imagens: ~45s
- Render: ~90s
- **Total: ~3 minutos**

---

## 🐛 Se Algo Der Errado

### Interface não abre:
```powershell
# Reinstalar Streamlit
.venv\Scripts\pip install --upgrade streamlit

# Tentar novamente
streamlit run app.py
```

### Erro de porta ocupada:
```powershell
# Usar porta diferente
streamlit run app.py --server.port 8502
```

### Vídeo não gera:
1. Veja mensagens de erro no terminal
2. Verifique se `.env` existe
3. Tente com menos imagens (3)
4. Tente sem música primeiro

---

## 🎯 Próximos Passos

Depois do primeiro vídeo:

1. ✅ **Testar outros templates** (Motivation é viral!)
2. ✅ **Adicionar música** de fundo
3. ✅ **Experimentar animações** (Zoom, Slide)
4. ✅ **Criar 5 vídeos** diferentes
5. ✅ **Publicar e medir** engajamento

---

## 📊 Comparação: Templates

| Template | Melhor Para | Viralidade |
|----------|-------------|------------|
| 💰 Finance | Investimentos, Dinheiro | ⭐⭐⭐⭐ |
| 🔥 Motivation | Superação, Frases | ⭐⭐⭐⭐⭐ |
| ⚡ Tech | IA, Tecnologia | ⭐⭐⭐⭐ |
| 📊 Business | Negócios, Carreira | ⭐⭐⭐ |
| ✨ Lifestyle | Bem-estar, Vida | ⭐⭐⭐⭐ |
| 📚 Education | Educação, Dicas | ⭐⭐⭐ |

---

## 🎬 Workflow Ideal

### Setup Inicial (1x):
```powershell
.\start_web.ps1
```

### Para Cada Vídeo (2-3 min):
1. Colar roteiro
2. Escolher template
3. Gerar
4. Preview
5. Download
6. Publicar

### Produção em Lote:
1. Preparar 10 roteiros
2. Abrir interface
3. Gerar todos (30 min)
4. Agendar publicações

---

## 🌟 Recursos Extras

### Atalhos Úteis:
- **Ctrl + R** - Recarregar interface
- **Ctrl + C** - Parar servidor (no terminal)

### Melhorar Performance:
- Usar menos imagens (3-4)
- Desabilitar música (se não precisar)
- Usar `--no-effects` no CLI (mais rápido)

### Deploy Online:
- Ver [INTERFACE_WEB.md](INTERFACE_WEB.md)
- Streamlit Cloud (grátis)
- Compartilhar com clientes

---

**Pronto! Em menos de 5 minutos você terá seu primeiro vídeo profissional! 🚀**

Comece agora:
```powershell
.\start_web.ps1
```
