from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
from Produto import Produto

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()

    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    bot.browse("C:\\Users\\matutino\\Documents\\Exercise-POO\\Jonas\\exercicio-02-botProduto\\botProduto\\index.html") #Atualizar o caminho
    
    produto = Produto("Açaí", 10.99, 200)

    bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(produto.nome)
    bot.sleep(2000)

    produto.preco = 15.99 # Atualizando o preço usando o setter
    bot.find_element('//*[@id="preco"]', By.XPATH).send_keys(str(produto.preco))
    bot.sleep(2000)

    bot.find_element('//*[@id="quantidade"]', By.XPATH).send_keys(str(produto.quantidade))
    bot.sleep(2000)
    
    bot.find_element("/html/body/div/form/input[4]", By.XPATH).click()
    
    produto.exibir_informacoes()

    bot.wait(3000)

    bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
