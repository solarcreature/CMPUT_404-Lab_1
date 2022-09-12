import requests

print(requests.__version__)
print(requests.get("http://www.google.com/"))

print(requests.get("https://raw.githubusercontent.com/solarcreature/CMPUT_404-Lab_1/main/script.py").text)