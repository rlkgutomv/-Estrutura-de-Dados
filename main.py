from fila import Fila
from pilha import Pilha

cliente = [] 
estoque = [] 
vendas = Fila() 
historico = Pilha()


class Cliente:
    def __init__(self, nome, identidadeCliente):
        self.nome = nome
        self.identidadeCliente = identidadeCliente

    def cadastrarCliente(self, nome, identidadeCliente):
        if identidadeCliente in [c.identidadeCliente for c in cliente]:
            print("⚠️ Cliente com ID já cadastrado!")
            return False
        cliente.append(self)
        print("✅ Cliente cadastrado com sucesso!")
        return True


class Produto:
    def __init__(self, nome, identidadeProduto, quantidade, preco): 
        self.nome = nome
        self.identidadeProduto = identidadeProduto
        self.quantidade = quantidade
        self.preco = preco

    def cadastrarProduto(self):
        if self.identidadeProduto in [p.identidadeProduto for p in estoque]:
            print("⚠️ Produto com ID já cadastrado!")
            return False
        estoque.append(self)
        print("📦 Produto cadastrado com sucesso!")
        return True
            
    def RealizarVendas(self, identidadeProduto, quantidade, identidadeCliente):
        if identidadeCliente not in [c.identidadeCliente for c in cliente]:
            print("⚠️ Cliente não cadastrado!")
            return
        for p in estoque:
            if p.identidadeProduto == identidadeProduto:
                if p.quantidade >= quantidade:
                    p.quantidade -= quantidade
                    totalVenda = quantidade * p.preco
                    venda = (identidadeCliente, totalVenda)
                    vendas.enqueue(venda)
                    historico.push(venda)
                    print(f"💸 Venda realizada! Cliente ID {identidadeCliente} → Produto {p.nome} x{quantidade} → Total R${totalVenda:.2f}")
                    return
                else:
                    print("⚠️  Quantidade insuficiente em estoque.")
                    return
        print("❌ Produto não encontrado.")

    def exibirValorTotalEstoque(self):
        totalEstoque = sum(p.quantidade * p.preco for p in estoque)
        print(f"📊 Valor total do estoque: R${totalEstoque:.2f}")

    def exibirTotalVendas(vendas):
        total = sum(venda[1] for venda in vendas.get_items())
        print(f"📊 Valor total de vendas realizadas: R${total:.2f}")

    def pesquisarProduto(self, nomeProduto):
        if not estoque:
            print("📦 Nenhum produto cadastrado.")
            return
        for p in estoque:
            if p.nome.lower() == nomeProduto.lower() or str(p.identidadeProduto) == str(nomeProduto):
                print(f"🔎 Produto encontrado → {p.nome} (ID {p.identidadeProduto}) | {p.quantidade} und. | R${p.preco:.2f}")
                return
        print("❌ Produto não encontrado.")
    
    @staticmethod
    def exibirClientesComValoresTotais():
        if not vendas.get_items():
            print("📊 Nenhuma venda realizada.")
            return
        totais = {}
        for cliente_id, valor in vendas.get_items():
            totais[cliente_id] = totais.get(cliente_id, 0) + valor
        print("===== 🧾 Gastos por Cliente =====")
        for cliente_id, total in totais.items():
            nome = next((c.nome for c in cliente if c.identidadeCliente == cliente_id), "Desconhecido")
            print(f"👤 {nome} (ID {cliente_id}) → R${total:.2f}")

    def salvarDados(self):
        with open("clientes.txt", "w", encoding="utf-8") as f:
            for c in cliente:
                f.write(f"{c.nome},{c.identidadeCliente}\n")
        with open("produtos.txt", "w", encoding="utf-8") as f:
            for p in estoque:
                f.write(f"{p.nome},{p.identidadeProduto},{p.quantidade},{p.preco}\n")
        print("💾 Dados salvos com sucesso!")


