from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import bs4
from pathlib import Path
import requests
import tabula

def obtenerCDT():

    url = 'https://www.bancoprocredit.com.co/es/home.html'
    url2 = 'https://www.bancoprocredit.com.co/images/Tasas_y_Tarifas_PN_18122018_2019.pdf'

    driver = webdriver.Chrome(executable_path=r'C:/Users/Rouzajor/Desktop/Chrome Web Driver/chromedriver.exe')


    try:
        nombrePDF = 'CDTProcredit.pdf'
        file = Path(nombrePDF)
        pdfResponse = requests.get(url2)
        file.write_bytes(pdfResponse.content)


    finally:
        # Cierra el webdriver
        driver.quit()




    #a = soup.find('a', string = 'Tasas y Tarifas')

    #linkPDF = a['href']

    #nombrePDF = 'CDTProCredit.pdf'
    #file = Path(nombrePDF)

    #pdfResponse = requests.get('https://www.bancoprocredit.com.co' + linkPDF)
    #file.write_bytes(pdfResponse.content)


