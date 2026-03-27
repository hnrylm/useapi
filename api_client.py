import requests
import pandas as pd
# 1. 设置 API 地址 (替换成你想访问的任何公开 API)
# 例子：GitHub 的公开用户信息 API
URL = "https://api.github.com/users/hnrylam" 
def fetch_data():
    try:
        # 2. 设置请求头 (有些 API 需要 Token，有些不需要)
        headers = {
            "Accept": "application/json",
            "User-Agent": "MyPythonApp/1.0"
        }
        # 3. 发送 GET 请求
        print(f"正在尝试连接: {URL} ...")
        response = requests.get(URL, headers=headers)

        # 4. 必须检查状态码 (200 代表成功)
        if response.status_code == 200:
            data = response.json()  # 解析 JSON 资料
            print("连接成功！已获取资料。")
            # 5. 打印资料看看（或者存入 Excel）
            print(f"用户名称: {data.get('login')}")
            print(f"公开仓库数: {data.get('public_repos')}")
            # 如果要存入 Excel (根据数据结构调整)
            # df = pd.DataFrame([data])
            # df.to_excel("api_result.xlsx", index=False)
            print(f"rating: {data.get('starred_url')}")
            print(f"email: {data.get('email')}")
            msg = "Hello" + data.get('login')
            for i in range(1,3):
                print(f"{msg}")
        elif response.status_code == 403:
            print("访问被拒绝：可能需要 API Key 或请求太频繁。")
        else:
            print(f"访问失败，状态码: {response.status_code}")
    except Exception as e:
        print(f"程序运行出错: {e}")
if __name__ == "__main__":
    fetch_data()
