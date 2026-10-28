grafo = {
    'SP': {'RJ': 300, 'BH': 400, 'CWB': 350},
    'RJ': {'SP': 300, 'BSB': 500},
    'BH': {'SP': 400, 'BSB': 450},
    'BSB': {'RJ': 500, 'BH': 450},
    'CWB': {'SP': 350},
}

def CalcularCustoRota(matriz, rota, tamanhoRota):
    custo_total = 0

    for i in range(tamanhoRota - 1):
        origem = rota[i]
        destino = rota[i + 1]

        if origem in grafo and destino in grafo[origem]:
            custo_total += grafo[origem][destino]
        else:
            print(f"Erro: Não existe voo direto de {origem} para {destino}!")
            return None



    return custo_total

minha_rota = ['CWB', 'SP', 'RJ', 'BSB']

tamanho_minha_rota = len(minha_rota)

custo = CalcularCustoRota(grafo, minha_rota, tamanho_minha_rota)

print(custo)
