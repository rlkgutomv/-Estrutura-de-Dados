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

        if opcao == '1': #Pedro Renosto
            nome = input("Nome do cliente: ")
            identidade = input("ID do cliente: ")
            c = Cliente(nome, identidade)
            c.cadastrarCliente()

        elif opcao == '2': #Pedro Renosto
            Cliente.listarCliente()

        elif opcao == '3': #Pedro Renosto
            nome = input("Nome do produto: ")
            identidade = input("ID do produto: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            p = Produto(nome, identidade, quantidade, preco)
            p.cadastrarProduto()

        elif opcao == '4': #Pedro Renosto
            Produto.listarProduto()

        elif opcao == '5': #Pedro Renosto
            id_produto = input("ID do produto: ")
            qtd = int(input("Quantidade: "))
            id_cliente = input("ID do cliente: ")
            Produto.realizarVenda(id_produto, qtd, id_cliente)

        elif opcao == '6': #Pedro Renosto
            Produto.visualizarFilaDeVendas()

        elif opcao == '7': #Pedro Renosto
            Produto.desfazerUltimaVenda()

        elif opcao == '8': #Pedro Renosto
            Produto.exibirValorTotalEstoque()

        elif opcao == '9': #Pedro Renosto
            Produto.exibirTotalVendas()

        elif opcao == '10': #Pedro Renosto
            Produto.exibirClientesComValoresTotais()

        elif opcao == '11': #Pedro Renosto
            valor = input("Digite o nome ou ID do produto: ")
            Produto.pesquisarProduto(valor)

        elif opcao == '12': #Pedro Renosto
            Produto.carregarDados()

        elif opcao == '13': #Pedro Renosto
            print("Saindo...")
            break

        else: #Pedro Renosto
            print("Opção inválida!")

if __name__ == "__main__": #Pedro Renosto
    menu()



