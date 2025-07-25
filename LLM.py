import requests

API_KEY = "你的_API_KEY"
API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=" + API_KEY

def ask_gemini(question):
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {"parts": [{"text": question}]}
        ]
    }
    try:
        response = requests.post(API_URL, headers=headers, json=data)
        result = response.json()
        # 解析回答
        answer = result["candidates"][0]["content"]["parts"][0]["text"]
        return answer
    except Exception as e:
        return f"API 錯誤: {e}"

if __name__ == "__main__":
    while True:
        user_input = input("請輸入問題（Ctrl+C 結束）：")
        reply = ask_gemini(user_input)
        print("Gemini 回答：", reply)
