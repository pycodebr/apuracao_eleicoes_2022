import requests
import json
import pandas as pd

data = requests.get(
    'https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json')

json_data = json.loads(data.content)

candidato = []
partido = []
votos = []
porcentagem = []

pergunta = ''

while pergunta in 'sS':
    for informacoes in json_data['cand']:

        if informacoes['seq'] in ['1', '2', '3', '4']:
            candidato.append(informacoes['nm'])
            votos.append(informacoes['vap'])
            porcentagem.append(informacoes['pvap'])

    df_eleicao = pd.DataFrame(list(zip(candidato, votos, porcentagem)), columns=[
        'Candidato', 'Nº de Votos', 'Porcentagem'
    ])

    print(df_eleicao)
    print()
    pergunta = str(input('Deseja rever os resultados? [S/N] '))
    if pergunta in 'Ss':
        candidato.clear()
        partido.clear()
        votos.clear()
        porcentagem.clear()
