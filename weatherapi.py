import requests
import pandas as pd

# 1. 定义官方 API 链接
url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=sc"


def save_hk_temp_to_excel():
    try:
        # 2. 发送请求获取数据
        response = requests.get(url)
        response.raise_for_status() # 确保请求成功
        
        # 3. 解析 JSON 数据 (API 已经帮我们把资料整理好了)
        data = response.json()
        
        # 4. 提取各站点的温度列表
       
        # 假設 data 是 response.json() 的結果
        temp_list = data.get('temperature').get('data')

        # 獲取第 2 個地點 (編號 1) 的資訊
        place = temp_list[1].get('place') # 結果會是 "香港天文台"
        value = temp_list[1].get('value') # 結果會是 24
        print(f"地区：{place}, 温度：{value}")
        if not temp_list:
            print("未能获取到温度数据")
            return

        # 5. 使用 Pandas 转换为表格格式
        df = pd.DataFrame(temp_list)
        
        # 整理表头：通常包含 'place' (站名), 'value' (数值), 'unit' (单位)
        df.columns = ['地点', '气温', '单位']
        
        # 6. 保存到 Excel
        file_name = "香港实时气温表.xlsx"
        df.to_excel(file_name, index=False)
        
        print(f"自动化成功！数据已存入: {file_name}")
        print(f"更新时间: {data.get('updateTime')}")

    except Exception as e:
        print(f"发生错误: {e}")

# 执行程序
if __name__ == "__main__":
    save_hk_temp_to_excel()
