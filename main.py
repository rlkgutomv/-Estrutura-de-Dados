class cliente:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.listarClientes = []


    def cadastrarCliente(self, nome, id):
        self.nome = nome
        self.id = id

    def listarCliente(self):
        pass

    def sair(self):
        pass

class produto:
    def __init__(self, nome, id, quantidade, preco):
        self.nome = nome
        self.id = id
        self.quantidade = quantidade
        self.preco = preco

    def cadastrarProduto(self, nome, id, quantidade, preco):
        self.nome = nome
        self.id = id
        self.quantidade = quantidade
        self.preco = preco
    
    def listarProduto(self):
    
    def RealizarVendas(self):

    def visualizarFila(self):
        pass

    def desfazerUltimaVenda(self):
        pass

    def exibirTotalEstoque(self):
        pass

    def exbirtotalVendas(self):
        pass

    def pesquisarProduto(self):
        pass

    def carregarDados(self):
        pass

    def menu(self):
        while True:
            print("\n=== Mini Sistema de Estoque e Vendas ===")
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
            print("11. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                
            elif opcao == '2':
                
            elif opcao == '3':
                
            elif opcao == '4':
                
            elif opcao == '5':
                
            elif opcao == '6':
                
            elif opcao == '7':
                
            elif opcao == '8':
               
            elif opcao == '9':
                
            elif opcao == '10':
            
            elif opcao == '11':

            elif opcao == '12':
                
            elif opcao == '13':
            else:
                print("Opção inválida!")

if __name__ == "__main__":


