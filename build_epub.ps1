$ErrorActionPreference = "Stop"

Write-Host "Setting console encoding to UTF-8..." -ForegroundColor Cyan
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Host "`n===============================================" -ForegroundColor Cyan
Write-Host "      STEP 1: Font Subsetting & Compression      " -ForegroundColor Yellow
Write-Host "===============================================" -ForegroundColor Cyan
& .\venv\Scripts\python script\subset_fonts.py

Write-Host "`n===============================================" -ForegroundColor Cyan
Write-Host "           STEP 2: Packaging EPUB                " -ForegroundColor Yellow
Write-Host "===============================================" -ForegroundColor Cyan
& .\venv\Scripts\python script\pack_epub.py

Write-Host "`n===============================================" -ForegroundColor Cyan
Write-Host "           STEP 3: Verification                  " -ForegroundColor Yellow
Write-Host "===============================================" -ForegroundColor Cyan
& .\venv\Scripts\python script\verify_fonts.py

Write-Host "`n===============================================" -ForegroundColor Cyan
Write-Host "           STEP 4: XML and EPUB Validation       " -ForegroundColor Yellow
Write-Host "===============================================" -ForegroundColor Cyan
& .\venv\Scripts\python script\validator.py

Write-Host "`n===============================================" -ForegroundColor Cyan
Write-Host "           STEP 5: EPUBCheck Validation          " -ForegroundColor Yellow
Write-Host "===============================================" -ForegroundColor Cyan
$env:PATH += ";C:\Program Files\Java\jre1.8.0_491\bin"
& .\venv\Scripts\epubcheck books\全知读者视角-外传.epub 2>&1

Write-Host "`n>>> All steps completed successfully! Your final EPUB is in the books/ folder. <<<" -ForegroundColor Green

# Wait for user keypress before closing
Write-Host ""
Pause
