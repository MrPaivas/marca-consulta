import pandas as pd
import pywhatkit


from horarios import segunda, terca, quarta, quinta, sexta, sabado

dias = ['SEGUNDA', 'TERÇA', 'QUARTA', 'QUINTA', 'SEXTA', 'SÁBADO']
agenda = "./arquivos/agenda.xlsx"
df = pd.read_excel(agenda)
salva_hora = []


def manda_o_zap(tel, nome, hora, local, paciente):
    pywhatkit.sendwhatmsg_to_group_instantly(
                                            tel, f'Oi {nome}, foi marcado com sucesso na '
                                            f'{hora} no {local} paciente {paciente}')


for index, row in df.iterrows():
    dia_consultorio = row['SEGUNDA']
    nome_paciente = row['Unnamed: 1']
    nome_estagiario = row['Unnamed: 3']
    telefone_estagiario = row['Unnamed: 4']

    if nome_estagiario == 'ESTAGIÁRIO':
        salva_hora.append(dia_consultorio)
        continue
    elif nome_paciente == "":
        continue
    print(index, dia_consultorio, nome_paciente, nome_estagiario, telefone_estagiario)
    #else:
        #manda_o_zap(telefone_estagiario, nome_estagiario, salva_hora[-1], dia_consultorio, nome_paciente)


