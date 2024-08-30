from bs4 import *
import requests
import os

def readURL(param):
    for i,a in enumerate(param):
        try:
            a_link = a["href"]
            f.write(a_link + '\n')
        except:
            print(a)
            continue

def main(num):
    r = requests.get('') # link read url
    soup = BeautifulSoup(r.text, 'html.parser')
    article = soup.select(".") # tag parents of <a/>
    #print(article)
    readURL(article)


f = open("result.txt", "a")
for x in range(1, 2):
    print(x)
    main(x)
f.close()