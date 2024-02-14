from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import re

# & Definir a URL do site
url = "https://www.hablarcondios.org/pt/meditacaodiaria.aspx"

# Configuração para modo headless
options = Options()
options.add_argument('--headless')  # Adiciona a opção para executar em modo headless
options.add_argument('--disable-gpu')  # Desabilita a aceleração de GPU, geralmente necessário no modo headless

# & Abrir o navegador no modo headless
driver = webdriver.Chrome(options)

# Acessar a URL
driver.get(url)

# Obter a data atual
data_atual = datetime.today().strftime("%Y-%m-%d")

# Criar o nome do arquivo com a data
nome_arquivo = f"{data_atual}.md"

# Extrair o conteúdo principal da página
conteudo_pagina = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "body"))
)

texto_formatado = re.sub(
    r"Subscrição Copie este mês.*|.*?Suscripciones",
    "",
    conteudo_pagina.text,
    flags=re.DOTALL,
)

# Salvar o conteúdo em Markdown
with open(nome_arquivo, "w") as arquivo:
    arquivo.write(texto_formatado)

# Fechar o navegador
driver.quit()

print(f"Conteúdo salvo no arquivo {nome_arquivo}")