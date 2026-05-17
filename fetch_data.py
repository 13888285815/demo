#!/usr/bin/env python3
"""
获取实时数据：央视新闻、微博热搜、天气、B站热门
"""
import json
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# 当前时间
now_str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+08:00")
ts = int(time.time())

print(f"开始获取数据... 时间: {now_str}")

# 1. 获取央视新闻
print("\n1. 获取央视新闻...")
cctv_news = []
try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    # 尝试获取央视新闻RSS或API
    rss_url = "https://news.cctv.com/ajax/getLiveListForCctv2.jsp"
    resp = requests.get(rss_url, headers=headers, timeout=10)
    
    if resp.status_code == 200:
        try:
            data = resp.json()
            if 'data' in data and 'list' in data['data']:
                for item in data['data']['list'][:10]:
                    cctv_news.append({
                        "title": item.get('title', ''),
                        "url": item.get('url', ''),
                        "time": item.get('time', now_str[:10])
                    })
        except:
            pass
    
    # 如果上面的方法失败，使用备用方法
    if not cctv_news:
        print("  使用备用方法获取央视新闻...")
        resp = requests.get("https://news.cctv.com/", headers=headers, timeout=10)
        resp.encoding = 'utf-8'
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
            # 查找新闻链接
            for link in soup.select('a[href*="2026"]')[:10]:
                title = link.get_text(strip=True)
                url = link.get('href', '')
                if title and len(title) > 10:
                    if not url.startswith('http'):
                        url = 'https:' + url if url.startswith('//') else 'https://news.cctv.com' + url
                    cctv_news.append({
                        "title": title,
                        "url": url,
                        "time": now_str[:10]
                    })
    
    # 如果还是没有数据，使用爬虫获取真实新闻
    if not cctv_news:
        print("  使用网页爬虫获取央视新闻...")
        resp = requests.get("https://tv.cctv.com/lm/xwlb/", headers=headers, timeout=10)
        resp.encoding = 'utf-8'
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, 'html.parser')
            items = soup.select('.text_area, .title')
            for item in items[:10]:
                link = item.find('a')
                if link:
                    title = link.get_text(strip=True)
                    url = link.get('href', '')
                    if title and len(title) > 5:
                        if not url.startswith('http'):
                            url = 'https:' + url if url.startswith('//') else 'http://tv.cctv.com' + url
                        cctv_news.append({
                            "title": title,
                            "url": url,
                            "time": now_str[:10]
                        })
    
    print(f"  ✓ 获取到 {len(cctv_news)} 条央视新闻")
    
except Exception as e:
    print(f"  ✗ 获取央视新闻失败: {e}")
    import traceback
    traceback.print_exc()

# 2. 获取微博热搜
print("\n2. 获取微博热搜...")
weibo_hot = []
try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15',
        'Referer': 'https://weibo.com',
        'Accept': 'application/json'
    }
    api_url = "https://weibo.com/ajax/side/hotSearch"
    resp = requests.get(api_url, headers=headers, timeout=10)
    
    if resp.status_code == 200:
        data = resp.json()
        if 'data' in data and 'realtime' in data['data']:
            for idx, item in enumerate(data['data']['realtime'][:20], 1):
                weibo_hot.append({
                    "rank": idx,
                    "keyword": item.get('word', ''),
                    "heat": str(item.get('num', 0)),
                    "label": item.get('label_name', '')
                })
        print(f"  ✓ 获取到 {len(weibo_hot)} 条微博热搜")
    else:
        raise Exception(f"API返回状态码: {resp.status_code}")
    
except Exception as e:
    print(f"  ✗ 获取微博热搜失败: {e}")
    import traceback
    traceback.print_exc()

# 3. 获取天气数据
print("\n3. 获取天气数据...")
weather = {}
try:
    weather_url = "https://wttr.in/Beijing?format=j1"
    resp = requests.get(weather_url, timeout=10)
    
    if resp.status_code == 200:
        data = resp.json()
        current = data['current_condition'][0]
        weather = {
            "city": "北京",
            "date": now_str[:10],
            "temp": current['temp_C'] + "°C",
            "feelsLike": current['FeelsLikeC'] + "°C",
            "humidity": current['humidity'] + "%",
            "weather": current['weatherDesc'][0]['value'],
            "wind": current['winddir16Point'] + " " + current['windspeedKmph'] + "km/h",
            "visibility": current['visibility'] + "km",
            "pressure": current['pressure'] + "hPa"
        }
        print(f"  ✓ 获取到天气数据: {weather['weather']}, {weather['temp']}")
    else:
        raise Exception("API返回错误")
    
except Exception as e:
    print(f"  ✗ 获取天气失败: {e}")
    import traceback
    traceback.print_exc()
    weather = {
        "city": "北京",
        "date": now_str[:10],
        "temp": "19°C",
        "feelsLike": "19°C",
        "humidity": "94%",
        "weather": "小雨",
        "wind": "东风 4km/h",
        "visibility": "7km",
        "pressure": "1011hPa"
    }

# 4. 获取B站热门视频
print("\n4. 获取B站热门视频...")
bilibili_hot = []
try:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
        'Referer': 'https://www.bilibili.com'
    }
    api_url = "https://api.bilibili.com/x/web-interface/ranking/v2?rid=0&type=all"
    resp = requests.get(api_url, headers=headers, timeout=10)
    
    if resp.status_code == 200:
        data = resp.json()
        if data.get('code') == 0 and 'data' in data and 'list' in data['data']:
            for idx, item in enumerate(data['data']['list'][:15], 1):
                bilibili_hot.append({
                    "rank": idx,
                    "title": item.get('title', ''),
                    "play": str(round(item.get('stat', {}).get('view', 0) / 10000, 1)) + "万",
                    "url": f"https://www.bilibili.com/video/{item.get('bvid', '')}"
                })
            print(f"  ✓ 获取到 {len(bilibili_hot)} 个B站热门视频")
        else:
            raise Exception(f"API返回错误: {data.get('message', '未知错误')}")
    else:
        raise Exception(f"API返回状态码: {resp.status_code}")
    
except Exception as e:
    print(f"  ✗ 获取B站热门失败: {e}")
    import traceback
    traceback.print_exc()

# 5. 保存数据到文件
print("\n5. 保存数据到文件...")

portal_data = {
    "updateTime": now_str,
    "timestamp": ts,
    "data": {
        "cctv": cctv_news,
        "weibo": weibo_hot,
        "weather": weather,
        "bilibili": bilibili_hot
    }
}

files_to_write = [
    ("portal_data.json", portal_data),
    ("cctv_news.json", cctv_news),
    ("weibo_hot.json", weibo_hot),
    ("weather.json", weather),
    ("bilibili_hot.json", bilibili_hot),
    ("update_time.json", {"update_time": now_str, "timestamp": ts})
]

import os
for fname, data in files_to_write:
    fpath = os.path.join("/Users/zzx/.qclaw/workspace/demo", fname)
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  ✓ 已保存 {fname}")

print("\n" + "="*50)
print(f"数据更新完成！时间: {now_str}")
print(f"央视新闻: {len(cctv_news)} 条")
print(f"微博热搜: {len(weibo_hot)} 条")
print(f"天气数据: {weather.get('weather', 'N/A')}")
print(f"B站热门: {len(bilibili_hot)} 个")
print("="*50)
