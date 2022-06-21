from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php')