from selenium import webdriver
import time

def obtenerCalificacion():
    driver = webdriver.Chrome()
    driver.get('https://www.fitchratings.com/site/search?request=falabella&content=entity')
    time.sleep(1)

    pathNameB = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/div[8]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/a[1]")
    pathCalificacion = driver.find_element_by_xpath('/html[1]/body[1]/div[3]/div[8]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/table[1]/tbody[1]/tr[1]/td[1]')

    nombreBanco = pathNameB.text
    calificacion = pathCalificacion.text[0:3]

    resp = {nombreBanco:calificacion}

    driver.quit()

    return resp

print(obtenerCalificacion())