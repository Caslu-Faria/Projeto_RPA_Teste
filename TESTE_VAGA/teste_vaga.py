from tokenize import String
from selenium import webdriver

driver=webdriver.Chrome(executable_path=r'./chromedriver.exe')

driver.get('https://buscacepinter.correios.com.br/app/endereco/index.php')
driver.find_element_by_xpath('//*[@id="endereco"]').send_keys('04547-130')  

