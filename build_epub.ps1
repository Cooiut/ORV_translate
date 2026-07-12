$ErrorActionPreference = "Stop"

Write-Host "Setting console encoding to UTF-8..." -ForegroundColor Cyan
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

# Ensure Java is available for EPUBCheck (Step 5)
$env:PATH += ";C:\Program Files\Java\jre1.8.0_491\bin"

function Invoke-Step {
    param(
        [int]$StepNumber,
        [string]$StepName,
        [string]$ScriptPath
    )
    Write-Host "`n===============================================" -ForegroundColor Cyan
    Write-Host "           STEP ${StepNumber}: $StepName" -ForegroundColor Yellow
    Write-Host "===============================================" -ForegroundColor Cyan

    & .\venv\Scripts\python $ScriptPath
    if ($LASTEXITCODE -ne 0) {
        Write-Host "`n>>> STEP $StepNumber FAILED with exit code $LASTEXITCODE <<<" -ForegroundColor Red
        Write-Host ""
        Pause
        exit $LASTEXITCODE
    }
}

Invoke-Step 1 "Font Subsetting & Compression" "script\subset_fonts.py"
Invoke-Step 2 "Packaging EPUB"                "script\pack_epub.py"
Invoke-Step 3 "Font Verification"             "script\verify_fonts.py"
Invoke-Step 4 "XML and EPUB Validation"       "script\validator.py"
Invoke-Step 5 "EPUBCheck Validation"          "script\epubcheck_validate.py"

Write-Host "`n>>> All steps completed successfully! Your final EPUB is in the books/ folder. <<<" -ForegroundColor Green

# Wait for user keypress before closing
Write-Host ""
Pause
