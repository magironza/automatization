# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 18:38:54 2020

@author: mWX619168
"""

from selenium import webdriver
from pandas import DataFrame
#from selenium.webdriver.common.keys import Keys
#import os
#import glob
import time
#import re
from selenium.webdriver.chrome.options import Options


chromeOptions = Options()
chromeOptions.add_experimental_option("prefs", {
    "download.default_directory" : "D:\mover\DescargasPython2"
    } )

driver = webdriver.Chrome(executable_path="D:\mover\TestNavegador\chromedriver", chrome_options=chromeOptions)

#pagina a la cual tomaremos los datos
driver.get("https://community.secop.gov.co/Public/Tendering/ContractNoticeManagement/Index?currentLanguage=es-CO&Page=login&Country=CO&SkinName=CCE")

#para hacer la pantalla de chrome completa
driver.maximize_window()
x = 0



nombre_entidad = "INSTITUTO COLOMBIANO DE BIENESTAR FAMILIAR"

timer = 0

while timer < 200:
    try:
        entidad = driver.find_element_by_xpath('//*[@id="txtAuthorityName"]')
        entidad.send_keys(nombre_entidad)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="btnSearchButton"]').click() 
        #entidad.send_keys(Keys.ENTER)
        time.sleep(2)
        break
    except:
        time.sleep(10)
        #print(timer)
        timer = timer + 1
        


campo_entidad = []
campo_referencia = []
campo_descripcion = []
campo_fase_actual = []
campo_fecha_publicacion = []
campo_fecha_presenta_oferta = []
campo_cuantia = []
campo_estado = []



def guardar_tabla(x):
    print("valor de x ",x)
    reportes = (x*5) + 5
    print("valor reportes:", reportes)
    for j in range(0, reportes):
        try:
            
            campo_entidad.append(driver.find_element_by_xpath('//*[@id="tblMainTable_trRowMiddle_tdCell1_tblForm_trGridRow_tdCell1_grdResultList_tdAuthorityNameCol_spnMatchingResultAuthorityName_'+str(j)+'"]').text)
            campo_referencia.append(driver.find_element_by_xpath('//*[@id="tblMainTable_trRowMiddle_tdCell1_tblForm_trGridRow_tdCell1_grdResultList_tdUniqueIdentifierCol_spnMatchingResultReference_'+str(j)+'"]').text)
            campo_descripcion.append(driver.find_element_by_xpath('//*[@id="tblMainTable_trRowMiddle_tdCell1_tblForm_trGridRow_tdCell1_grdResultList_tdDescriptionCol_spnMatchingResultDescription_'+str(j)+'"]').text)
            campo_fase_actual.append(driver.find_element_by_xpath('//*[@id="tblMainTable_trRowMiddle_tdCell1_tblForm_trGridRow_tdCell1_grdResultList_tdCurrentPhaseCol_spnMatchingResultPhaseCode_'+str(j)+'"]').text)
            campo_fecha_publicacion.append(driver.find_element_by_id('dtmbRequestOnlinePublishingDate_'+str(j)+'_txt').text)
            campo_fecha_presenta_oferta.append(driver.find_element_by_id('dtmbDueDateForReceivingReplies_'+str(j)+'_txt').text)
            
            try:
                campo_cuantia.append(driver.find_element_by_id('cbxBasePriceValue_'+str(j)).text)
            except:
                campo_cuantia.append("No value")
                print("no hay valor", j)
            
            campo_estado.append(driver.find_element_by_xpath('//*[@id="tblMainTable_trRowMiddle_tdCell1_tblForm_trGridRow_tdCell1_grdResultList_tdContractNoticeStateCol_spnMatchingResultContractNoticeState_'+str(j)+'"]').text)
        except:
            print("Hay un error:", j)
            #print(driver.find_element_by_id('cbxBasePriceValue_'+str(j)).text)
            break

    
    base_datos = [campo_entidad, campo_referencia, campo_descripcion, campo_fecha_publicacion,  campo_fecha_presenta_oferta, campo_fase_actual, campo_cuantia, campo_estado]
    #print(base_datos)
    
    df= DataFrame(base_datos).transpose()
    df.columns=["EntidadEstatal", "Referencia", "Descripcion", "FechaActual","FechaPresentacionOfertas","FaseActual", "Cuantia", "Estado"]

    print("---------cambio----------")
    #print(df)
    df.to_excel("documento_final.xlsx", sheet_name="Data")

#esta parte es solo de prueba, se debe quitar y quitar el comentario de ver_todo
#x=1
#guardar_tabla(x)    
    
def ver_todo():
    x = 0
    while x<200:
        try:
            boton_mas = driver.find_element_by_class_name("VortalPaginatorMorePages")
            if boton_mas:
                boton_mas.click()
                time.sleep(3.5)
                x= x+1
            print(x)
        except:
            print("Se debe guardar toda la info")
            break
    guardar_tabla(x)

    
ver_todo()


#driver.close()