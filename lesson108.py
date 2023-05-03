import requests
import json


response = requests.get('')
todos = json.loads(response.text)
print(todos[:10])