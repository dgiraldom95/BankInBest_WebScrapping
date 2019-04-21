from selenium import webdriver
import time
from calificaciones.CalificacionBancaria import CalificacionBancaria


def obtenerCalificacion():
    driver = webdriver.Chrome()
    driver.get('http://www.vriskr.com/productos/banco-caja-social-s-a-antes-bcsc/')
    time.sleep(1)

    #logueo para acceder a los datos de la pagina

    userName = driver.find_element_by_id("user_login")
    userPass = driver.find_element_by_id("user_pass")
    bottomLog = driver.find_element_by_id("wp-submit")

    userName.send_keys("richieknow")
    userPass.send_keys("richie2019")
    bottomLog.click()
    time.sleep(1)

    #accedo a la pagina con la info
    driver.get('http://www.vriskr.com/productos/banco-caja-social-s-a-antes-bcsc/')

   # pathNameBanco = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[2]/ul[1]/li[1]")
    pathCalificacion = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/section[1]/div[1]/div[1]/article[1]/div[1]/div[1]/div[2]/ul[1]/li[4]")

   # nameBanco = str(pathNameBanco.text).split(":")[1]
    calificacion = str(pathCalificacion.text).split(":")[1]

   # fNameB = nameBanco.split("(")[0].strip()
    fcal = calificacion.split("/")[0].strip()

    cal = CalificacionBancaria(str('Banco Caja Social'), str(fcal))


    driver.quit()

    return cal

if __name__ == '__main__':
    calificacion = obtenerCalificacion()
    calificacion.POST('http://157.230.14.37:8080')
