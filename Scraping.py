import requests
from bs4 import BeautifulSoup
import csv

url = 'https://lenouvelliste.com/'

repons = requests.get(url)

if repons.ok:
    soup = BeautifulSoup(repons.text, "html.parser")
    tit = soup.find_all('h1')  
    lyen = soup.find_all('a')
    atik = soup.find_all('div', class_='lnv-featured-article-lg')

    imj_link = []

    for div in atik:
        imaj = div.find('img')
        if imaj:
            sous_ = imaj.get('src')
            imj_link.append(sous_)

    with open('My_csv.csv', mode='w', newline='') as file:
        ekri = csv.writer(file)

        ekri.writerow(['Tit_yo'])  
        for t in tit:
            ekri.writerow([t.text.strip()])  
            
        ekri.writerow(['Lyen_yo'])
        for l in lyen : 
            ekri.writerow([l.text.strip()])
    
        ekri.writerow(['L_img_yo']) 
        for link in imj_link:
            ekri.writerow([link])
            
print(imj_link)
print(sous_)