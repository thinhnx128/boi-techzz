@echo off
chcp 65001 >nul
title Push AI Bounty Solutions to https://github.com/thinhnx128
cd /d "%~dp0"
echo =====================================================================
echo   🐙 ĐẨY BỘ 3 GIẢI PHÁP AI BOUNTY LÊN GITHUB: @thinhnx128
echo   1. Hệ thống sẽ mở trang tạo Repo mới trên GitHub của anh (đặt tên: boi-tech-ai-bounties)
echo   2. Sau khi anh bấm "Create repository", quay lại cửa sổ này bấm phím bất kỳ để Git tự động Push!
echo =====================================================================
start "" "https://github.com/new?name=boi-tech-ai-bounties&description=AI+Cloud+MCP+Connectors,+RAG+Security+Patches+and+Concurrency+Solutions"
pause
git remote remove origin 2>nul
git remote add origin https://github.com/thinhnx128/boi-tech-ai-bounties.git
git branch -M main
git push -u origin main
echo.
echo ✅ Đã đẩy toàn bộ code lên https://github.com/thinhnx128/boi-tech-ai-bounties !
pause
