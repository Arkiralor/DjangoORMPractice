select db_api_pokemon.pokedex_id, 
db_api_pokemon.name, 
db_api_stat.attack,
db_api_stat.special_atk,
db_api_pokemon.type_1,
db_api_pokemon.type_2,
db_api_stat.defense,
db_api_multiplier.against_fight,
db_api_pokemon.generation
from (
		(
			db_api_pokemon
	        inner join db_api_stat
	        on db_api_pokemon.pokedex_id = db_api_stat.pokedex_id_id
		)
		inner join db_api_multiplier 
	    on db_api_pokemon.pokedex_id = db_api_multiplier.pokedex_id_id
	)
where (db_api_pokemon.generation = 2 or db_api_pokemon.generation = 3) 
and db_api_multiplier.against_fight > 1;