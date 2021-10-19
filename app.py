from src.classes.pokemon import Pokemon
from src.dao.pokemon_dao import PokemonDAO
from src.bd.bd_connection import bd

implementa_descricao= "Greninja é a forma evoluída de Frogadier e a forma final de Froakie, Greninja é um mestre de rapidez e furtividade."
novo= Pokemon(1, "Greninja", "Água e Sombrio", "Frokie, Frogadier e Greninja ",implementa_descricao)
nova_dao = PokemonDAO(novo)
bd.insert_in_BD(nova_dao._programacao_json)
