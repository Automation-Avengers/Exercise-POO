from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
from Veiculos import Veiculos, Carros, Motocicletas  

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def definir_veiculo_carro():
    Veiculos.nome = "Fiat UNO"
    Veiculos.ano = 2024
    Veiculos.valor_diaria = 300
    Carros.tipo_combustivel = "Gasolina"

def definir_veiculo_motocicleta():
    Veiculos.nome = "Yamaha Fazer"
    Veiculos.ano = 2023
    Veiculos.valor_diaria = 75
    Motocicletas.cilindrada = 250

def preencher_formulario(bot, tipo_veiculo):
    bot.find_element('//*[@id="nomeVeiculo"]', By.XPATH).send_keys(Veiculos.nome)
    bot.sleep(500)
    bot.find_element('//*[@id="anoVeiculo"]', By.XPATH).send_keys(Veiculos.ano)
    bot.sleep(500)
    bot.find_element('//*[@id="valorDiario"]', By.XPATH).send_keys(Veiculos.valor_diaria)
    bot.sleep(500)
    if tipo_veiculo == 'carro':
        bot.find_element('//*[@id="formVeiculo"]/div[1]/div[1]/label', By.XPATH).click()
        bot.sleep(500)
        bot.find_element('//*[@id="combustivel"]', By.XPATH).send_keys(Carros.tipo_combustivel)
        bot.sleep(500)
    elif tipo_veiculo == 'motocicleta':
        bot.find_element('//*[@id="formVeiculo"]/div[1]/div[2]/label', By.XPATH).click()
        bot.sleep(500)
        bot.find_element('//*[@id="cilindrada"]', By.XPATH).send_keys(Motocicletas.cilindrada)
        bot.sleep(500)

    bot.find_element('//*[@id="formVeiculo"]/button', By.XPATH).click()

def preencher_formulario_calculo(bot):
    bot.browse("http://127.0.0.1:5000/")
    bot.find_element('/html/body/div/button[2]', By.XPATH).click()

    bot.find_element('//*[@id="veiculo"]', By.XPATH).click()
    bot.sleep(300) 

    Veiculos.dias = 7

    bot.find_element('//*[@id="veiculo"]/option[3]', By.XPATH).click()
    bot.sleep(500)
    bot.find_element('//*[@id="dias"]', By.XPATH).send_keys(Veiculos.dias)
    bot.sleep(500)
    bot.find_element('//*[@id="formCalculo"]/button', By.XPATH).click()
    bot.sleep(2000)

    bot.browse("http://127.0.0.1:5000/")
    bot.find_element('/html/body/div/button[2]', By.XPATH).click()

    bot.find_element('//*[@id="veiculo"]', By.XPATH).click()
    bot.sleep(300) 

    Veiculos.dias = 8
    Veiculos.cupom = "DESCONTO5"

    bot.find_element('//*[@id="veiculo"]/option[2]', By.XPATH).click()
    bot.sleep(500)
    bot.find_element('//*[@id="dias"]', By.XPATH).send_keys(Veiculos.dias)
    bot.sleep(500)
    bot.find_element('//*[@id="cupom"]', By.XPATH).send_keys(Veiculos.cupom)

    bot.find_element('//*[@id="formCalculo"]/button', By.XPATH).click()
    bot.sleep(500)

def not_found(label):
    print(f"Element not found: {label}")

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()
    bot.browse("http://127.0.0.1:5000/")
    bot.find_element('/html/body/div/button[1]', By.XPATH).click()

    definir_veiculo_carro()
    preencher_formulario(bot, 'carro')

    bot.browse("http://127.0.0.1:5000/")
    bot.find_element('/html/body/div/button[1]', By.XPATH).click()

    definir_veiculo_motocicleta()
    preencher_formulario(bot, 'motocicleta')
    
    preencher_formulario_calculo(bot)

    bot.sleep(5)
    bot.wait(3000)
    bot.stop_browser()

if __name__ == '__main__':
    main()
