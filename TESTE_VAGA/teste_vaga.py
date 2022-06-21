from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path=r'./chromedriver.exe')

driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php')

driver.find_element(By.CSS_SELECTOR,'input[id="endereco"]').send_keys('04547-130')
sleep(1)
driver.find_element(By.CSS_SELECTOR,'button[id="btn_pesquisar"]').click()
sleep(1)

try:
    logradouro = driver.find_element(By.CSS_SELECTOR,'table[id="resultado-DNEC"] tbody tr td[data-th="Logradouro/Nome"]').text
    bairro = driver.find_element(By.CSS_SELECTOR,'table[id="resultado-DNEC"] tbody tr td[data-th="Bairro/Distrito"]').text
    uf = driver.find_element(By.CSS_SELECTOR,'table[id="resultado-DNEC"] tbody tr td[data-th="Localidade/UF"]').text
    cep = driver.find_element(By.CSS_SELECTOR,'table[id="resultado-DNEC"] tbody tr td[data-th="CEP"]').text
    
    with open("logradouro.txt","a",encoding="utf-8") as arquivo:
        arquivo.write(f'Logradouro/Nome: {logradouro}\n')
        arquivo.write(f'Bairro/Distrito: {bairro}\n')
        arquivo.write(f'Localidade/UF: {uf}\n')
        arquivo.write(f'CEP: {cep}\n\n')
    
    driver.get('https://www.google.com.br')
    
    driver.find_element(By.CSS_SELECTOR,'input[aria-label="Pesquisar"]').send_keys(f'{logradouro} - {bairro}')
    driver.find_element(By.CSS_SELECTOR,'input[aria-label="Pesquisar"]').send_keys(Keys.ENTER)

    driver.find_element(By.CSS_SELECTOR,'.lu_map_section > a').click()
    sleep(2)
    driver.find_element(By.CSS_SELECTOR,'div[id="minimap"] > div > div button[aria-labelledby="widget-minimap-icon-overlay"]').click()
    sleep(3)

    driver.get_screenshot_as_png()
    
except NoSuchElementException:
    print("elemento nao encontrado")

sleep(1)

#driver.close()