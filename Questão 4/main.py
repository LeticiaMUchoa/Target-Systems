SP = float(67.83643)

RJ = float(36.67866)

MG = float(29.22988)

ES = float(27.16548)

OUTRO = float(19.84953)

TOTAL = float(SP + RJ + MG + ES + OUTRO)

print('O valor total', TOTAL)

PORCENTAGEMSP = ((SP/TOTAL)*100)
PORCENTAGEMRJ = ((RJ/TOTAL)*100)
PORCENTAGEMMG = ((MG/TOTAL)*100)
PORCENTAGEMES = ((ES/TOTAL)*100)
PORCENTAGEMOUTRO = ((OUTRO/TOTAL)*100)

print('\nPorcentagem de SP {}'.format(PORCENTAGEMSP))

print('\nPorcentagem de RJ {}'.format(PORCENTAGEMRJ))

print('\nPorcentagem de MG {}'.format(PORCENTAGEMMG))

print('\nPorcentagem de ES {}'.format(PORCENTAGEMES))

print('\nPorcentagem de OUTRO {}'.format(PORCENTAGEMOUTRO))