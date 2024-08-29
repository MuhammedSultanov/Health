import requests
import json

API_KEY = "AIzaSyBQwHJ0DJIwsl2qGDI2WVvM73F_koDuxuI"
url = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={API_KEY}"

headers = {
    'Content-Type': 'application/json',
}

data = {
    "contents": [
        {
            "role": "user",
            "parts": [
                {"text": "Hello! I’d love to help you achieve your health goals. Please share your recent health data, such as your activity levels, sleep patterns, dietary habits, or any other relevant metrics you’re tracking. Based on the trends in your data, I’ll provide personalized insights and actionable tips to help you improve your overall well-being. Whether you're looking to boost your energy, improve your sleep, or make healthier dietary choices, I'm here to assist!"}
            ]
        }
    ]
}

response = requests.post(url, headers=headers, data=json.dumps(data))
with open("response.json", "w") as f:
    f.write(json.dumps(response.json(), indent=4))
print(response.json())
