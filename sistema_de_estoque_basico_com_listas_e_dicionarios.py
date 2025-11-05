estoque = []
lista_preco = []
for i in range(3):
    dicionario = {}
    n=str(input(f'digite o {i + 1}º nome: '))
    p=float(input(f'digite o preço do {n} : '))
    e=int(input(f'digite a quantidade no estoque do {n} : '))
    dicionario['nome'] = n
    dicionario['preço'] = p
    lista_preco.append(p)
    dicionario['estoque'] = e
    estoque.append(dicionario)
for i in range(3):
    print('nome =',estoque[i] ['nome']  ,' | preço =', estoque[i] ['preço'])
    print()
maior_p = max(lista_preco)
menor_p = min(lista_preco)
print()
print('o maior preço e de: ',maior_p)
print()
print('o menor preço e de: ',menor_p)
print()
for i in range(3):
    total = 0
    total = estoque[i]['preço'] * estoque[i]['estoque']
    print('se verder todo o estoque de ',estoque[i]['nome'],'o valor total da venda vai ser de:',total)
    print()
for i in range(3):
    if estoque[i]['estoque']< 5:
        print('o',estoque[i]['nome'],' esta  com o estoque baixo')
    

  

    
    