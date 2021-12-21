troco = 28

moedas = [1, 2, 8, 14, 25]
qtd_moedas = len(moedas)

m = [[None for i in range(troco + 1)] for j in range(qtd_moedas)]

for i in range(qtd_moedas):
    for j in range(troco+1):
        print(m[i][j])
    

def resolve_troco(v_restante: int, ind_moeda_atual: int=0):
    print(v_restante)
    if v_restante == 0:
        return 0
    if v_restante > 0 and ind_moeda_atual == qtd_moedas:
        return float("inf")
    if v_restante < 0:
        return float("inf")
    if m[ind_moeda_atual][v_restante] is None:
        pego_a_moeda = 1 + resolve_troco(v_restante - moedas[ind_moeda_atual], ind_moeda_atual)
        nao_pego_moeda = resolve_troco(v_restante, ind_moeda_atual + 1)
        m[ind_moeda_atual][v_restante] = min(pego_a_moeda, nao_pego_moeda)
    return m[ind_moeda_atual][v_restante]

print("A quantidade mínima de moedas para " + str(troco) + " são "+str(resolve_troco(troco)) + " moeda(s)")
