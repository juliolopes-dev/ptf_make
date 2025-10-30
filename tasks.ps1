# Tasks PowerShell para ptf_maker

param(
    [Parameter(Mandatory=$false)]
    [ValidateSet('setup', 'run', 'clean', 'help')]
    [string]$Task = 'help'
)

function Setup {
    Write-Host "=== Setup do ambiente ===" -ForegroundColor Cyan
    
    # Verificar FFmpeg
    try {
        ffmpeg -version | Out-Null
        Write-Host "✓ FFmpeg encontrado" -ForegroundColor Green
    } catch {
        Write-Host "✗ FFmpeg não encontrado. Instale com:" -ForegroundColor Red
        Write-Host "  winget install ffmpeg" -ForegroundColor Yellow
        return
    }
    
    # Criar ambiente virtual
    if (Test-Path ".venv") {
        Write-Host "✓ Ambiente virtual já existe" -ForegroundColor Green
    } else {
        Write-Host "Criando ambiente virtual..." -ForegroundColor Yellow
        python -m venv .venv
        Write-Host "✓ Ambiente virtual criado" -ForegroundColor Green
    }
    
    # Ativar e instalar dependências
    Write-Host "Instalando dependências..." -ForegroundColor Yellow
    & ".venv\Scripts\pip.exe" install -r requirements.txt
    Write-Host "✓ Dependências instaladas" -ForegroundColor Green
    
    # Criar diretórios
    New-Item -ItemType Directory -Force -Path "assets" | Out-Null
    New-Item -ItemType Directory -Force -Path "out" | Out-Null
    Write-Host "✓ Diretórios criados" -ForegroundColor Green
    
    # Verificar .env
    if (Test-Path ".env") {
        Write-Host "✓ Arquivo .env encontrado" -ForegroundColor Green
    } else {
        Write-Host "! Arquivo .env não encontrado. Copie .env.example para .env" -ForegroundColor Yellow
    }
    
    Write-Host "`n=== Setup concluído! ===" -ForegroundColor Cyan
    Write-Host "Execute: .\tasks.ps1 run" -ForegroundColor Yellow
}

function Run {
    Write-Host "=== Executando exemplo ===" -ForegroundColor Cyan
    
    if (-not (Test-Path ".venv\Scripts\python.exe")) {
        Write-Host "✗ Ambiente virtual não encontrado. Execute: .\tasks.ps1 setup" -ForegroundColor Red
        return
    }
    
    & ".venv\Scripts\python.exe" -m ptf_maker --script-file exemplo.txt --topic "finance money savings" --images 4
}

function Clean {
    Write-Host "=== Limpando arquivos gerados ===" -ForegroundColor Cyan
    
    if (Test-Path "out") {
        Remove-Item -Recurse -Force "out\*"
        Write-Host "✓ Pasta out/ limpa" -ForegroundColor Green
    }
    
    if (Test-Path "assets\pexels_*.jpg") {
        Remove-Item -Force "assets\pexels_*.jpg"
        Write-Host "✓ Imagens do Pexels removidas" -ForegroundColor Green
    }
    
    Write-Host "✓ Limpeza concluída" -ForegroundColor Green
}

function Help {
    Write-Host @"
=== ptf_maker - Tasks ===

Uso: .\tasks.ps1 <comando>

Comandos:
  setup   - Configura ambiente virtual e instala dependências
  run     - Executa exemplo com exemplo.txt
  clean   - Remove arquivos gerados (out/ e imagens baixadas)
  help    - Mostra esta mensagem

Exemplos:
  .\tasks.ps1 setup
  .\tasks.ps1 run
  .\tasks.ps1 clean

"@ -ForegroundColor Cyan
}

# Executar task
switch ($Task) {
    'setup' { Setup }
    'run'   { Run }
    'clean' { Clean }
    'help'  { Help }
}
