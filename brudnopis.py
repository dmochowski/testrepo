def ciagCyfr(x):
    lista = []
    for i in range(x):
        if i%2 == 0:
            i = i+1
            lista.append(i)
        else:
            i = (i+1)*(-1)
            lista.append(i)
    print(lista)
