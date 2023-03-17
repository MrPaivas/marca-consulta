import pandas as pd
import pywhatkit


from horarios import segunda, terca, quarta, quinta, sexta, sabado

dias = ['SEGUNDA', 'TERÇA', 'QUARTA', 'QUINTA', 'SEXTA', 'SÁBADO']
agenda = "./arquivos/agenda.xlsx"
df = pd.read_excel(agenda)
salva_hora = []

for index, row in df.iterrows():
    dia_consultorio = row['SEGUNDA']
    nome_paciente = row['Unnamed: 1']
    nome_estagiario = row['Unnamed: 3']
    telefone_estagiario = row['Unnamed: 4']

    if dia_consultorio in segunda:
        salva_hora.append(dia_consultorio)

    pywhatkit.sendwhatmsg_to_group_instantly(telefone_estagiario, f'Oi {nome_estagiario}, foi marcado com sucesso na '
                                                                  f'{salva_hora} no {dia_consultorio} paciente '
                                                                  f'{nome_paciente}')
