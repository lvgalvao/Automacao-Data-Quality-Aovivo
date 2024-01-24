from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

# Define um timeout implícito
driver.set_page_load_timeout(5)  # 5 segundos

try:
    driver.get("http://localhost:8501")
    
    # Aguarda até que o título da página esteja presente
    WebDriverWait(driver, 5).until(EC.title_contains("Validador de Schema de Excel"))
    print("Página carregada com sucesso e o título está correto.")

except TimeoutException:
    print("Tempo de carregamento da página excedeu o limite.")
finally:
    driver.quit()
