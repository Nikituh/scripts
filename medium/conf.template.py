
#######
# This is the template for our configuration file. To use scripts in this folder create a file named "conf.py"
# and have the contents of that file be the same as this one, except fill the properties with actual values
# 
# Source for snippets here: https://medium.com/geekculture/rest-api-in-medium-8539340f2650
#######

INTEGRATION_TOKEN = ""
USER_ID = ""

ENDPOINT = "https://api.medium.com/v1"
HEADER = {
    "Accept":	"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding"	:"gzip, deflate, br",
    "Accept-Language"	:"en-US,en;q=0.5",
    "Connection"	:"keep-alive",
    "Host"	:"api.medium.com",
    "TE"	:"Trailers",
    "Upgrade-Insecure-Requests":	"1",
    "User-Agent":	"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
}