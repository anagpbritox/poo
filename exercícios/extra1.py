# EXERCICIO EXTRA - MANIPULACAO DE COLECOES




def remove_repeticao(lista):
    c = []
    for elemento in lista:
        if elemento not in c:
            c.append(elemento)

    return c



# principal
a = [0, 1, 2, 3, 4, 5, 5, 0]
b = [4, 5, 6, 7, 8, 9, 9, 4]


print(a, b)

a_sem_repeticao = remove_repeticao(a)
b_sem_repeticao = remove_repeticao(b)

print(a_sem_repeticao, b_sem_repeticao)