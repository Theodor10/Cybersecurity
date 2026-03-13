import requests

url = 'http://68.183.45.143:32000/flag'  # replace with the website URL you want to request

with open("output.txt", "w") as f:
    for i in range(1000):
        response = requests.get(url)
        f.write(response.content.decode() + "\n")
