def calcular_preco_com_acrescimo(preco):
    if not isinstance(preco, (int, float)) or preco <= 0:
        raise ValueError("Número inválido, tente novamente.")
    return round(preco * 1.10, 2)


if __name__ == "__main__":
    try:
        preco = float(input("Informe o valor do produto: "))
        novo_preco = calcular_preco_com_acrescimo(preco)
        print(f"Novo valor do produto: {novo_preco:.2f}")
    except Exception:
        print("Número inválido, tente novamente.")
