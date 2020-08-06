import urllib.request
import requests
from bs4 import BeautifulSoup

r = requests.get('https://icons8.com/icons/pack/free-icons')
print(r.status_code)
soup = BeautifulSoup(r.content,"lxml") 
images = soup.find_all("div",attrs={"class":"icon"})
i = 1;
for image in images:
        print(image.find("a",attrs={"class":"icon-link"}).img.get('src'))
        urllib.request.urlretrieve(image.find("a",attrs={"class":"icon-link"}).img.get('src'),"img/{}.png".format(i))
        i+=1

