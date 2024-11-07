from botcity.core import DesktopBot
from botcity.maestro import *

BotMaestroSDK.RAISE_NOT_CONNECTED = False

def preencher_funcionario():
    bot = DesktopBot()
    bot.browse("C:\\Users\\jonas\\BotFuncionario\\dist\\interface.exe") # Substitua pelo caminho correto
    
    # Funcionário Horista
    
    nome = "Jonas"
    matricula = "03338832"
    valor_hora = "15.00"
    horas_trabalhadas = "220"

    if not bot.find( "nome", matching=0.97, waiting_time=10000):
        not_found("nome")
    bot.click_relative(113, 10)
    bot.sleep(0.5)
    bot.type_keys(nome)
    
    if not bot.find( "matricula", matching=0.97, waiting_time=10000):
        not_found("matricula")
    bot.click_relative(131, 10)
    bot.sleep(0.5)
    bot.type_keys(matricula)

    if not bot.find( "valor_hora", matching=0.97, waiting_time=10000):
        not_found("valor_hora")
    bot.click_relative(148, 13)
    bot.sleep(0.5)
    bot.type_keys(valor_hora)

    if not bot.find( "horas_trabalhadas", matching=0.97, waiting_time=10000):
        not_found("horas_trabalhadas")
    bot.click_relative(218, 13)
    bot.sleep(0.5)
    bot.type_keys(horas_trabalhadas)
    
    if not bot.find( "cadastrar_horista", matching=0.97, waiting_time=10000):
        not_found("cadastrar_horista")
    bot.click()

    
    if not bot.find( "fechar_horista", matching=0.97, waiting_time=10000):
        not_found("fechar_horista")
    bot.click()

    # Funcionário Mensalista

    nome = "Yasmin"
    matricula = "47459584"
    salario_mensal = "4500.00"

    if not bot.find( "mensalista", matching=0.97, waiting_time=10000):
        not_found("mensalista")
    bot.click()

    if not bot.find( "nome", matching=0.97, waiting_time=10000):
        not_found("nome")
    bot.click_relative(108, 13)
    bot.sleep(0.5)
    bot.type_keys(nome)
    
    if not bot.find( "matricula", matching=0.97, waiting_time=10000):
        not_found("matricula")
    bot.click_relative(136, 10)
    bot.sleep(0.5)
    bot.type_keys(matricula)

    if not bot.find( "salario_mensal", matching=0.97, waiting_time=10000):
        not_found("salario_mensal")
    bot.click_relative(194, 14)
    bot.sleep(0.5)
    bot.type_keys(salario_mensal)

    if not bot.find( "cadastrar", matching=0.97, waiting_time=10000):
        not_found("cadastrar")
    bot.click()
    
    if not bot.find( "fechar_mensalista", matching=0.97, waiting_time=10000):
        not_found("fechar_mensalista")
    bot.click()

    # Funcionário Comissionado

    nome = "Deise"
    matricula = "5159584"
    salario_base = "3000.00"
    vendas = "15000.00"
    taxa = "0.10"

    if not bot.find( "comissionado", matching=0.97, waiting_time=10000):
        not_found("comissionado")
    bot.click()

    if not bot.find( "nome", matching=0.97, waiting_time=10000):
        not_found("nome")
    bot.click_relative(125, 14)
    bot.sleep(0.5)
    bot.type_keys(nome)

    if not bot.find( "matricula", matching=0.97, waiting_time=10000):
        not_found("matricula")
    bot.click_relative(132, 12)
    bot.sleep(0.5)
    bot.type_keys(matricula)

    if not bot.find( "salario_base", matching=0.97, waiting_time=10000):
        not_found("salario_base")
    bot.click_relative(183, 14)
    bot.sleep(0.5)
    bot.type_keys(salario_base)

    if not bot.find( "vendas", matching=0.97, waiting_time=10000):
        not_found("vendas")
    bot.click_relative(136, 15)
    bot.sleep(0.5)
    bot.type_keys(vendas)

    if not bot.find( "taxa_comissao", matching=0.97, waiting_time=10000):
        not_found("taxa_comissao")
    bot.click_relative(219, 12)
    bot.sleep(0.5)
    bot.type_keys(taxa)
    
    if not bot.find( "cadastrar_comissionado", matching=0.97, waiting_time=10000):
        not_found("cadastrar_comissionado")
    bot.click()
    
    if not bot.find( "fechar_comissionado", matching=0.97, waiting_time=10000):
        not_found("fechar_comissionado")
    bot.click()
    
    if not bot.find( "fechar_app", matching=0.97, waiting_time=10000):
        not_found("fechar_app")
    bot.click()
    

def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()

    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    preencher_funcionario()

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()
