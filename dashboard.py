from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

# Freqtrade API ayarları (config.json ile uyumlu olmalı)
FREQTRADE_API_URL = "http://127.0.0.1:8080/api/v1"
API_USER = "admin"
API_PASS = "admin_password"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/status')
def get_status():
    try:
        r = requests.get(f"{FREQTRADE_API_URL}/status", auth=(API_USER, API_PASS))
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/profit')
def get_profit():
    try:
        r = requests.get(f"{FREQTRADE_API_URL}/profit", auth=(API_USER, API_PASS))
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/performance')
def get_performance():
    try:
        r = requests.get(f"{FREQTRADE_API_URL}/performance", auth=(API_USER, API_PASS))
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # templates klasörünü kontrol et
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    app.run(debug=True, port=5000)
