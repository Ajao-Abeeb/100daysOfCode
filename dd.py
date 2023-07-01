import requests
import requests

URL = "https://download.code-projects.org/details/e13ce994-d280-4a64-90fb-f08663479bb4"
page = requests.get(URL)

print(page.text)