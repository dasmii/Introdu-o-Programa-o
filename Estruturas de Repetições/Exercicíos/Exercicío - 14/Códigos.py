# Usando o loop for
for numero in range(1000, 2001):
    if numero % 11 == 5:
        print(f'O número é {numero}')

        # Usando o loop while
        numero = 1000
        while numero <= 2000:
            if numero % 11 == 5:
                print(f'O número é {numero}')
            numero += 1  # Incrementa o número