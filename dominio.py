class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor):
        if self._valor_valido(valor):
            raise ValueError("Não pode propor um valor maior que a carteira!!!")
        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira

    def _valor_valido(self, valor):
        return valor <= self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []
        self.maior_lance = 0.0
        self.menor_lance = 0.0

    def propoe(self, lance: Lance):
        if self._lance_eh_valido(lance):
            if not self._tem_lances:
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor
            self.__lances.append(lance)
        else:
            raise ValueError("O mesmo usuário não pode propor dois lances seguidos ou maior que o último!!!")

    @property
    def lances(self):
        return self.__lances[:]

    def _tem_lances(self):
        return self.__lances

    def _usuarios_diferentes(self, lance):
        return self.__lances[-1].usuario != lance.usuario

    def _valor_maior_que_lance_anterior(self, lance):
        return lance.valor > self.__lances[-1].valor

    def _lance_eh_valido(self, lance):
        return not self._tem_lances or self._usuarios_diferentes(lance) and self._valor_maior_que_lance_anterior(lance)
