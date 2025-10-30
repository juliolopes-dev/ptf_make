# ═══════════════════════════════════════════════════════════════
# COMANDOS PARA DEPLOY NO STREAMLIT CLOUD (GRÁTIS)
# ═══════════════════════════════════════════════════════════════
#
# Execute este arquivo: .\comandos_deploy.ps1
# Ou copie os comandos linha por linha
#
# ═══════════════════════════════════════════════════════════════

Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  🚀 DEPLOY GRATUITO - STREAMLIT CLOUD" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# ─────────────────────────────────────────────────────────────────
# PASSO 1: Verificações
# ─────────────────────────────────────────────────────────────────

Write-Host "📋 PASSO 1: Verificações iniciais..." -ForegroundColor Yellow
Write-Host ""

# Verificar Git
$gitInstalled = Get-Command git -ErrorAction SilentlyContinue
if (-not $gitInstalled) {
    Write-Host "❌ Git não está instalado!" -ForegroundColor Red
    Write-Host "Instale em: https://git-scm.com/download/win" -ForegroundColor Gray
    exit 1
}
Write-Host "✅ Git instalado" -ForegroundColor Green

# Verificar se está no diretório correto
if (-not (Test-Path "app.py")) {
    Write-Host "❌ Arquivo app.py não encontrado!" -ForegroundColor Red
    Write-Host "Execute este script na pasta do projeto" -ForegroundColor Gray
    exit 1
}
Write-Host "✅ Diretório correto" -ForegroundColor Green

Write-Host ""

# ─────────────────────────────────────────────────────────────────
# PASSO 2: Configuração Git
# ─────────────────────────────────────────────────────────────────

Write-Host "📝 PASSO 2: Configurando Git..." -ForegroundColor Yellow
Write-Host ""

# Verificar se já é um repositório Git
if (Test-Path ".git") {
    Write-Host "⚠️  Repositório Git já existe" -ForegroundColor Yellow
    $resposta = Read-Host "Deseja reinicializar? (s/N)"
    if ($resposta -eq "s" -or $resposta -eq "S") {
        Remove-Item -Recurse -Force .git
        Write-Host "✅ Repositório reinicializado" -ForegroundColor Green
    }
}

if (-not (Test-Path ".git")) {
    Write-Host "Inicializando repositório Git..." -ForegroundColor Gray
    git init
    Write-Host "✅ Git inicializado" -ForegroundColor Green
}

Write-Host ""

# ─────────────────────────────────────────────────────────────────
# PASSO 3: Commit
# ─────────────────────────────────────────────────────────────────

Write-Host "💾 PASSO 3: Preparando commit..." -ForegroundColor Yellow
Write-Host ""

Write-Host "Adicionando arquivos..." -ForegroundColor Gray
git add .
Write-Host "✅ Arquivos adicionados" -ForegroundColor Green

Write-Host "Criando commit..." -ForegroundColor Gray
git commit -m "Deploy ptf_maker - Interface Streamlit profissional"
Write-Host "✅ Commit criado" -ForegroundColor Green

Write-Host ""

# ─────────────────────────────────────────────────────────────────
# PASSO 4: GitHub
# ─────────────────────────────────────────────────────────────────

Write-Host "🌐 PASSO 4: Conectar ao GitHub..." -ForegroundColor Yellow
Write-Host ""

Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "  ATENÇÃO: Você precisa criar o repositório no GitHub!" -ForegroundColor Yellow
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Acesse: https://github.com/new" -ForegroundColor White
Write-Host "2. Nome do repositório: ptf-maker" -ForegroundColor White
Write-Host "3. Público ou Privado: qualquer um" -ForegroundColor White
Write-Host "4. NÃO marque 'Add README'" -ForegroundColor White
Write-Host "5. Click 'Create repository'" -ForegroundColor White
Write-Host ""

$continuar = Read-Host "Repositório criado no GitHub? (s/N)"
if ($continuar -ne "s" -and $continuar -ne "S") {
    Write-Host "❌ Crie o repositório primeiro e execute o script novamente" -ForegroundColor Red
    exit 1
}

Write-Host ""
$githubUser = Read-Host "Digite seu username do GitHub"
$repoName = Read-Host "Digite o nome do repositório (padrão: ptf-maker)"

