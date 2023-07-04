import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

url         = 'https://cpl.anp.gov.br/anp-cpl-web/public/sigep/consulta-producao-mensal-hidrocarbonetos/consulta.xhtml'

### Start - Selenium WebScraping

print("Etapa 1 - Abrir ChromeDrive")

options = Options()
options.add_argument('--headless=new')
options.add_argument('--no-sandbox')
#options.add_argument('--single-process')
#options.add_argument('--disable-dev-shm-usage')
options.binary_location = "/home/misteryoh/Coding/Git/anp-extractor/chrome-driver/headless-chromium"

# pass the defined options and executable_path to initialize the web driver 
driver = webdriver.Chrome(executable_path='/home/misteryoh/Coding/Git/anp-extractor/chrome-driver/chromedriver', chrome_options=options) 

print("Etapa 2 - Requisição no ChromeDrive com URL")

driver.get(url)

time.sleep(5)
driver.find_element_by_i
campo_texto = driver.find_element_by_id('frmConsulta:anoMesInicio:inputText').text = '012022'
time.sleep(5)
verifica = driver.find_element_by_id('frmConsulta:anoMesInicio:inputText')
driver.find_element_by_id('frmConsulta:anoMesFim:inputText').send_keys('012022')

time.sleep(5)
driver.find_element_by_id('frmConsulta:buttonConsultaQuantidade').submit()
time.sleep(5)

teste = driver.find_element_by_id('frmConsulta:panelResultadoConsulta')
time.sleep(10)
# driver.find_element_by_id('frmConsulta:buttonExportarCSV').submit()


# dt_inicio = driver.find_element_by_id('frmConsulta:anoMesInicio:inputText')
# dt_inicio.clear()
# dt_inicio.send_keys('01/2022')

# dt_fim = driver.find_element_by_id('frmConsulta:anoMesFim:inputText')
# dt_fim.clear()
# dt_fim.send_keys('01/2022')

# btn_consultar = driver.find_element_by_id('frmConsulta:buttonConsultaQuantidade')
# btn_consultar.submit()

# time.sleep(10)

# btn_download = driver.find_element_by_id('frmConsulta:buttonExportarCSV')
# btn_download.submit()