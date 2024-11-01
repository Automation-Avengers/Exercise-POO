from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
from Formulario import FormBase
from Formulario import FormularioContato
from Formulario import FormularioLogin

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def preencher_formulario_base(bot, formulario):
    bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(formulario.nome)
    bot.sleep(2000)
    
    bot.find_element('//*[@id="email"]', By.XPATH).send_keys(formulario.email)
    bot.sleep(2000)
    
    bot.find_element('//*[@id="telefone"]', By.XPATH).send_keys(formulario.telefone)
    bot.sleep(2000)
    
    bot.find_element('//*[@id="endereco"]', By.XPATH).send_keys(formulario.endereco)
    bot.sleep(2000)

    bot.find_element('//*[@id="data_nascimento"]', By.XPATH).send_keys(formulario.data_nascimento)
    bot.sleep(2000)

    bot.find_element('//*[@id="mensagem"]', By.XPATH).send_keys(formulario.mensagem)
    bot.sleep(2000)

    bot.find_element("/html/body/form/button", By.XPATH).click()
    formulario.exibir_informacoes()

def preencher_formulario_contato(bot, formulario):
    bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(formulario.nome)
    bot.sleep(2000)
    
    bot.find_element('//*[@id="email"]', By.XPATH).send_keys(formulario.email)
    bot.sleep(2000)
    
    bot.find_element('//*[@id="telefone"]', By.XPATH).send_keys(formulario.telefone)
    bot.sleep(2000)
    
    bot.find_element('//*[@id="endereco"]', By.XPATH).send_keys(formulario.endereco)
    bot.sleep(2000)

    bot.find_element('//*[@id="data_nascimento"]', By.XPATH).send_keys(formulario.data_nascimento)
    bot.sleep(2000)
    
    bot.find_element('//*[@id="assunto"]', By.XPATH).send_keys(formulario.assunto)
    bot.sleep(2000)

    bot.find_element('//*[@id="mensagem"]', By.XPATH).send_keys(formulario.mensagem)
    bot.sleep(2000)
    
    bot.find_element("/html/body/form/button", By.XPATH).click()
    formulario.exibir_informacoes()

def preencher_formulario_login(bot, formulario):
    bot.find_element('//*[@id="usuario"]', By.XPATH).send_keys(formulario.email)
    bot.sleep(2000)
    
    bot.find_element('//*[@id="senha"]', By.XPATH).send_keys(formulario.senha)
    bot.sleep(2000)
    
    bot.find_element("/html/body/form/button", By.XPATH).click()
    formulario.exibir_informacoes()

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    nome = "Jonas Santos"
    email = "jonas.santos2302@gmail.com"
    telefone = "(92)99510-5416"
    endereco = "Rua São João, 147 - Cidade Nova"
    data_nascimento = "23/02/2003"
    assunto = "Sistema Lento"
    mensagem = "Notei que o sistema está um pouco lento ultimamente. Poderiam verificar isso?"
    senha = "12345678"

    bot.browse("C:\\Users\\matutino\\Documents\\Exercise-POO\\Jonas\\exercicio-04-botFomulario\\botFormulario\\FormBase.html") # Atualizar caminho
    formulario = FormBase(nome, email, telefone, endereco, data_nascimento, mensagem)
    preencher_formulario_base(bot, formulario)

    bot.browse("C:\\Users\\matutino\\Documents\\Exercise-POO\\Jonas\\exercicio-04-botFomulario\\botFormulario\\FormularioContato.html") # Atualizar caminho
    formulario_contato = FormularioContato(nome, email, telefone, endereco, data_nascimento, assunto, mensagem)
    preencher_formulario_contato(bot, formulario_contato)

    bot.browse("C:\\Users\\matutino\\Documents\\Exercise-POO\\Jonas\\exercicio-04-botFomulario\\botFormulario\\FormularioLogin.html") # Atualizar caminho
    formulario_login = FormularioLogin(email, senha)
    preencher_formulario_login(bot, formulario_login)

    bot.wait(3000)
    bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
