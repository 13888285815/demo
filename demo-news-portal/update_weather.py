#!/usr/bin/env python3
import json
import requests
from datetime import datetime

now_str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")

print("获取天气数据...")
try:
    resp = requests.get("https://wttr.in/Beijing?format=j1", timeout=10)
    if resp.status_code == 200:
        data = resp.json()
        current = data['current_condition'][0]
        
        weather = {
            "city": "北京",
            "date": now_str[:10],
            "temp": current['temp_C'] + "°C",
            "feelsLike": current['FeelsLikeC'] + "°C",
            "humidity": current['humidity'] + "%",
            "weather": current['weatherDesc'][0]['value'].strip(),
            "wind": current['winddir16Point'] + " " + current['windspeedKmph'] + "km/h",
            "visibility": current['visibility'] + "km",
            "pressure": current['pressure'] + "hPa"
        }
        
        with open('weather.json', 'w', encoding='utf-8') as f:
            json.dump(weather, f, ensure_ascii=False, indent=2)
        
        print(f"✓ 天气数据已更新: {weather['weather']}, {weather['temp']}")
    else:
        print(f"✗ 获取失败: HTTP {resp.status_code}")
except Exception as e:
    print(f"✗ 错误: {e}")
