# Script de teste dos recursos profissionais
# Execute: .\test_profissional.ps1

Write-Host "=== Testando Recursos Profissionais ===" -ForegroundColor Cyan

# Criar diretórios
New-Item -ItemType Directory -Force -Path "exemplos" | Out-Null

# Teste 1: Template Finance
Write-Host "`n[1/3] Testando template FINANCE..." -ForegroundColor Yellow
.venv\Scripts\python -m ptf_maker `
  --script-file exemplos\finance_pro.txt `
  --template finance `
  --images 4

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Vídeo finance gerado!" -ForegroundColor Green
    Rename-Item "out\video.mp4" "out\video_finance.mp4" -Force
} else {
    Write-Host "✗ Erro ao gerar vídeo finance" -ForegroundColor Red
}

# Teste 2: Template Motivation com animação zoom
Write-Host "`n[2/3] Testando template MOTIVATION com animação ZOOM..." -ForegroundColor Yellow
.venv\Scripts\python -m ptf_maker `
  --script-file exemplos\motivation_pro.txt `
  --template motivation `
  --animation zoom `
  --images 5

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Vídeo motivation gerado!" -ForegroundColor Green
    Rename-Item "out\video.mp4" "out\video_motivation.mp4" -Force
} else {
    Write-Host "✗ Erro ao gerar vídeo motivation" -ForegroundColor Red
}

# Teste 3: Template Tech
Write-Host "`n[3/3] Testando template TECH..." -ForegroundColor Yellow
.venv\Scripts\python -m ptf_maker `
  --script-file exemplos\tech_pro.txt `
  --template tech `
  --animation slide `
  --images 4

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Vídeo tech gerado!" -ForegroundColor Green
    Rename-Item "out\video.mp4" "out\video_tech.mp4" -Force
} else {
    Write-Host "✗ Erro ao gerar vídeo tech" -ForegroundColor Red
}

Write-Host "`n=== Testes Concluídos ===" -ForegroundColor Cyan
Write-Host "Vídeos gerados em out/:" -ForegroundColor White
Get-ChildItem "out\video_*.mp4" | ForEach-Object {
    $size = [math]::Round($_.Length / 1MB, 2)
    Write-Host "  - $($_.Name) ($size MB)" -ForegroundColor Gray
}

Write-Host "`nPara testar com música de fundo:" -ForegroundColor Yellow
Write-Host "  1. Baixe uma música MP3 em assets/music.mp3" -ForegroundColor Gray
Write-Host "  2. Execute:" -ForegroundColor Gray
Write-Host "     .venv\Scripts\python -m ptf_maker --script-file exemplos\finance_pro.txt --template finance --background-music assets\music.mp3" -ForegroundColor DarkGray
