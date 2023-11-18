# coding=gb2312
import pymysql
import pandas as pd

# 连接到 MySQL 数据库
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    db='python_weather',
    charset='utf8'
)

# 创建数据库游标
cursor = conn.cursor()

# 读取 CSV 文件
csv_file_path = 'hong_kong_weather_7days.csv'
weather_df = pd.read_csv(csv_file_path, encoding='utf-8')

# 设置目标表的名称
target_table = 'weather_data'

# 创建表
create_table_sql = f"""
CREATE TABLE IF NOT EXISTS {target_table} (
    日期 DATE,
    最高温度 FLOAT,
    最低温度 FLOAT,
    白天天气 VARCHAR(255),
    夜晚天气 VARCHAR(255),
    白天风向 VARCHAR(255),
    夜晚风向 VARCHAR(255),
    白天风力 VARCHAR(255),
    夜晚风力 VARCHAR(255)
);
"""

cursor.execute(create_table_sql)

# 插入数据
insert_data_sql = f"""
INSERT INTO {target_table} (日期, 最高温度, 最低温度, 白天天气, 夜晚天气, 白天风向, 夜晚风向, 白天风力, 夜晚风力)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

for index, row in weather_df.iterrows():
    cursor.execute(insert_data_sql, (
        pd.to_datetime(row["日期"]).date(),
        row["最高温度"],
        row["最低温度"],
        row["白天天气"],
        row["夜晚天气"],
        row["白天风向"],
        row["夜晚风向"],
        row["白天风力"],
        row["夜晚风力"]
    ))

conn.commit()

print("CSV 文件成功导入到数据库表中.")

conn.close()