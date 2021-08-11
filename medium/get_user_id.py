import requests
import conf

token = conf.INTEGRATION_TOKEN

# End point for yout requests
url = "https://api.medium.com/v1"
# header requred
header = {
    "Accept":	"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding"	:"gzip, deflate, br",
    "Accept-Language"	:"en-US,en;q=0.5",
    "Connection"	:"keep-alive",
    "Host"	:"api.medium.com",
    "TE"	:"Trailers",
    "Upgrade-Insecure-Requests":	"1",
    "User-Agent":	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
}


if __name__ == "__main__":
    from pprint import pprint
    
    # sending request to medium
    response = requests.get(
        url=url + "/me", #https://api.medium.com/me
        headers=header,
        params={ "accessToken" : token},
    )
    # checking response from server
    if response.status_code ==  200:
        pprint(response.json()) # displaying the json 
        response_json = response.json()
        userId = response_json["data"]["id"]