def menu():
    while True:
        print("\n================= 📊 MENU ESTOQUE E VENDAS =================")
        print("1️⃣  Cadastrar cliente")
        print("2️⃣  Listar clientes")
        print("3️⃣  Cadastrar produto")
        print("4️⃣  Listar produtos do estoque")
        print("5️⃣  Realizar venda")
        print("6️⃣  Visualizar fila de vendas")
        print("7️⃣  Desfazer última operação")
        print("8️⃣  Exibir valor total do estoque")
        print("9️⃣  Exibir valor total de vendas realizadas")
        print("🔟 Exibir clientes e valores totais gastos")
        print("1️⃣ 1️⃣  Pesquisar produto por nome ou ID")
        print("1️⃣ 2️⃣  Salvar dados no SISTEMA ")
        print("1️ 3️⃣  Sair ❌")
        print("============================================================")
        
        opcao = input("👉 Escolha uma opção: ")

        if opcao == '1':
            nome = input("👤 Nome do cliente: ")
            try:
                identidadeCliente = int(input("🆔 ID do cliente: "))
            except ValueError:
                print("⚠️ ID inválido.")
                continue
            c = Cliente(nome, identidadeCliente)
            c.cadastrarCliente(nome, identidadeCliente)

        elif opcao == '2':
            if not cliente:
                print("📋 Nenhum cliente cadastrado.")
            else:
                print("===== 📋 Lista de Clientes =====")
                for c in cliente:
                    print(f"👤 {c.nome} (ID {c.identidadeCliente})")    

        elif opcao == '3':
            nome = input("📦 Nome do produto: ")
            try:
                identidadeProduto = int(input("🆔 ID do produto: "))
                quantidade = int(input("🔢 Quantidade: "))
                preco = float(input("💸 Preço: "))
            except ValueError:
                print("⚠️ Valores inválidos.")
            else:
                p = Produto(nome, identidadeProduto, quantidade, preco)
                p.cadastrarProduto()

        elif opcao == '4':
            if not estoque:
                print("📦 Nenhum produto cadastrado.")
            else:
                print("===== 📦 Produtos em Estoque =====")
                for p in estoque:
                    print(f"{p.nome} (ID {p.identidadeProduto}) → {p.quantidade} und. - R${p.preco:.2f}")

        elif opcao == '5':
            try:
                quantidade = int(input("🔢 Quantidade: "))
                identidadeCliente = int(input("🆔 ID do cliente: "))
                identidadeProduto = int(input("🆔 ID do produto: "))
            except ValueError:
                print("⚠️ Valores inválidos.")
                continue
            info = Produto("", identidadeProduto, 0, 0)
            info.RealizarVendas(identidadeProduto, quantidade, identidadeCliente)

        elif opcao == '6':
            if not vendas.get_items():
                print("📋 Nenhuma venda realizada.")
            else:
                print("===== 🛒 Fila de Vendas =====")
                for venda in vendas.get_items():
                    print(venda)

        elif opcao == '7':
            if historico.is_empty():
                print("⚠️  Nenhuma venda para desfazer.")
                continue
            ultimaVenda = historico.pop()
            if ultimaVenda in vendas.get_items():
                vendas.get_items().remove(ultimaVenda)
                print(f"↩️ Venda desfeita: {ultimaVenda}")

        elif opcao == '8':
            if not estoque:
                print("📦 Nenhum produto cadastrado.")
            else:
                Produto("", 0, 0, 0).exibirValorTotalEstoque()

        elif opcao == '9':
            if not vendas.get_items():
                print("📊 Nenhuma venda realizada.")
            else:
                Produto.exibirTotalVendas(vendas)

        elif opcao == '10':
            Produto.exibirClientesComValoresTotais()
            
        elif opcao == '11':
            nomeProduto = input("🔎 Digite o nome ou ID do produto: ")
            Produto("", 0, 0, 0).pesquisarProduto(nomeProduto)

        elif opcao == '12':
            Produto("", 0, 0, 0).salvarDados()

        elif opcao == '13':
            print("👋 Saindo do sistema... Até logo!")
            break

        else: 
            print("⚠️  Opção inválida!")


if __name__ == "__main__": 
    menu()
