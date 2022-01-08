select * 
from (
		(
			db_api_pokemon
	        inner join db_api_stat
	        on db_api_pokemon.pokedex_id = db_api_stat.pokedex_id_id
		)
		inner join db_api_multiplier 
	    on db_api_pokemon.pokedex_id = db_api_multiplier.pokedex_id_id
	);
