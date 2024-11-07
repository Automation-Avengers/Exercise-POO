from Comissionado import Comissionado
from Horista import Horista
from Mensalista import Mensalista
from Projetista import Projetista

def main():    
    def processar_pagamento(funcionario):
        print(f"Nome: {funcionario.nome}")
        print(f"Salário: {funcionario.calcular_salario():.2f}\n")

    funcionarios = []
    
    try:
        funcionarios.append(Horista("Jonas", "0332", 220, 15))
    except ValueError as e:
        print(f"Erro ao criar funcionário: {e}")

    try:
        funcionarios.append(Mensalista("Lucas", "0412", 4000))
    except ValueError as e:
        print(f"Erro ao criar funcionário: {e}")

    try:
        funcionarios.append(Comissionado("Yasmin", "0742", 3000, 15000, 0.1))
    except ValueError as e:
        print(f"Erro ao criar funcionário: {e}")

    try:
        funcionarios.append(Projetista("Deise", "7468", 900, 5))
    except ValueError as e:
        print(f"Erro ao criar funcionário: {e}")

    for funcionario in funcionarios:
        processar_pagamento(funcionario)

    def simular_pagamento_horistas(horistas):
        dias_trabalhados = 26 
        feriados = [4, 15]  
        fins_de_semana = [5, 6] 

        for funcionario in horistas:
            funcionario.horas_trabalhadas = (dias_trabalhados - len(feriados) - len(fins_de_semana)) * 8
            print(f"Pagamento para {funcionario.nome} com {funcionario.horas_trabalhadas} horas trabalhadas")
            processar_pagamento(funcionario)

    simular_pagamento_horistas([funcionarios[0]])

if __name__ == '__main__':
    main()
