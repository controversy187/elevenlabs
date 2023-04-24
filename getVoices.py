import requests
import local_settings

url = "https://api.elevenlabs.io/v1/voices"

headers = {
	"Accept": "application/json",
	"xi-api-key": local_settings.XI_API_KEY
}

response = requests.get(url, headers=headers)

print(response.text)