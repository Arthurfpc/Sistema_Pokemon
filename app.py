from src.classes.pokemon import Pokemon
from src.dao.pokemon_dao import PokemonDAO

novo= Pokemon(1, "teste", "teste", "124","teste")
nova_dao = PokemonDAO(novo)
print(nova_dao)
