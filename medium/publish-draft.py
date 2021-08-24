
import requests
import conf
from pathlib import Path

post = Path("posts/01-react-blog.md").read_text()

data = {
    "title": "<add-clever-title-for-preview",
    "contentFormat": "markdown",
    "content": post,
    "tags": ["development", "design"],
    "publishStatus": "draft"
}

response = requests.post(
    url= f"{conf.ENDPOINT}/users/{conf.USER_ID}/posts",
    headers=conf.HEADER,
    data=data,
    params={"accessToken" : conf.INTEGRATION_TOKEN},
)

print(response.json())