# Sistema de caixa para sorveteria com opções de pagamento
print("Bem-vindo à Sorveteria do João!")

# Menu de produtos
menu = """
Menu:
1. Casquinha - R$ 5.00
2. Sundae - R$ 8.00
3. Milkshake - R$ 10.00
4. Finalizar compra
"""
# Dicionário com preços
precos = {
    1: 5.00,
    2: 8.00,
    3: 10.00
}

total = 0

while True:
    print(menu)
    try:
        opcao = int(input("Escolha o número do produto: "))
        
        if opcao == 4:  # Finalizar compra
            print(f"Total a pagar: R$ {total:.2f}")
            print("\nFormas de pagamento:")
            print("1. Pix")
            print("2. Cartão de Débito")
            print("3. Cartão de Crédito")
            
            pagamento = int(input("Escolha a forma de pagamento: "))
            if pagamento in [1, 2, 3]:
                formas = {1: "Pix", 2: "Cartão de Débito", 3: "Cartão de Crédito"}
                print(f"Pagamento concluído via {formas[pagamento]}.")
                print("Obrigado pela compra! Volte sempre!")
                break
            else:
                print("Forma de pagamento inválida. Tente novamente.")
        elif opcao in precos:
            total += precos[opcao]
            print(f"Produto adicionado! Total até agora: R$ {total:.2f}")
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Por favor, insira um número válido.")
