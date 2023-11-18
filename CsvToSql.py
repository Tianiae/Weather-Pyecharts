# coding=gb2312
import pymysql
import pandas as pd

# ���ӵ� MySQL ���ݿ�
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='root',
    db='python_weather',
    charset='utf8'
)

# �������ݿ��α�
cursor = conn.cursor()

# ��ȡ CSV �ļ�
csv_file_path = 'hong_kong_weather_7days.csv'
weather_df = pd.read_csv(csv_file_path, encoding='utf-8')

# ����Ŀ��������
target_table = 'weather_data'

# ������
create_table_sql = f"""
CREATE TABLE IF NOT EXISTS {target_table} (
    ���� DATE,
    ����¶� FLOAT,
    ����¶� FLOAT,
    �������� VARCHAR(255),
    ҹ������ VARCHAR(255),
    ������� VARCHAR(255),
    ҹ����� VARCHAR(255),
    ������� VARCHAR(255),
    ҹ����� VARCHAR(255)
);
"""

cursor.execute(create_table_sql)

# ��������
insert_data_sql = f"""
INSERT INTO {target_table} (����, ����¶�, ����¶�, ��������, ҹ������, �������, ҹ�����, �������, ҹ�����)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

for index, row in weather_df.iterrows():
    cursor.execute(insert_data_sql, (
        pd.to_datetime(row["����"]).date(),
        row["����¶�"],
        row["����¶�"],
        row["��������"],
        row["ҹ������"],
        row["�������"],
        row["ҹ�����"],
        row["�������"],
        row["ҹ�����"]
    ))

conn.commit()

print("CSV �ļ��ɹ����뵽���ݿ����.")

conn.close()