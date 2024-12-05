from flask import Flask, jsonify
from flask_cors import CORS
import csv
from scheduler import start_scheduler
from modules.weather import capture_weather

app = Flask(__name__)
CORS(app)

# 서버 시작시 스케줄러 시작
start_scheduler()

@app.route('/')
def home():
    return jsonify({"status": "Server is running"})

@app.route('/news')
def news():
    try:
        news_items = []
        with open('latest_news.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                news_items.append({
                    'section': row['Section'],
                    'number': row['Number'],
                    'title': row['Title'],
                    'link': row['Link'],
                    'timestamp': row['Timestamp']
                })
        return jsonify(news_items)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/trending-csv')
def trending():
    try:
        trends = []
        with open('latest_trends.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                trends.append(row['Keyword'])
        return jsonify(trends)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/weather')
def weather():
    try:
        screenshot_path = capture_weather()
        return jsonify({"screenshot": screenshot_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(port=5001)