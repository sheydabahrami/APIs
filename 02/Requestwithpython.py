import requests
import json

url = "https://europe-west6-imposing-eye-332615.cloudfunctions.net/sentiment_analysis_function"

payload = json.dumps({
  "model": [
    "LinearSVC"
  ],
  "x": [
    "I love Brokeback Mountain",
    "I dislike Brokeback Mountain"
  ]
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
