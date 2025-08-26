from fila import Fila

cliente = []
estoque = []
vendas = Fila()



class Cliente:
    def __init__(self, nome, identidade):
        self.nome = nome
        self.identidade = identidade


    def cadastrarCliente(self, nome, identidade):
        self.nome = nome
        self.identidade = identidade
        cliente.append(self)

class Produto:
    def __init__(self, nome, identidade, quantidade, preco): #GUSTAVO
        self.nome = nome
        self.identidade = identidade
        self.quantidade = quantidade
        self.preco = preco

    def cadastrarProduto(self): #GUSTAVO
        if self.identidade in [p.identidade for p in estoque]:
            print("Produto com ID já cadastrado.")
            return False
        else:
            estoque.append(self)
            print("Produto cadastrado com sucesso!")
            return True
    
    def RealizarVendas(self, id_produto, qtd, id_cliente):
        if estoque == None:
            print("Nenhum produto cadastrado.")
        else:
            for p in estoque:
                if p.identidade == id_produto:
                    if p.quantidade >= qtd:
                        p.quantidade -= qtd
                        total_venda = qtd * p.preco
                        vendas.enqueue((p.nome, qtd, total_venda, id_cliente))
                        print(f"Venda realizada: {qtd} unidades de {p.nome} para o cliente {id_cliente}. Total: R${total_venda:.2f}")
                    else:
                        print(f"Quantidade insuficiente em estoque para o produto {p.nome}.")
                    return

    def visualizarFilaDeVendas(self):
        if vendas == None:
            print("Nenhuma venda realizada.")
        else:
            print(f"Fila de vendas: {vendas}")

    def desfazerUltimaVenda(self):
            vendas.dequeue()

    def exibirValorTotalEstoque(self):
        totalEstoque = sum(p.quantidade * p.preco for p in estoque)
        print(f"Valor total do estoque: R${totalEstoque:.2f}")

    def exbirTotalVendas(self):
        totalVendas = sum(venda[2] for venda in vendas.get_items())
        print(f"Valor total de vendas realizadas: R${totalVendas:.2f}")

    def pesquisarProduto(self, nomeProduto):
        if estoque == None:
            print("Nenhum produto cadastrado.")
        else:
            for p in estoque:
                if p.nome == nomeProduto or p.id == nomeProduto:
                    print(f"Produto encontrado: Nome: {p.nome}, ID: {p.id}, Quantidade: {p.quantidade}, Preço: R${p.preco:.2f}")
                    return
            print("Produto não encontrado.")

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
            nome =input("Nome do cliente: ")
            try:
                identidade = int(input("ID do cliente: "))
                
            except ValueError:
                print("ID inválido. Por favor, insira um valor numérico.")
            c = Cliente(nome, identidade)
            c.cadastrarCliente(nome, identidade)

        elif opcao == '2':
            if not cliente:
             print("Nenhum cliente cadastrado.")
            else:
                for c in cliente:
                    print(f"Nome: {c.nome}, ID: {c.identidade}")    


        elif opcao == '3':
            nome = input("Nome do produto: ")
            try:
                identidade = int(input("ID do produto: "))
            except ValueError:
                print("ID inválido. Por favor, insira um valor numérico.")
                continue
            try:
                quantidade = int(input("Quantidade: "))
            except ValueError:
                print("Quantidade inválida. Por favor, insira um valor numérico.")
                continue
            try:
                preco = float(input("Preço: "))
            except ValueError:
                print("Preço inválido. Por favor, insira um valor numérico.")
                continue

            p = Produto(nome, identidade, quantidade, preco)
            p.cadastrarProduto()
                

        elif opcao == '4': #Pedro Renosto
            if estoque == None:
                print("Nenhum produto cadastrado.")
            else:
                for p in estoque:
                    print(f"Nome: {p.nome}, ID: {p.id}, Quantidade: {p.quantidade}, Preço: R${p.preco:.2f}")

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
            nomeProduto = input("Digite o nome ou ID do produto: ")
            Produto.pesquisarProduto(nomeProduto)

        elif opcao == '12': #Pedro Renosto
            Produto.carregarDados()

        elif opcao == '13': #Pedro Renosto
            print("Saindo...")
            exit()

        else: #Pedro Renosto
            print("Opção inválida!")

if __name__ == "__main__": #Pedro Renosto
    menu()



