import pandas as pd
import simplejson as json
import bs4 as bs
import requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep
df = pd.read_csv('../data/panama/99.csv')
for link in df['link']:
    print (link)
    url = link
    chromeOptions = webdriver.ChromeOptions()
    browser = webdriver.Chrome(r"C:\Python\chromedriver.exe",options=chromeOptions)
    browser.get(url)
    delay = 3 # segundos
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'elementToPDF')))
        print ("Pagina lista")
        html = browser.page_source
        soup = BeautifulSoup(html, 'lxml')
        div = soup.find("div", {"id": "elementToPDF"})
        f = open( 'csv/'+url[62:]+'.csv', 'w' )
        f.write( str(div) )
        f.close()
        browser.close()
    except TimeoutException:
        print ("Cargando..")    
