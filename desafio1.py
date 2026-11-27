from mapa import mapa_romenia, heuristica_bucareste

# desafio1 - 1
print('Cidades que tem 1 estrada apenas:')
print()
for cidade in mapa_romenia:
    if len(mapa_romenia[cidade]) == 1:
        print(f'{cidade}: {mapa_romenia[cidade]}')

# desafio1 - 2
print()
print('Cidades com h(n) menor que 200 km:')
print()
for cidade in heuristica_bucareste:
    if heuristica_bucareste[cidade] < 200:
        print(f'{cidade}: {heuristica_bucareste[cidade]} km')

# desafio1 - 3
print()
print('Estrada mais longa: ')
print()
max_custo = 0
cidade_origem = ''
cidade_destino = ''

for cidade in mapa_romenia:
    for vizinho, custo in mapa_romenia[cidade]:
        if custo > max_custo:
            max_custo = custo
            cidade_origem = cidade
            cidade_destino = vizinho

print(f'De {cidade_origem} até {cidade_destino}: {max_custo} km')