if ([string]::IsNullOrWhiteSpace($repoName)) {
    $repoName = "ptf-maker"
}

$repoUrl = "https://github.com/$githubUser/$repoName.git"

Write-Host ""
Write-Host "Conectando ao repositório: $repoUrl" -ForegroundColor Gray

# Verificar se já tem remote
$remoteExists = git remote | Select-String "origin"
if ($remoteExists) {
    Write-Host "⚠️  Remote 'origin' já existe, removendo..." -ForegroundColor Yellow
    git remote remove origin
}

git remote add origin $repoUrl
Write-Host "✅ Repositório conectado" -ForegroundColor Green

Write-Host ""

# ─────────────────────────────────────────────────────────────────
# PASSO 5: Push
# ─────────────────────────────────────────────────────────────────

Write-Host "🚀 PASSO 5: Enviando para GitHub..." -ForegroundColor Yellow
Write-Host ""

Write-Host "Fazendo push (pode pedir suas credenciais do GitHub)..." -ForegroundColor Gray
git branch -M main
git push -u origin main

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ Push concluído com sucesso!" -ForegroundColor Green
} else {
    Write-Host "❌ Erro ao fazer push" -ForegroundColor Red
    Write-Host "Verifique suas credenciais do GitHub" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# ─────────────────────────────────────────────────────────────────
# PASSO 6: Instruções Streamlit
# ─────────────────────────────────────────────────────────────────

Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  ✅ CÓDIGO NO GITHUB - PRÓXIMO PASSO" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

Write-Host "Agora faça o deploy no Streamlit Cloud:" -ForegroundColor White
Write-Host ""
Write-Host "1️⃣  Acesse: https://share.streamlit.io" -ForegroundColor Yellow
Write-Host "2️⃣  Click 'Sign up with GitHub'" -ForegroundColor Yellow
Write-Host "3️⃣  Autorize o Streamlit" -ForegroundColor Yellow
Write-Host "4️⃣  Click 'New app'" -ForegroundColor Yellow
Write-Host ""
Write-Host "5️⃣  Preencha:" -ForegroundColor Yellow
Write-Host "    Repository: $githubUser/$repoName" -ForegroundColor Gray
Write-Host "    Branch: main" -ForegroundColor Gray
Write-Host "    Main file: app.py" -ForegroundColor Gray
Write-Host ""
Write-Host "6️⃣  Click 'Advanced settings'" -ForegroundColor Yellow
Write-Host "    Python version: 3.10" -ForegroundColor Gray
Write-Host ""
Write-Host "7️⃣  Secrets - Adicione sua chave Pexels:" -ForegroundColor Yellow
Write-Host "    PEXELS_KEY = `"SUA_CHAVE_AQUI`"" -ForegroundColor Gray
Write-Host ""
Write-Host "8️⃣  Click 'Deploy!'" -ForegroundColor Yellow
Write-Host ""
Write-Host "⏳ Aguarde 3-5 minutos para o deploy concluir..." -ForegroundColor Cyan
Write-Host ""
Write-Host "🎉 Sua app estará online em:" -ForegroundColor Green
Write-Host "   https://seu-app.streamlit.app" -ForegroundColor White
Write-Host ""

Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host "  ✨ DEPLOY INICIADO COM SUCESSO!" -ForegroundColor Green
Write-Host "═══════════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host ""

# Abrir URLs automaticamente
Write-Host "Deseja abrir os sites no navegador? (s/N)" -ForegroundColor Yellow
$abrirSites = Read-Host

if ($abrirSites -eq "s" -or $abrirSites -eq "S") {
    Start-Process "https://github.com/$githubUser/$repoName"
    Start-Sleep -Seconds 2
    Start-Process "https://share.streamlit.io"
    Write-Host "✅ Sites abertos!" -ForegroundColor Green
}

Write-Host ""
Write-Host "📚 Para mais detalhes, veja:" -ForegroundColor White
Write-Host "   - COMECE_AQUI.md" -ForegroundColor Gray
Write-Host "   - DEPLOY_STREAMLIT.md" -ForegroundColor Gray
Write-Host ""
