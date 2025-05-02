import requests
url="https://example.com"

try:
    response = requests.get(url)
    print(f"{url} is UP and the status code is :{response.status_code}")
except requests.ConnectionError:
    print(f"{url} is down")

finally:
    print("the session closed !!!")