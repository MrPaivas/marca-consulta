import pandas as pd


from horarios import segunda, terca, quarta, quinta, sexta, sabado

dias = ['SEGUNDA', 'TERÇA', 'QUARTA', 'QUINTA', 'SEXTA', 'SÁBADO']
agenda = "./arquivos/agenda.xlsx"
df = pd.read_excel(agenda)
horario_for = []

for index, row in df.iterrows():
    dia_consultorio = row['SEGUNDA']
    nome_paciente = row['Unnamed: 1']
    nome_estagiario = row['Unnamed: 3']
    telefone_estagiario = row['Unnamed: 4']
    if dia_consultorio in dias:
        continue
    if dia_consultorio in segunda or terca or quarta or quinta or sexta or sabado:
        horario_for.append(dia_consultorio)
        continue
    print(horario_for)
    print(index, dia_consultorio, nome_paciente, nome_estagiario, telefone_estagiario)
