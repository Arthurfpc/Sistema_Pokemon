class PokemonDAO():
    def __init__(self, instancia_pokemon):
        self._programacao_json = {}
        self.preenche_valores_json(instancia_pokemon)
    
    def preenche_valores_json(self, instancia):
        self._programacao_json['id'] = instancia.id
        self._programacao_json['Nome'] = instancia.nome
        self._programacao_json['Tipo'] = instancia.tipo
        self._programacao_json['Evolucoes'] = instancia.evolucoes
        self._programacao_json['Descricao'] = instancia.descricao
  
    def __str__(self):
        return str(self._programacao_json)