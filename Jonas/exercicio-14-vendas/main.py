from Conta import Conta
from Funcionario import Funcionario
from HistoricoVendas import HistoricoVendas
from SistemaRH import SistemaRH
from Venda import Venda

def main():
    print("\n----------------Sistema de Vendas----------------")

    historico = HistoricoVendas()
    historico.adicionar_venda(Venda("Açai", 5, 10))
    historico.adicionar_venda(Venda("Morango", 3, 15))
    historico.adicionar_venda(Venda("Maracujá", 4, 25))

    print("Total por produto:", historico.total_por_produto())
    print("Vendas acima de R$ 49,99:")
    for venda in historico.listar_vendas_acima_de(49.99):
        print(f"Produto: {venda.nome}, Quantidade: {venda.quantidade}, Total: R$ {venda.total():.2f}")
        
    print("\n----------------Sistema de RH----------------")
    
    sistema = SistemaRH()
    gerente = Funcionario("Jonas", "Gerente", 5000)
    sistema.adicionar_funcionario(gerente)
    funcionario = Funcionario("João", "Técnico", 3000)
    funcionario = Funcionario("Larissa", "Analista", 4000)
    sistema.adicionar_funcionario(funcionario)

    try:
        sistema.aumentar_salario(usuario=gerente, nome_funcionario="João", incremento=900)
        sistema.aumentar_salario(usuario=funcionario, nome_funcionario="Larissa", incremento=800)
    except PermissionError as e:
        print(e)

    print("\n----------------Conta----------------")

    conta = Conta()
    conta.adicionar_transacao("Depósito", 1000)
    conta.adicionar_transacao("Saque", 200)
    conta.adicionar_transacao("Saque", 150)

    print("Depósitos Realizados:", conta.filtrar_transacoes_por_tipo("Depósito"))
    print("Transações de Saque:", conta.filtrar_transacoes_por_tipo("Saque"))
    
    conta.aplicar_taxa(10)
    print("Transações após aplicar taxa:", conta._transacoes)

if __name__ == "__main__":
    main()
