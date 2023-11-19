# coding=gb2312
import pandas as pd
import requests

url = "https://weather.cma.cn/api/weather/"
city_id = "45005"  # 香港的城市ID
response = requests.get(url + city_id)
data = response.json()

location = data["data"]["location"]
daily = data["data"]["daily"]
last_update = data["data"]["lastUpdate"]

columns = ["日期", "最高温度", "最低温度", "白天天气", "夜晚天气", "白天风向", "夜晚风向", "白天风力", "夜晚风力"]
weather_df = pd.DataFrame(columns=columns)

for day_data in daily:
    date = day_data["date"]
    high_temp = day_data["high"]
    low_temp = day_data["low"]
    day_weather = day_data["dayText"]
    night_weather = day_data["nightText"]
    day_wind_direction = day_data["dayWindDirection"]
    night_wind_direction = day_data["nightWindDirection"]
    day_wind_scale = day_data["dayWindScale"]
    night_wind_scale = day_data["nightWindScale"]

    weather_df = weather_df.append({
        "日期": date,
        "最高温度": high_temp,
        "最低温度": low_temp,
        "白天天气": day_weather,
        "夜晚天气": night_weather,
        "白天风向": day_wind_direction,
        "夜晚风向": night_wind_direction,
        "白天风力": day_wind_scale,
        "夜晚风力": night_wind_scale
    }, ignore_index=True)

print("城市ID:", location["id"])
print("城市名称:", location["name"])
print("最后更新时间:", last_update)

weather_df.to_csv('hong_kong_weather_7days.csv', index=False, encoding='utf-8-sig')



