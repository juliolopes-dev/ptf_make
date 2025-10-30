# 🎯 COMECE AQUI - Deploy Gratuito em 10 Minutos

## 📋 O Que Você Vai Fazer

Colocar sua interface web **ONLINE e GRÁTIS** no Streamlit Cloud!

**Resultado:** Link público tipo `https://ptf-maker.streamlit.app`

---

## ✅ Você Precisa de:

- [ ] Conta GitHub (criar em 2 minutos)
- [ ] 10 minutos livres
- [ ] Sua chave Pexels (você já tem!)

---

## 🚀 3 PASSOS SIMPLES

### 📦 PASSO 1: GitHub (3 min)

#### 1.1 Criar Conta
👉 https://github.com/signup

#### 1.2 Criar Repositório
👉 https://github.com/new
- Nome: `ptf-maker`
- Público: ✅
- Click "Create repository"

#### 1.3 Fazer Push
Abra PowerShell **nesta pasta** e execute:

```powershell
# Copie e cole linha por linha:

git init

git add .

git commit -m "Deploy ptf_maker"

git remote add origin https://github.com/SEU_USUARIO/ptf-maker.git

git push -u origin main
```

**⚠️ Substitua `SEU_USUARIO` pelo seu username do GitHub!**

---

### 🌐 PASSO 2: Streamlit Cloud (5 min)

#### 2.1 Criar Conta Streamlit
👉 https://share.streamlit.io
- Click "Sign up with GitHub"
- Autorize o acesso

#### 2.2 Criar App
1. Click **"New app"**
2. Preencha:
   ```
   Repository: ptf-maker
   Branch: main
   Main file: app.py
   ```
3. Click **"Advanced settings"**
4. Python version: `3.10`

#### 2.3 Adicionar Secret (Sua Chave Pexels)
Na seção "Secrets", adicione:

```toml
PEXELS_KEY = "HOGVRRduhEfweaCN28TUD0sjQpMMzYWkmfwHFVOEyD1uk2Sy9EibRykK"
```

**⚠️ Cole SUA chave real acima!**

#### 2.4 Deploy!
Click no botão azul **"Deploy!"**

---

### ⏳ PASSO 3: Aguardar (2 min)

Streamlit vai:
1. ⏳ Instalar dependências
2. ⏳ Iniciar aplicação
3. ✅ Mostrar sua URL!

**Pronto!** Sua app está online! 🎉

---

## 🎊 Resultado Final

Você terá:

✅ Interface web rodando 24/7  
✅ Link público para compartilhar  
✅ HTTPS automático (seguro)  
✅ Atualizações automáticas (push = deploy)  
✅ **100% GRÁTIS** 💰

**Exemplo de URL:**
```
https://ptf-maker-abc123.streamlit.app
```

---

## 🔄 Fazer Mudanças Depois

Sempre que quiser atualizar:

```powershell
git add .
git commit -m "Descrição da mudança"
git push
```

Streamlit **re-deploya automaticamente!** ✨

---

## 💡 Dicas

### ✅ Teste Localmente Primeiro
```powershell
streamlit run app.py
```

### ✅ Veja Logs
No dashboard Streamlit → "Manage app" → Logs

### ✅ Reinicie Se Precisar
Dashboard → ⋮ → "Reboot app"

---

## 🐛 Se Algo Der Errado

**App não inicia?**
- Veja os logs no dashboard
- Confirme que secrets estão corretos
- Tente "Reboot app"

**Git pede login?**
- Use username + password do GitHub
- Ou configure SSH keys

**Erro ao fazer push?**
```powershell
# Se der erro, tente:
git pull origin main --allow-unrelated-histories
git push -u origin main --force
```

---

## 📚 Documentação Completa

Para mais detalhes, veja:

- **[DEPLOY_STREAMLIT.md](DEPLOY_STREAMLIT.md)** - Guia completo
- **[DEPLOY_RAPIDO.txt](DEPLOY_RAPIDO.txt)** - Comandos resumidos
- **[INTERFACE_WEB.md](INTERFACE_WEB.md)** - Como usar a interface

---

## 🎯 Checklist Final

Antes de considerar pronto:

- [ ] Push no GitHub OK
- [ ] Deploy no Streamlit OK
- [ ] Secret Pexels configurado
- [ ] App iniciou sem erros
- [ ] Testei gerar um vídeo
- [ ] Download funciona
- [ ] Compartilhei o link! 🎉

---

## 🆘 Precisa de Ajuda?

**Problemas com Git:**
- https://docs.github.com/get-started

**Problemas com Streamlit:**
- https://docs.streamlit.io/streamlit-community-cloud

**Problemas com o App:**
- Veja os logs no dashboard
- Teste localmente primeiro

---

## 🎉 COMEÇAR AGORA!

1. **Abra PowerShell** nesta pasta
2. **Siga o PASSO 1** (GitHub)
3. **Siga o PASSO 2** (Streamlit)
4. **Aguarde PASSO 3** (Deploy)
5. **Compartilhe seu link!** 🚀

---

**Boa sorte! Sua app estará online em minutos! 💪**
