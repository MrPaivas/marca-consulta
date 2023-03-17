segunda = []
terca = []
quarta = []
quinta = []
sexta = []
sabado = []

modelo_segunda = 'SEGUNDA '
modelo_terca = 'TERÇA '
modelo_quarta = 'QUARTA '
modelo_quinta = 'QUINTA '
modelo_sexta = 'SEXTA '
modelo_sabado = 'SÁBADO '
hora = 'h'

for i in range(8, 22):
    segunda.append(modelo_segunda+str(i)+hora)
    terca.append(modelo_terca+str(i)+hora)
    quarta.append(modelo_quarta+str(i)+hora)
    quinta.append(modelo_quinta+str(i)+hora)
    sexta.append(modelo_sexta+str(i)+hora)
    sabado.append(modelo_sabado+str(i)+hora)

print(segunda, terca, quarta, quinta, sexta, sabado)