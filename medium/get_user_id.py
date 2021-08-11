import requests
import conf

token = conf.INTEGRATION_TOKEN

if __name__ == "__main__":
    from pprint import pprint
    
    # sending request to medium
    response = requests.get(
        url=conf.ENDPOINT + "/me", #https://api.medium.com/me
        headers=conf.HEADER,
        params={"accessToken" : token},
    )
    # checking response from server
    if response.status_code ==  200:
        pprint(response.json()) # displaying the json 
        response_json = response.json()
        userId = response_json["data"]["id"]