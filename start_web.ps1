# Script para iniciar interface web do ptf_maker
# Execute: .\start_web.ps1

Write-Host "=== ptf_maker - Interface Web ===" -ForegroundColor Cyan
Write-Host ""

# Verificar se venv existe
if (-not (Test-Path ".venv\Scripts\activate.ps1")) {
    Write-Host "⚠️  Ambiente virtual não encontrado!" -ForegroundColor Yellow
    Write-Host "Execute primeiro: python -m venv .venv" -ForegroundColor Gray
    exit 1
}

# Verificar se Streamlit está instalado
Write-Host "Verificando Streamlit..." -ForegroundColor Yellow
$streamlitInstalled = & ".venv\Scripts\pip.exe" list | Select-String "streamlit"

if (-not $streamlitInstalled) {
    Write-Host "📦 Instalando Streamlit..." -ForegroundColor Yellow
    & ".venv\Scripts\pip.exe" install streamlit
    Write-Host "✓ Streamlit instalado!" -ForegroundColor Green
} else {
    Write-Host "✓ Streamlit já instalado" -ForegroundColor Green
}

Write-Host ""
Write-Host "🚀 Iniciando interface web..." -ForegroundColor Cyan
Write-Host ""
Write-Host "A interface abrirá automaticamente no navegador." -ForegroundColor Gray
Write-Host "URL: http://localhost:8501" -ForegroundColor Gray
Write-Host ""
Write-Host "Pressione Ctrl+C para parar o servidor" -ForegroundColor Yellow
Write-Host ""

# Iniciar Streamlit
& ".venv\Scripts\streamlit.exe" run app.py
