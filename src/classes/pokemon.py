class Pokemon:
    def __init__(self, id, nome, tipo, evolucoes, descricao):
        self.__id = int(id)
        self.__nome = str(nome)
        self.__tipo = str(tipo)
        self.__evolucoes = str(evolucoes)
        self.__descricao = str(descricao)

    @property
    def nome(self):
        return self.__nome
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def evolucoes(self):
        return self.__evolucoes
    
    @property
    def descricao(self):
        return self.__descricao

    def __str__(self):
        return f''' 
        Nome: {self.__nome}
        Tipo: {self.__tipo}
        Evoluções: {self.__evolucoes}
        Descrição: {self.__descricao}
        '''
novopokemon = Pokemon(1, "Greninja", "Água", "Frog", "É ISSO")
print(novopokemon)