@echo off
echo Starting YeniBot FreqAI (Headless Mode)...
.\.venv\Scripts\freqtrade trade --config user_data/config.json --strategy XGBoostStrategy
pause
