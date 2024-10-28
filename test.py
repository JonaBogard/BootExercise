from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd

options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

test = webdriver.Chrome()

test.get('https://www.eltiempo.es')

WebDriverWait(test, 10).until(
    EC.element_to_be_clickable((By.XPATH,
                                 '/html/body/div[1]/div/div[3]/div[2]/div[1]/div/div/div[2]/div[1]/a'))
).click()

WebDriverWait(test, 10).until(
    EC.element_to_be_clickable((By.XPATH,
                                 '/html/body/header/div/nav/div[1]/div[2]/div/form/input'))
).send_keys('Madrid')

WebDriverWait(test, 10).until(
    EC.element_to_be_clickable((By.XPATH,
                                 '/html/body/header/div/nav/div[1]/div[2]/div/div/div/div/ul/li[1]/a/div/p[1]'))
).click()

WebDriverWait(test, 10).until(
    EC.element_to_be_clickable((By.XPATH,
                                 '/html/body/div[7]/div[1]/div[4]/div/main/section[3]/section/section/ul/li[2]/h2/a'))
).click()

WebDriverWait(test, 10).until(
    EC.element_to_be_clickable((By.XPATH,
                                 '/html/body/div[7]/div[1]/div[4]/div/main/section[3]/article/ul/li[1]/ul'))
)
texto = test.find_element(By.XPATH, '/html/body/div[7]/div[1]/div[4]/div/main/section[3]/article/ul/li[1]/ul')
texto = texto.text

tiempo_hoy = texto.split('Mañana')[0].split('\n')[1:-1]

print(tiempo_hoy)

temp = list()
mm = list()
pres = list()
v_viento = list()
horas = list()

for i in range(0, len(tiempo_hoy) - 4, 5):
    temp.append(tiempo_hoy[i])
    mm.append(tiempo_hoy[i+1])
    pres.append(tiempo_hoy[i+2])
    v_viento.append(tiempo_hoy[i+3])
    horas.append(tiempo_hoy[i+4])

df = pd.DataFrame({'Temperatura': temp, 'MM': mm, 'Precipitaciones': pres, 'Vel. Viento': v_viento, 'Hora': horas})
print(df)
df.to_csv('tiempo_hoy.csv', index=False)

test.quit()