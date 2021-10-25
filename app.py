from src.classes.pokemon import Pokemon
from src.dao.pokemon_dao import PokemonDAO
from src.bd.bd_connection import bd
from flask import Flask, jsonify, request

implementa_descricao= "Greninja é a forma evoluída de Frogadier e a forma final de Froakie, Greninja é um mestre de rapidez e furtividade."

#novo= Pokemon(2, "Greninja", "Água e Sombrio", ["Frokie, Frogadier e Greninja"],implementa_descricao)
#nova_dao = PokemonDAO(novo)
#bd.insert_in_BD(nova_dao._programacao_json)
#<div>Eu estou online! - Hello World<div/>
#return f'''<html>
#<h1>Pokémon</h1>
    #<div>Nome: {novo_pokemon.nome}<div/>
    #<div>Tipo: {novo_pokemon.tipo}<div/>
    #<div>Evoluções: {novo_pokemon.evolucoes}<div/>
    #<div>Descrição: {novo_pokemon.descricao}<div/>

app = Flask(__name__)
@app.route('/', methods=['GET']) 
def home():
    novo_pokemon= Pokemon(2, "Greninja", "Água e Sombrio", ["Frokie, Frogadier e Greninja"],implementa_descricao)
    novo_pokemon2= Pokemon(1, "Teste", "Pedra", ["teste, teste"],"1234")
    return f'''<html>
    <h1>Pokémon</h1>
        <table class=" aligncenter" style="height: 89px;" border="1" width="195">
            <tbody>
                <tr>
                    <th style="text-align: left;">Nome</th>
                    <th style="text-align: left;">Tipo</th>
                    <th style="text-align: left;">Evoluções</th>
                    <th style="text-align: left;">Descrição</th>
                </tr>
                <tr>
                    <td>{novo_pokemon.nome}</td>
                    <td>{novo_pokemon.tipo}</td>
                    <td>{novo_pokemon.evolucoes}</td>
                    <td>{novo_pokemon.descricao}</td>
                </tr>
                <tr>
                    <td>{novo_pokemon2.nome}</td>
                    <td>{novo_pokemon2.tipo}</td>
                    <td>{novo_pokemon2.evolucoes}</td>
                    <td>{novo_pokemon2.descricao}</td>
                </tr>
    </html>'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='3001')
