vetordias = [22174.1664, 24537.6698, 26139.6134,0 , 0, 26742.6612, 0 ,42889.2258, 46251.174, 11191.4722, 0 ,0, 3847.4823, 373.7838, 2659.7563, 48924.2448, 18419.2614,0, 0 ,35240.1826, 43829.1667, 18235.6852, 4355.0662, 13327.1025, 0, 0, 25681.8318, 1718.1221, 13220.495, 8414.61]


MAIOR = 0

MAIOR = max(vetordias)
print('O maior valor é:', MAIOR)

MENOR = 0

MENOR = min(vetordias)
print('O menor valor é:', MENOR)

SOMA = 0

SOMA = sum (vetordias)
print('O total é:', SOMA)

MEDIA = SOMA/21
print('A média mensal é:', MEDIA)

for ACIMAMEDIA in vetordias:  
  if ACIMAMEDIA > MEDIA:  
    MAIOR += 1  
    print (f'Os valores acima da média são:', ACIMAMEDIA)
  elif MENOR < MEDIA:  
    MENOR += 1 





