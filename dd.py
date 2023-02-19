import requests
import requests

URL = " https://www.linode.com/docs/guides/create-restful-api-using-python-and-flask/"
page = requests.get(URL)

print(page.text)