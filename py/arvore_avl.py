class No_arvore_avl:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None
        self.altura = 1

def altura(no):
    return 0 if no is None else no.altura

def atualizar_altura(no):
    no.altura = 1 + max(altura(no.esq), altura(no.dir))

def fator(no):
    return altura(no.esq) - altura(no.dir)

def rotacao_esquerda(z):
    y = z.dir
    z.dir = y.esq
    y.esq = z
    atualizar_altura(z)
    atualizar_altura(y)
    return y 

def rotacao_direita(z):
    y = z.esq
    z.esq = y.dir
    y.dir = z
    atualizar_altura(z)
    atualizar_altura(y)
    return y

def inserir(no, valor):
    if no is None:
        return No_arvore_avl(valor)
    if valor < no.valor:
        no.esq = inserir(no.esq, valor)
    else:
        no.dir = inserir(no.dir, valor)
    atualizar_altura(no)
    red = fator(no)
    if red > 1:
        if valor > no.esq.valor:
            no.esq = rotacao_esquerda(no.esq)
        return rotacao_direita(no)
    if red < -1:
        if valor > no.esq.valor:
            no.dir = rotacao_direita(no.dir)
        return rotacao_esquerda(no)
    return no
    