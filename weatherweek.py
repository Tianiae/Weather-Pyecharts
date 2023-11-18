# coding=gb2312
import pandas as pd
import requests

url = "https://weather.cma.cn/api/weather/"
city_id = "45005"  # ��۵ĳ���ID
response = requests.get(url + city_id)
data = response.json()

location = data["data"]["location"]
daily = data["data"]["daily"]
last_update = data["data"]["lastUpdate"]

columns = ["����", "����¶�", "����¶�", "��������", "ҹ������", "�������", "ҹ�����", "�������", "ҹ�����"]
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
        "����": date,
        "����¶�": high_temp,
        "����¶�": low_temp,
        "��������": day_weather,
        "ҹ������": night_weather,
        "�������": day_wind_direction,
        "ҹ�����": night_wind_direction,
        "�������": day_wind_scale,
        "ҹ�����": night_wind_scale
    }, ignore_index=True)

print("����ID:", location["id"])
print("��������:", location["name"])
print("������ʱ��:", last_update)

weather_df.to_csv('hong_kong_weather_7days1.csv', index=False, encoding='utf-8-sig')



