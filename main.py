from selenium import webdriver
from time import sleep
from playsound import playsound

url = "https://www.4devs.com.br/gerador_de_cpf"
url2 = "https://www.4devs.com.br/validador_cpf"
text3 = []

playsound('start.wav')
def log(pop):
    with open("cpfs.txt", 'a') as f:
        print(pop, file=f)
    print(pop)


def gerar_cpf():
    hello = int(input("olá, qual é a quantidade de CPFs que você quer gerar?"))
    driver = webdriver.Chrome(r"C:\Users\lucas.dias\Downloads\chromedriver\chromedriver.exe")
    driver.get(url)

    for _ in range(hello):
        text = []
        driver.find_element_by_id('bt_gerar_cpf').click()
        sleep(1)
        text2 = driver.find_element_by_id('texto_cpf').text
        text.append(text2)
        log(text)
    # testar_cpf(hello)
    playsound('end.wav')


# def testar_cpf(x):
#    driver = webdriver.Chrome(r"C:\Users\lucas.dias\Downloads\chromedriver\chromedriver.exe")
#    driver.get(url2)
#    i=0
#    for _ in range (x):
#        inputElement = driver.find_element_by_id('txt_cpf')
#        inputElement.send_keys(text[i])
#        driver.find_element_by_id('bt_validar_cpf').click()
#        i=i+1
#        inputElement.clear()
#        sleep(2)


gerar_cpf()
