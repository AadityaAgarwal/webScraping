from os import write
from selenium import webdriver as wd
from bs4 import BeautifulSoup as bs
import time,csv

# opening the link of nasa webpage
startUrl='https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
browser=wd.Chrome(r"D:/alkaa/Downloads/chromedriver_win32/chromedriver.exe")

def scrapeData():
    headers=['Name','Light-Years from Earth','PLANET MASS','STELLAR MAGNITUDE','DISCOVERY RATE']
    planetData=[]

    for i in range(0,440):

        soup=bs(browser.page_source,'html.parser')
    
        for ultag in soup.find_all('ul',attrs={'class','exoplanet'}):
            litags=ultag.find_all('li')
            templist=[]

            for index,litag in enumerate(litags):
                if index==0:
                    templist.append(litag.find_all('a')[0].contents[0])
                else:
                    try:
                        templist.append(litag.contents[0])
                    except:
                        templist.append('')
            planetData.append(templist)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('scrapedData.csv','w') as f:
        csvWrite=csv.writer(f)
        csvWrite.writerow(headers)
        csvWrite.writerows(planetData)
scrapeData()