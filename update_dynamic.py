import json, time, os

# Get current time in correct format
now_str = time.strftime("%Y-%m-%dT%H:%M:%S+08:00")
ts = int(time.time())

# Read data from JSON files
def read_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return None

# Load all data sources
cctv_data = read_json('cctv_news.json')
weibo_data = read_json('weibo_hot.json')
weather_data = read_json('weather.json')
bilibili_data = read_json('bilibili_hot.json')

# Transform data to match expected format
def transform_cctv(data):
    if not data:
        return []
    # Already in correct format
    return data if isinstance(data, list) else []

def transform_weibo(data):
    if not data:
        return []
    # Check if data is already in expected format or needs transformation
    if isinstance(data, list) and len(data) > 0:
        if 'keyword' in data[0]:
            return data  # Already in correct format
        elif 'word' in data[0]:
            # Transform from API format
            return [{'rank': i+1, 'keyword': x.get('word', ''), 'heat': str(x.get('raw_hot', 0)), 'label': '热' if x.get('flag_desc') else ''} for i, x in enumerate(data[:20])]
    return []

def transform_weather(data):
    if not data:
        return {}
    # Convert from wttr.in format to expected format
    if 'current_condition' in str(data):
        return {
            'city': data.get('location', '上海'),
            'date': time.strftime('%Y-%m-%d'),
            'temp': f"{data['current_condition'][0]['temp_C']}°C",
            'feelsLike': f"{data['current_condition'][0].get('FeelsLikeC', data['current_condition'][0]['temp_C'])}°C",
            'humidity': f"{data['current_condition'][0]['humidity']}%",
            'weather': data['current_condition'][0]['weatherDesc'][0]['value'],
            'wind': f"{data['current_condition'][0]['winddir16Point']} {data['current_condition'][0]['windspeedKmph']}km/h",
            'visibility': f"{data['current_condition'][0].get('visibility', 10)}km",
            'pressure': f"{data['current_condition'][0].get('pressure', 1014)}hPa",
            'sunrise': data['weather'][0].get('astronomy', [{}])[0].get('sunrise', '06:00'),
            'sunset': data['weather'][0].get('astronomy', [{}])[0].get('sunset', '18:00')
        }
    return data  # Already in correct format

def transform_bilibili(data):
    if not data:
        return []
    if 'rankings' in data:
        return [{'rank': x['rank'], 'title': x['title'], 'play': str(x['play']), 'url': f"https://www.bilibili.com/video/av{x.get('bvid', '')}"} for x in data['rankings'][:15]]
    elif isinstance(data, list):
        return data  # Already in correct format
    return []

# Transform all data
cctv_news = transform_cctv(cctv_data) if isinstance(cctv_data, list) else []
weibo_hot = transform_weibo(weibo_data) if weibo_data else []
weather = transform_weather(weather_data) if weather_data else {}
bilibili_hot = transform_bilibili(bilibili_data) if bilibili_data else []

# Build portal data
portal_data = {
    'updateTime': now_str,
    'data': {
        'cctv': cctv_news,
        'weibo': weibo_hot,
        'weather': weather,
        'bilibili': bilibili_hot
    }
}

# Write all files
files_to_write = [
    ('portal_data.json', portal_data),
    ('cctv_news.json', cctv_news),
    ('weibo_hot.json', weibo_hot),
    ('weather.json', weather),
    ('bilibili_hot.json', bilibili_hot),
    ('update_time.json', {'update_time': now_str, 'timestamp': ts})
]

for fname, data in files_to_write:
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Written: {fname}")

print(f"\nUpdate completed at {now_str}")
print(f"Data summary:")
print(f"  - CCTV news: {len(cctv_news)} items")
print(f"  - Weibo hot: {len(weibo_hot)} items")
print(f"  - Weather: {'OK' if weather else 'Failed'}")
print(f"  - Bilibili: {len(bilibili_hot)} items")
