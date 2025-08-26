from fila import Fila
from pilha import Pilha

cliente = [] 
estoque = [] 
vendas = Fila() 



class Cliente:
    def __init__(self, nome, identidadeCliente):#Certo
        self.nome = nome
        self.identidadeCliente = identidadeCliente


    def cadastrarCliente(self, nome, identidadeCliente):
        self.identidadeCliente = identidadeCliente
        self.nome = nome
        if self.identidadeCliente in [c.identidadeCliente for c in cliente]:
            print("Cliente com ID já cadastrado.")
            return False
        else:
            cliente.append(self)
            print("Cliente cadastrado com sucesso!")
            return True

class Produto:
    def __init__(self, nome, identidadeProduto, quantidade, preco): 
        self.nome = nome
        self.identidadeProduto = identidadeProduto
        self.quantidade = quantidade
        self.preco = preco

    def cadastrarProduto(self): #certo
        if self.identidadeProduto in [p.identidade for p in estoque]:
            print("Produto com ID já cadastrado.")
            return False
        else:
            estoque.append(self)
            print("Produto cadastrado com sucesso!")
            
    
    def RealizarVendas(self, identidadeProduto, quantidade, identidadeCliente):
        if identidadeCliente not in [c.identidadeCliente for c in cliente]:
                print("Cliente não cadastrado. Cadastre o cliente antes de realizar uma venda.")
                return
        for p in estoque:
            if p.identidadeProduto == identidadeProduto:
                if p.quantidade >= quantidade:
                    p.quantidade -= quantidade
                    totalVenda = quantidade * p.preco
                    vendas.enqueue((identidadeCliente,totalVenda))
                    print(f"Venda realizada: Cliente ID {identidadeCliente}, Produto ID {identidadeProduto}, Quantidade {quantidade}, Total R${totalVenda:.2f}")
                    return
                else:
                    print("Quantidade insuficiente em estoque.")
                    return
        print("Produto não encontrado.")

    def desfazerUltimaVenda(self):
            vendas.dequeue()

    def exibirValorTotalEstoque(self):
        totalEstoque = sum(p.quantidade * p.preco for p in estoque)
        print(f"Valor total do estoque: R${totalEstoque:.2f}")

    def exibirTotalVendas(vendas):
        total = sum(venda[1] for venda in vendas.get_items())
        print(f"Valor total de vendas realizadas: R${total:.2f}")

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
        print("14. Sair")
        print("==================================")
        opcao = input("Escolha uma opção: ")
        print("==================================")

        if opcao == '1':  #Certo
            nome = input("Nome do cliente: ")
            try:
                identidadeCliente = int(input("ID do cliente: "))
            except ValueError:
                print("ID inválido. Por favor, insira um valor numérico.")
                continue
            c = Cliente(nome, identidadeCliente)
            c.cadastrarCliente(nome, identidadeCliente)

        elif opcao == '2': 
            if not cliente:
             print("Nenhum cliente cadastrado.")
            else:
                for c in cliente:
                    print(f"Nome: {c.nome}, ID: {c.identidadeCliente}")    


        elif opcao == '3':
            nome = input("Nome do produto: ")
            try:
                identidadeProduto = int(input("ID do produto: "))
                quantidade = int(input("Quantidade: "))
                preco = float(input("Preço: "))
            except ValueError:
                print("Erro: insira valores numéricos válidos para ID, quantidade e preço.")
                
            else:
                p = Produto(nome, identidadeProduto, quantidade, preco)
                p.cadastrarProduto()
                

        elif opcao == '4':
            if not estoque:
                print("Nenhum produto cadastrado.")
            else:
                for p in estoque:
                    print(f"Nome: {p.nome}, ID: {p.identidadeProduto}, Quantidade: {p.quantidade}, Preço: R${p.preco:.2f}")

        elif opcao == '5':
            try:
                quantidade = int(input("Digite a quantidade: "))
                identidadeCliente = int(input("Digite o ID do cliente: "))
                identidadeProduto = int(input("Digite o ID do produto: "))
            except ValueError:
                print("Erro: insira valores numéricos válidos para ID e quantidade.")
                continue
            info = Produto("", identidadeProduto, 0, 0)
            info.RealizarVendas(identidadeProduto, quantidade, identidadeCliente)
            

        elif opcao == '6':
            if not vendas.get_items():
                print("Nenhuma venda realizada.")
            else:
                print("Fila de vendas (Cliente ID, Valor da Venda):")
                for venda in vendas.get_items():
                    print(venda)

        elif opcao == '7': 
            Produto.desfazerUltimaVenda() #GUSTAVO

        elif opcao == '8': 
            if not estoque:
                print("Nenhum produto cadastrado.")
            else:
                totalEstoque = Produto("", 0, 0, 0)
                Produto.exibirValorTotalEstoque(totalEstoque) #LUIS

        elif opcao == '9':
            if not vendas:
                print("Nenhuma venda realizada.")
            else:
                Produto.exibirTotalVendas(vendas) #LUIS

        elif opcao == '10': 
            Produto.exibirClientesComValoresTotais() #PEDRO

        elif opcao == '11': 
            nomeProduto = input("Digite o nome ou ID do produto: ") #PEDRO
            Produto.pesquisarProduto(nomeProduto)

        elif opcao == '12': #GUSTAVO
            Produto.carregarDados()

        elif opcao == '14': #LUIS
            print("Saindo...")
            exit()

        else: 
            print("Opção inválida!")

if __name__ == "__main__": 
    menu()



