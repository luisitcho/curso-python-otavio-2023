import random
import time
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html


# Função para criar uma instância do Chrome com opções personalizadas
def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = Options()

    # Adicionar as opções desejadas ao navegador
    if options:
        for option in options:
            chrome_options.add_argument(option)

    # Criar a instância do Chrome WebDriver
    chrome_browser = webdriver.Chrome(options=chrome_options)

    return chrome_browser


# Função para simular movimento de mouse aleatório
def random_mouse_move(browser):
    action = ActionChains(browser)
    # Movimentação aleatória do mouse
    action.move_by_offset(random.randint(10, 100), random.randint(10, 100))
    action.perform()


if __name__ == '__main__':
    TIME_TO_WAIT = 140

    options = (
        "--disable-gpu",  # Desativa o uso da GPU (melhora a performance)
        # Necessário em alguns ambientes (principalmente servidores)
        "--no-sandbox",
        # Descomente essa linha para rodar sem interface gráfica (headless)
        # "--headless",
    )

    # Criar o navegador com as opções definidas
    browser = make_chrome_browser(*options)
    browser.get('https://www.google.com.br')  # Acessar o Google

    # Esperar até o campo de pesquisa ser localizado
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    # Simular movimento de mouse aleatório antes de digitar
    random_mouse_move(browser)

    # Enviar os dados para o campo de pesquisa
    search_input.send_keys('Hello World!')
    search_input.send_keys(Keys.ENTER)

    # Esperar até os resultados de pesquisa estarem visíveis
    results = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.ID, 'search')  # Espera até a seção de resultados estar disponível
        )
    )

    # Encontrar todos os links nos resultados
    links = results.find_elements(By.TAG_NAME, 'a')

    if links:
        # Simular mais um movimento de mouse antes de clicar
        random_mouse_move(browser)

        # Clicar no primeiro link encontrado
        links[0].click()

    # Dormir por 5 segundos para esperar o carregamento
    time.sleep(TIME_TO_WAIT)
    browser.quit()  # Fechar o navegador
