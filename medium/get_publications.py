
import requests
import conf

response = requests.get(
  url= f"{conf.ENDPOINT}/users/{conf.USER_ID}/publications",
  headers=conf.HEADER,
  params={"accessToken" : conf.INTEGRATION_TOKEN},
)

print(f"{conf.ENDPOINT}/users/{conf.USER_ID}/publications")
print(response.json())