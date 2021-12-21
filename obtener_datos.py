# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:17:27 2020

@author: mWX619168
"""

from selenium import webdriver
import os
import glob
import time
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {
    "download.default_directory" : "D:\mover\DescargasPython"
    } )

driver = webdriver.Chrome(executable_path="D:\mover\TestNavegador\chromedriver", chrome_options=chromeOptions)

#pagina a la cual tomaremos los datos
driver.get("https://community.secop.gov.co/Public/App/AnnualPurchasingPlanManagementPublic/Index?currentLanguage=en&Page=login&Country=CO&SkinName=CCE")

#para hacer la pantalla de chrome completa
driver.maximize_window()

#se setean los valores iniciales para comenzar la descarga
pagina_inicial=0
inicial = pagina_inicial*5
final = inicial + 5 

#directorio en el que se guardaran los archivos
path_archivos = 'D:\mover\DescargasPython'


#funcion para descargar los archivos
def descargar(inicial, final):
    for j in range(inicial, final):
        # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "myDynamicElement"))
                                                      
        driver.find_element_by_xpath('//*[@id="lnkGridAppDownloadLink_'+str(j)+'"]').click()
        time.sleep(10)
    
        #cambiar nombre del archivo descaegado
        #print(driver.find_element_by_id("spnGridAppEntitySpan1_"+str(j)).text)
        #filename = max([f for f in os.listdir(path_archivos)], key=os.path.getctime)
        filename = max(glob.glob(path_archivos), key=os.path.getctime)
        print(filename)
        #os.rename(path_archivos/filename, driver.find_element_by_id("spnGridAppEntitySpan1_"+str(j)).text+".zip")
        #shutil.move(os.path.join('D:\mover\DescargasPython',filename),driver.find_element_by_id("spnGridAppEntitySpan1_"+str(j)).text+".zip")

#llamada incial de descarga para la primera página        
descargar(inicial, final)   


while pagina_inicial < 3:
    
    cambiar_pestana = driver.find_elements_by_class_name("VortalPaginatorPage")
    boton_oprimir = cambiar_pestana[-1].get_attribute("innerHTML")
    pagina_inicial= pagina_inicial + 1
    inicial = pagina_inicial*5
    final = inicial + 5 
    
       
    if not pagina_inicial%2==0:
        print("pagina siguinte ---")
        driver.find_element_by_xpath('//*[@id="grdGridAPP_Paginator_goToPage_Next"]').click()
        time.sleep(2)
        descargar(inicial, final)
        
    else:
        print("3 puntos ---")
        driver.find_element_by_xpath('//*[@id="grdGridAPP_Paginator_goToPage_MoreItems"]').click()
        time.sleep(2)
        descargar(inicial, final)
        

#print(driver.find_element_by_xpath('//*[@id="grdGridAPP_Paginator_goToPage_MoreItems"]').get_attribute("value"))
#for i in contador_paginas:

driver.close()








