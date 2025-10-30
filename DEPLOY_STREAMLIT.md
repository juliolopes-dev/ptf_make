# 🚀 Deploy Gratuito no Streamlit Cloud

## Guia Passo a Passo (10 minutos)

### ✅ Pré-requisitos
- Conta GitHub (criar em https://github.com se não tiver)
- Git instalado no Windows

---

## 📝 Passo 1: Subir para GitHub

### 1.1 Criar Repositório no GitHub

1. Acesse: https://github.com/new
2. Preencha:
   - **Repository name:** `ptf-maker` (ou outro nome)
   - **Description:** "Gerador profissional de vídeos TikTok/Reels"
   - **Visibilidade:** Public (ou Private, funciona nos dois)
3. **NÃO** marque "Add README" (já temos)
4. Click "Create repository"

### 1.2 Fazer Push do Projeto

Abra PowerShell no diretório do projeto e execute:

```powershell
# Inicializar Git (se ainda não fez)
git init

# Adicionar todos os arquivos
git add .

# Fazer commit
git commit -m "Initial commit - ptf_maker com Streamlit"

# Conectar ao repositório (substitua SEU_USUARIO e NOME_REPO)
git remote add origin https://github.com/SEU_USUARIO/NOME_REPO.git

# Fazer push
git branch -M main
git push -u origin main
```

**Nota:** O Git vai pedir login do GitHub. Use suas credenciais.

---

## 🌐 Passo 2: Deploy no Streamlit Cloud

### 2.1 Criar Conta Streamlit Cloud

1. Acesse: https://share.streamlit.io
2. Click "Sign up"
3. **Sign up with GitHub** (recomendado)
4. Autorize o Streamlit a acessar seus repositórios

### 2.2 Criar Nova App

1. Click no botão **"New app"**
2. Preencha:
   - **Repository:** Selecione seu repositório `ptf-maker`
   - **Branch:** `main`
   - **Main file path:** `app.py`
3. Click em **"Advanced settings"** (opcional mas recomendado)
   - **Python version:** `3.10`
   - **Secrets:** Adicione sua chave Pexels (veja próximo passo)
4. Click **"Deploy!"**

### 2.3 Configurar Secrets (Chave Pexels)

Na seção "Secrets" das Advanced settings, adicione:

```toml
PEXELS_KEY = "SUA_CHAVE_PEXELS_AQUI"
```

**Substitua `SUA_CHAVE_PEXELS_AQUI` pela sua chave real!**

### 2.4 Aguardar Deploy

O Streamlit vai:
1. 📦 Instalar dependências (~2 minutos)
2. 🚀 Iniciar aplicação (~1 minuto)
3. ✅ Mostrar URL da sua app

**Tempo total:** 3-5 minutos

---

## 🎉 Passo 3: Testar Sua App

### 3.1 Acessar URL

Você receberá uma URL tipo:
```
https://seu-app-aleatorio.streamlit.app
```

### 3.2 Testar Geração

1. Abra a URL no navegador
2. Escolha um template
3. Cole um roteiro de teste
4. Click "Gerar Vídeo"
5. Aguarde e baixe!

---

## 🔄 Atualizações Automáticas

Sempre que você fizer mudanças:

```powershell
git add .
git commit -m "Descrição da mudança"
git push
```

O Streamlit **automaticamente** faz re-deploy! ✨

---

## ⚙️ Configurações Importantes

### Gerenciar Secrets

1. Acesse sua app no Streamlit Cloud
2. Click em **"Settings"** (⚙️)
3. Aba **"Secrets"**
4. Edite os secrets
5. Click **"Save"**

### Logs e Debugging

1. Acesse sua app
2. Click em **"Manage app"**
3. Veja logs em tempo real
4. Útil para debug

### Reiniciar App

Se algo der errado:
1. Click **"⋮"** (três pontos)
2. **"Reboot app"**

---

## 💡 Dicas Importantes

### ✅ Boas Práticas

1. **Nunca commite secrets**
   - `.env` está no `.gitignore`
   - Configure secrets no painel Streamlit

2. **Teste localmente primeiro**
   ```powershell
   streamlit run app.py
   ```

3. **Commits descritivos**
   ```powershell
   git commit -m "Adicionar template Business"
   ```

4. **Use branches para testes**
   ```powershell
   git checkout -b nova-feature
   # testar mudanças
   git merge main
   ```

### 🐛 Troubleshooting

**App não inicia:**
- Verifique logs no dashboard
- Confirme que `requirements.txt` está correto
- Python version = 3.10 ou 3.11

**Secrets não funcionam:**
- Formato correto: `KEY = "value"`
- Sem espaços extras
- Entre aspas duplas

**Deploy muito lento:**
- Normal na primeira vez (instala tudo)
- Próximos deploys são mais rápidos (cache)

**Erro de memória:**
- Streamlit grátis = 1 GB RAM
- Reduza número de imagens simultâneas
- Otimize código

---

## 📊 Limites da Versão Gratuita

| Recurso | Limite |
|---------|--------|
| **Apps públicos** | 3 |
| **Apps privados** | 1 |
| **RAM** | 1 GB |
| **CPU** | 1 core |
| **Storage** | Limitado |
| **Usuários simultâneos** | ~10 |
| **Uptime** | Apps inativos dormem após 7 dias |

**Quando exceder:** Upgrade para Streamlit Cloud Pro ($20/mês)

---

## 🎯 Checklist Final

Antes de compartilhar sua app:

- [ ] App funciona localmente
- [ ] Push no GitHub completo
- [ ] Secrets configurados corretamente
- [ ] Deploy sem erros
- [ ] Testado geração de vídeo
- [ ] Preview funciona
- [ ] Download funciona
- [ ] Templates todos OK

---

## 🔗 Links Úteis

- **Streamlit Cloud:** https://share.streamlit.io
- **Documentação:** https://docs.streamlit.io/streamlit-community-cloud
- **GitHub:** https://github.com
- **Suporte:** https://discuss.streamlit.io

---

## 🆘 Precisa de Ajuda?

Se algo não funcionar:

1. **Verifique logs** no dashboard Streamlit
2. **Teste localmente** primeiro
3. **Veja documentação** oficial
4. **Stack Overflow** ou comunidade Streamlit

---

**Pronto! Sua app estará online e funcionando! 🎉**

URL para compartilhar: `https://seu-app.streamlit.app`
