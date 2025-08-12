import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.get("https://todomvc.com/examples/react/dist/")
browser.maximize_window()

itens = ["Estudar para a prova de inglês",
         "Comprar ração",
         "Ir ao mercado",
         "Fazer o exercicio de matemática",
         "Agendar consulta"
]

for item in itens:
    field_input = browser.find_element(By.ID, "todo-input")
    field_input.send_keys(item)
    field_input.send_keys(Keys.ENTER)
    time.sleep(0.5)

checkboxes = browser.find_elements(By.CLASS_NAME, "toggle")
for i in [0, 1, 2]:
    checkboxes[i].click()
    time.sleep(0.3)


Active = browser.find_element(By.XPATH, '//a[text() = "Active"]').click()

Completed = browser.find_element(By.XPATH, '//a[text() = "Completed"]').click()


browser.quit()

