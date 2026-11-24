class No_arvore_avl:
    def __init__(self, valor, post=None):
        self.valor = valor
        self.posts = []
        if post is not None:
            self.posts.append(post)
        self.esq = None
        self.dir = None
        self.altura = 1

class ArvoreAVLSocial:

    def __init__(self):
        self.raiz = None
        self.total_posts = 0

    def social_obter_altura(self, no):
        if no is None:
            return 0
        return no.altura

    def social_obter_fator_balanceamento(self, no):
        if no is None:
            return 0
        return self.social_obter_altura(no.esquerda) - self.social_obter_altura(no.direita)

    def social_atualizar_altura(self, no):
        alt_esq = self.social_obter_altura(no.esquerda)
        alt_dir = self.social_obter_altura(no.direita)
        if alt_esq > alt_dir:
            no.altura = 1 + alt_esq
        else:
            no.altura = 1 + alt_dir

    def social_rotacao_direita(self, y):
        x = y.esquerda
        t2 = x.direita

        x.direita = y
        y.esquerda = t2

        self.social_atualizar_altura(y)
        self.social_atualizar_altura(x)

        return x

    def social_rotacao_esquerda(self, x):
        y = x.direita
        t2 = y.esquerda

        y.esquerda = x
        x.direita = t2

        self.social_atualizar_altura(x)
        self.social_atualizar_altura(y)

        return y

    def social_inserir(self, valor, post):
        self.raiz = self.social_inserir_recursivo(self.raiz, valor, post)
        self.total_posts += 1

    def social_inserir_recursivo(self, no, valor, post):
        if no is None:
            return No_arvore_avl(valor, post)

        if valor == no.valor:
            no.posts.append(post)
            return no
        elif valor < no.valor:
            no.esquerda = self.social_inserir_recursivo(no.esquerda, valor, post)
        else:
            no.direita = self.social_inserir_recursivo(no.direita, valor, post)

        self.social_atualizar_altura(no)
        fb = self.social_obter_fator_balanceamento(no)

        if fb > 1 and valor < no.esquerda.valor:
            return self.social_rotacao_direita(no)


        if fb < -1 and valor > no.direita.valor:
            return self.social_rotacao_esquerda(no)


        if fb > 1 and valor > no.esquerda.valor:
            no.esquerda = self.social_rotacao_esquerda(no.esquerda)
            return self.social_rotacao_direita(no)


        if fb < -1 and valor < no.direita.valor:
            no.direita = self.social_rotacao_direita(no.direita)
            return self.social_rotacao_esquerda(no)

        return no

    def social_buscar_intervalo(self, data1, data2):
        resultado = []
        if data1 > data2:
            return resultado
        self.social_buscar_intervalo_recursivo(self.raiz, data1, data2, resultado)
        return resultado

    def social_buscar_intervalo_recursivo(self, no, data1, data2, resultado):
        if no is None:
            return

        if no.valor > data1:
            self.social_buscar_intervalo_recursivo(no.esquerda, data1, data2, resultado)

        if data1 <= no.valor <= data2:
            for p in no.posts:
                resultado.append(p)

        if no.valor < data2:
            self.social_buscar_intervalo_recursivo(no.direita, data1, data2, resultado)

    def social_contar_nos(self, no=None):
        if no is None:
            no = self.raiz
        if no is None:
            return 0
        total = 1
        if no.esquerda is not None:
            total += self.social_contar_nos(no.esquerda)
        if no.direita is not None:
            total += self.social_contar_nos(no.direita)
        return total

    def social_verificar_avl(self, no=None):
        if no is None:
            no = self.raiz
        if no is None:
            return True
        fb = self.social_obter_fator_balanceamento(no)
        if fb < -1 or fb > 1:
            return False
        esq_ok = True if no.esquerda is None else self.social_verificar_avl(no.esquerda)
        dir_ok = True if no.direita is None else self.social_verificar_avl(no.direita)
        return esq_ok and dir_ok