@echo off
chcp 65001 > nul
cd /d "%~dp0"
echo AI 가위바위보 게임을 실행합니다...
echo 이 창을 닫으면 게임이 종료됩니다.
rem 서버가 뜬 뒤에 브라우저가 열리도록 2초 기다렸다가 엽니다
start "" powershell -NoProfile -WindowStyle Hidden -Command "Start-Sleep -Seconds 2; Start-Process 'http://localhost:8765/index.html'"
python serve.py
