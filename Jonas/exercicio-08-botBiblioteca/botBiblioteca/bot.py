from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager

from Autor import Autor
from Livro import Livro
from Biblioteca import Biblioteca

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def preencher_formulario(bot, codigo, nome):
    bot.sleep(500)
    bot.find_element('//*[@id="codigoLivro"]', By.XPATH).send_keys(codigo)
    bot.sleep(500)
    bot.find_element('//*[@id="nomeCliente"]', By.XPATH).send_keys(nome)
    bot.find_element('//*[@id="emprestimoForm"]/button', By.XPATH).click()    
    bot.wait(1000)

def listar_emprestimos(biblioteca):
    print("\nLivros emprestados:")
    for codigo, cliente in biblioteca._Biblioteca__emprestimos.items():  
        print(f"Código: {codigo}, Cliente: {cliente}")

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    autor_hp = Autor("J.K. Rowling")
    livro_hp1 = Livro("Harry Potter e a Pedra Filosofal", autor_hp, "003")
    livro_hp2 = Livro("Harry Potter e a Câmara Secreta", autor_hp, "004")
    
    autor_jv = Autor("Suzanne Collins")
    livro_jv1 = Livro("Jogos Vorazes", autor_jv, "005")
    livro_jv2 = Livro("Catching Fire", autor_jv, "006")

    biblioteca = Biblioteca("Biblioteca Municipal")
    biblioteca.adicionar_livro(livro_hp1)
    biblioteca.adicionar_livro(livro_hp2)
    biblioteca.adicionar_livro(livro_jv1)
    biblioteca.adicionar_livro(livro_jv2)

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()
    bot.browse("C:\\Users\\matutino\\Documents\\Exercise-POO\\Jonas\\exercicio-08-botBiblioteca\\botBiblioteca\\index.html") # Trocar caminho pelo certo
    
    codigo = livro_hp1.codigo
    nome = "Jonas"
    preencher_formulario(bot, codigo, nome)

    if biblioteca.registrar_emprestimo(codigo, nome):
        print(f"Empréstimo registrado: Código {codigo}, Cliente {nome}")
    else:
        print(f"Falha ao registrar o empréstimo para o código {codigo}.")

    print(f"\nLivros disponíveis após empréstimo: {biblioteca.mostrar_livros_disponiveis()}") 

    bot.wait(3000)

    bot.stop_browser()

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
