def FIBONACCI(NUM):
    ANT, PROX = 0, 1
    while PROX < NUM:
        ANT, PROX = PROX, ANT + PROX
    if PROX == NUM:
        return True
    else:
        return False

N = int(input("Digite um número inteiro: "))
if FIBONACCI(N):
    print(f"{N} pertence à sequência de Fibonacci")
else:
    print(f"{N} Não pertence à sequência de Fibonacci")

