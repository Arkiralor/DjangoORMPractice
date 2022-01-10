select * from db_api_pokemon where pokedex_id = 88;
select * from db_api_stat where pokedex_id_id = 259;
select * from db_api_multiplier where pokedex_id_id = 259;

select db_api_pokemon.name, db_api_pokemon.pokedex_id from db_api_pokemon where is_legendary = true;