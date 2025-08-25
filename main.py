from fila import Fila

cliente = []
estoque = []
vendas = Fila()



class Cliente:
    def __init__(self, nome, identidade):
        self.nome = nome
        self.id = identidade


    def cadastrarCliente(self, nome, identidade):
        self.nome = nome
        self.id = identidade
        cliente.append(self)

    def listarCliente(self):
        if cliente == None:
            print("Nenhum cliente cadastrado.")
        else:
            for c in cliente:
                print(f"Nome: {c.nome}, ID: {c.identidade}")
    
    def exbirClientesComValoresTotais(self):
        pass

    def sair(self):
        pass

class Produto:
    def __init__(self, nome, identidade, quantidade, preco): #GUSTAVO
        self.nome = nome
        self.id = identidade
        self.quantidade = quantidade
        self.preco = preco

    def cadastrarProduto(self, nome, identidade, quantidade, preco): #GUSTAVO
        self.nome = nome
        self.id = identidade
        self.quantidade = quantidade
        self.preco = preco
    
    def listarProduto(self): 
        pass
    
    def RealizarVendas(self):
        pass

    def visualizarFilaDeVendas(self):
        pass

    def desfazerUltimaVenda(self):
        pass

    def exibirValorTotalEstoque(self):
        pass

    def exbirTotalVendas(self):
        pass

    def pesquisarProduto(self):
        pass

    def carregarDados(self):
        pass
def menu():
    while True:
        print("===== MENU ESTOQUE E VENDAS =====")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Cadastrar produto")
        print("4. Listar produtos do estoque")
        print("5. Realizar venda")
        print("6. Visualizar fila de vendas")
        print("7. Desfazer última operação (pilha)")
        print("8. Exibir valor total do estoque")
        print("9. Exibir valor total de vendas realizadas")
        print("10. Exibir clientes e valores totais gastos")
        print("11. Pesquisar produto por nome ou ID")
        print("12. Carregar dados de clientes e produtos de arquivos")
        print("13. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            pass

        elif opcao == '2':
            pass

        elif opcao == '3':
            pass

        elif opcao == '4':
            pass

        elif opcao == '5':
            pass

        elif opcao == '6':
            pass

        elif opcao == '7':
            pass

        elif opcao == '8':
            pass

        elif opcao == '9':
            pass

        elif opcao == '10':
            pass

        elif opcao == '11':
            pass

        elif opcao == '12':
            pass

        elif opcao == '13':
            pass

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()


