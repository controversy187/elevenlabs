import requests

url = "https://api.elevenlabs.io/v1/voices"

headers = {
	"Accept": "application/json",
	"xi-api-key": "<xi-api-key>"
}

response = requests.get(url, headers=headers)

print(response.text)