import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz).strftime("%Y-%m-%dT%H:%M:%S+08:00")

cctv_data = {"update_time": now, "source": "https://news.cctv.com/", "news": [
    {"title": "\u5df4\u62c9\u573e\u603b\u7edf\u7a82\u53f0 \u5916\u4ea4\u90e8\uff1a\u575a\u51b3\u53cd\u5bf9 \u5f3a\u70c8\u8e23\u8d23\u5df4\u65b9\u6709\u5173\u884c\u5f84", "url": "https://tv.cctv.com/2026/05/12/VIDEhqEIplmfWMLxE21yVRyx260512.shtml", "date": "2026-05-12", "summary": "\u5df4\u62c9\u573e\u603b\u7edf\u7a82\u8bbf\u53f0\u6e7e\u5730\u533a\uff0c\u5916\u4ea4\u90e8\u8868\u793a\u575a\u51b3\u53cd\u5bf9\u5e76\u5f3a\u70c8\u8e23\u8d23\u5df4\u65b9\u6709\u5173\u884c\u5f84\u3002"},
    {"title": "\u4e2d\u56fd\u4eba\u6c11\u94f6\u884c\uff1a\u9002\u5ea6\u5bbd\u677e\u7684\u8d27\u5e01\u653f\u7b56\u6548\u679c\u6301\u7eed\u663e\u73b0", "url": "https://tv.cctv.com/2026/05/12/VIDEATozrKi2vWSjQL6RPcrR260512.shtml", "date": "2026-05-12", "summary": "\u4e2d\u56fd\u4eba\u6c11\u94f6\u884c\u8868\u793a\u9002\u5ea6\u5bbd\u677e\u7684\u8d27\u5e01\u653f\u7b56\u6548\u679c\u6301\u7eed\u663e\u73b0\uff0c\u5404\u9879\u91d1\u878d\u6570\u636e\u7a33\u4e2d\u5411\u597d\u3002"},
    {"title": "\u6c49\u5766\u75c5\u6bd2\u662f\u4ec0\u4e48\uff1f\u4f55\u4e3a\u5b89\u7b2c\u65af\u75c5\u6bd2\uff1f", "url": "https://tv.cctv.com/2026/05/12/VIDEPe9j5qh1j8yIC8MPCvWr260512.shtml", "date": "2026-05-12", "summary": "\u592e\u89c6\u79d1\u666e\u6c49\u5766\u75c5\u6bd2\u53ca\u5b89\u7b2c\u65af\u75c5\u6bd2\u76f8\u5173\u77e5\u8bc6\uff0c\u4ecb\u7ecd\u4f20\u64ad\u9014\u5f84\u4e0e\u9884\u9632\u63aa\u65bd\u3002"}
]}
weibo_data = {"update_time": now, "source": "tophub.today \u5fae\u535a\u70ed\u641c", "hotList": [
    {"rank": 1, "keyword": "\u5b87\u6811\u673a\u7532 \u6c11\u7528\u4ea4\u901a\u5de5\u5177", "heat": 1110000, "tag": "\u70ed"},
    {"rank": 2, "keyword": "\u71c3\u6cb9\u9644\u52a0\u8d39 \u6da8\u4ef7", "heat": 1100000, "tag": "\u65b0"},
    {"rank": 3, "keyword": "\u79d1\u5b66\u907f\u9669\u81ea\u6551\u6307\u5357", "heat": 980000, "tag": ""},
    {"rank": 4, "keyword": "\u6df1\u5733\u592b\u5987\u5c6f\u5b58\u50a8\u82af\u72475\u4e2a\u6708\u72c2\u6da8320\u4ebf", "heat": 950000, "tag": ""},
    {"rank": 5, "keyword": "\u5357\u4eac\u5ba1\u8ba1\u5927\u5b66\u901a\u62a5\u7537\u751f\u5c1a\u62cd", "heat": 900000, "tag": "\u70ed"},
    {"rank": 6, "keyword": "\u5efa\u8bae\u4e0d\u8981\u5728\u5c0f\u73af\u5883\u4e2d\u5f85\u592a\u4e45", "heat": 840000, "tag": ""},
    {"rank": 7, "keyword": "\u516c\u638c\u6986\u69d3", "heat": 490000, "tag": "\u65b0"},
    {"rank": 8, "keyword": "\u539f\u6765\u5065\u5eb7\u7684\u4eba\u8eab\u4f53\u662f\u9759\u97f3\u7684", "heat": 360000, "tag": ""},
    {"rank": 9, "keyword": "\u4f4e\u667a\u5546\u72af\u7f6a", "heat": 360000, "tag": ""},
    {"rank": 10, "keyword": "\u4e2d\u65b9\u5f3a\u70c8\u8e23\u8d23\u5df4\u65b9\u6709\u5173\u884c\u5f84", "heat": 360000, "tag": "\u70ed"},
    {"rank": 11, "keyword": "\u8003\u8bd5\u5750\u4e25\u6d69\u7ffb\u524d\u9762\u7684\u540c\u5b66\u53d1\u58f0", "heat": 360000, "tag": ""},
    {"rank": 12, "keyword": "\u6c6a\u6c5d\u6709\u591a\u559c\u5403\u69d0\u6930", "heat": 360000, "tag": ""},
    {"rank": 13, "keyword": "\u5973\u5b69\u9000\u793c\u670d\u4e8b\u4ef6\u5408\u5531\u56e2\u79f0\u53d7\u7259\u8fde", "heat": 360000, "tag": ""},
    {"rank": 14, "keyword": "\u767d\u9e3f\u6f14\u5531\u4f1a\u8fc7\u5ba1", "heat": 360000, "tag": ""},
    {"rank": 15, "keyword": "hybe\u62d2\u7edd\u5bab\u8107\u55cc\u826f\u53c2\u4e0e\u521b\u4f5c", "heat": 360000, "tag": ""},
    {"rank": 16, "keyword": "\u72fc\u961f\u5bf9\u6218AG", "heat": 360000, "tag": ""},
    {"rank": 17, "keyword": "\u738b\u4fca\u51ef\u4e2d\u9910\u5385\u62db\u5546\u80fd\u529b", "heat": 360000, "tag": "\u7efc\u827a"},
    {"rank": 18, "keyword": "\u6296\u97f3\u8bc4\u8bba\u533a \u9648\u8d6b\u773c\u4e2d\u542b\u6cea", "heat": 360000, "tag": ""},
    {"rank": 19, "keyword": "\u60ca\u73b0\u6d3b\u86c7\u706b\u9505\u5e97\u8001\u677f\u81f4\u6b49", "heat": 360000, "tag": ""},
    {"rank": 20, "keyword": "\u5370\u5ea6\u6e38\u5ba2\u5728\u83ab\u65af\u79d1\u55b3\u6cc9\u6c34\u6c60\u6d17\u8863\u670d", "heat": 350000, "tag": ""}
]}
bilibili_data = {"update_time": now, "source": "tophub.today \u54ed\u5229\u54ed\u5229\u5168\u7ad9\u65e5\u699c", "hotList": [
    {"rank": 1, "title": "\u300a\u9668\u4e0b\u4f55\u6545\u8c0b\u53cd\u300b", "url": "https://www.bilibili.com/video/av116546085061974/", "heat": 8107000},
    {"rank": 2, "title": "\u7b2c\u4e00\u5929\u6765\u5317\u4eac\u5c31\u9047\u5230\u4e86\u597d\u591a\u6e29\u6696\u7684\u4eba...", "url": "https://www.bilibili.com/video/av116535750301165/", "heat": 7676000},
    {"rank": 3, "title": "\u300a\u65e0\u80fd\u7684\u90c1\u54e5\u300b", "url": "https://www.bilibili.com/video/av116543065228571/", "heat": 5335000},
    {"rank": 4, "title": "\u661f\u6cb3\u8272\u60ac\u6d6e\u5b57", "url": "https://www.bilibili.com/video/av116536840817474/", "heat": 5804000},
    {"rank": 5, "title": "\u8fd9\u662f\u771f\u62fc\u8c46\uff01\u4e5f\u771f\u634f\u634f\uff01\u8fd8\u662f\u771f\u82a6\u4e50\uff01", "url": "https://www.bilibili.com/video/av116544004822670/", "heat": 5033000},
    {"rank": 6, "title": "\u8bb8 \u4ed9 \u4e70 \u74dc", "url": "https://www.bilibili.com/video/av116540112372371/", "heat": 3440000},
    {"rank": 7, "title": "\u8bed\u6587\u8001\u5e08\u6539\u5230\u7684\u79bb\u8c31\u7b54\u6848\u4e2d\u5927\u5168\u96c6", "url": "https://www.bilibili.com/video/av116532361298949/", "heat": 3645000},
    {"rank": 8, "title": "\u4eca\u6211\u592b\u5987\u4e24\u4eba\uff0c\u4eca\u7acb\u5492\u4e8e\u6b64\u5802", "url": "https://www.bilibili.com/video/av116538334124846/", "heat": 3633000},
    {"rank": 9, "title": "\u52a8\u6001\u89f6\u9891\uff5c\u6211\u548c\u5218\u8c26\u6bd4\u4e86\u4e00\u573a...", "url": "https://www.bilibili.com/video/av116545682480579/", "heat": 3765000},
    {"rank": 10, "title": "\u4e00\u79d2\u4e0d\u7528\u526a", "url": "https://www.bilibili.com/video/av116542410989068/", "heat": 3302000},
    {"rank": 11, "title": "\u6211\u957f\u8fd9\u6837\uff0c\u4f46\u662f\u6211\u7684\u753b\u2026", "url": "https://www.bilibili.com/video/av116543484596659/", "heat": 3622000},
    {"rank": 12, "title": "3\u53f0\u9ad8\u901f\u673aVS\u5218\u8c26\u624b\u901f\uff01\u8c01\u66f4\u80dc\u4e00\u7b79\uff1f", "url": "https://www.bilibili.com/video/av116554742109232/", "heat": 3193000},
    {"rank": 13, "title": "\u300a\u5d29\u574f\uff1a\u661f\u7a79\u94c1\u9053\u300b\u7edb\u82f1\u89d2\u8272PV\u2014\u2014\u300c\u5979\u7684\u65e5\u5e38\u300d", "url": "https://www.bilibili.com/video/av116553567699238/", "heat": 2545000},
    {"rank": 14, "title": "\u5343\u547c\u4e07\u5524\uff01\u300aENEMY\u300b\u65e0\u7801\u4e94K\u91cd\u5236\u5b8c\u6574\u7248\u4e0a\u7ebf\u4e86\uff01", "url": "https://www.bilibili.com/video/av116533183386934/", "heat": 2546000},
    {"rank": 15, "title": "\u624b\u6321\u8f7d\u4eba\u98de\u5251\uff01\u5fa1\u5251\u98de\u884c\uff01", "url": "https://www.bilibili.com/video/av116538233328961/", "heat": 2675000},
    {"rank": 16, "title": "\u300a\u4e24\u6746\u5927\u70df\u67aa\u300b", "url": "https://www.bilibili.com/video/av116548568156747/", "heat": 2759000},
    {"rank": 17, "title": "\u628a\u534a\u65a4\u6d53\u6c64\u704c\u8fdb\u9c7c\u8099\uff0c\u5207\u5f00\u7684\u77ac\u95f4\uff0c\u503c\u4e86\uff01", "url": "https://www.bilibili.com/video/av116549708940644/", "heat": 2475000},
    {"rank": 18, "title": "\u767e\u4e07\u82f1\u938a\u4e70\u74dc\uff08\u56fd\u8bed\u7248\uff09", "url": "https://www.bilibili.com/video/av116541135784923/", "heat": 2002000},
    {"rank": 19, "title": "\u6c38\u8fdc\u6000\u5ff5\u6211\u4eb2\u7231\u7684\u5434\u5988\uff01", "url": "https://www.bilibili.com/video/av116544524850828/", "heat": 1756000},
    {"rank": 20, "title": "\u4e2d\u7f8e\u4f1a\u9762\u524d\uff0c\u53cc\u65b9\u5982\u4f55\u51fa\u62db\uff1f", "url": "https://www.bilibili.com/video/av116556000401085/", "heat": 1617000}
]}
weather_data = {"update_time": now, "source": "wttr.in", "location": "Kunming", "current": {"tempC": 19, "feelsLikeC": 19, "condition": "Partly Cloudy", "humidity": "60%", "windspeedKmph": 13, "windDirection": "SW", "pressure": "1014 mb", "visibility": "10 km", "uvIndex": "0", "cloudcover": "50%", "observation_time": "2026-05-12 20:20"}, "astronomy": {"sunrise": "05:27", "sunset": "18:45", "moonrise": "02:01", "moonset": "14:06", "moon_phase": "Waning Crescent"}, "forecast": [{"date": "05-12", "week": "Tue", "weather": "Light Rain", "high": "19", "low": "14"}, {"date": "05-13", "week": "Wed", "weather": "Partly Cloudy", "high": "24", "low": "14"}], "alert": "Tonight Kunming partly cloudy, 14-19C, comfortable."}
portal_data = {"updateTime": now, "dataSource": {"cctvNews": {"source": "CCTV", "fetchTime": now, "topStories": [{"title": "巴拉圭总统窜台 外交部：坚决反对 强烈谴责巴方有关行径", "url": "https://tv.cctv.com/2026/05/12/VIDEhqEIplmfWMLxE21yVRyx260512.shtml"}, {"title": "中国人民银行：适度宽松的货币政策效果持续显现", "url": "https://tv.cctv.com/2026/05/12/VIDEATozrKi2vWSjQL6RPcrR260512.shtml"}, {"title": "汉坦病毒是什么？何为安第斯病毒？", "url": "https://tv.cctv.com/2026/05/12/VIDEPe9j5qh1j8yIC8MPCvWr260512.shtml"}]}, "weiboHot": {"source": "Weibo Hot", "fetchTime": now, "hotList": weibo_data["hotList"][:15]}, "weather": {"source": "Weather", "fetchTime": now, "location": "Kunming", "current": {"date": "2026-05-12", "dayOfWeek": "Tue", "weather": "Partly Cloudy", "tempHigh": "19", "tempLow": "14", "wind": "SW", "windLevel": "3", "humidity": "60", "sunrise": "05:27", "sunset": "18:45"}, "forecast": [{"date": "2026-05-13", "day": "Wed", "weather": "Partly Cloudy", "high": "24", "low": "14", "wind": "SW"}, {"date": "2026-05-14", "day": "Thu", "weather": "Sunny", "high": "26", "low": "15", "wind": "S"}], "alerts": [{"type": "Comfort", "content": "Tonight Kunming comfortable, 14-19C."}]}, "bilibiliHot": {"source": "Bilibili", "fetchTime": now, "highlights": [{"title": "宇树机甲引发热议", "description": "宇树机甲390万起成为微博热搜第一", "url": "https://s.weibo.com/weibo?q=宇树机甲390万起"}, {"title": "汶川地震18周年", "description": "2008.5.12-2026.5.12 B站用户自发纪念", "url": "https://www.bilibili.com/video/av116556235344740/"}, {"title": "特朗普访华在即", "description": "美国总统特朗普时隔九年再度访华", "url": "https://www.bilibili.com/video/av116555312531376/"}], "popularContent": ["陛下何故谋反", "第一天来北京", "许仙买瓜", "崩坏星穹铁道绯英PV", "ENEMY无码重制版", "御剑飞行", "刘谦比手速"]}}}

for fname, data in [("cctv_news.json", cctv_data), ("weibo_hot.json", weibo_data), ("bilibili_hot.json", bilibili_data), ("weather.json", weather_data), ("portal_data.json", portal_data)]:
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("OK:", fname)
print("All done")