equipos_premier_league = {"Manchester United", "Liverpool", "Chelsea", "Manchester City", "Arsenal"}
equipos_la_liga = {"Real Madrid", "Barcelona", "Atletico Madrid", "Sevilla", "Valencia"}
equipos_serie_a = {"Juventus", "AC Milan", "Inter de Milán", "Napoli", "Roma"}
equipo = "Liverpool"
if equipo in equipos_premier_league:
    print(f"{equipo} juega en la Premier League.")
else:
    print(f"{equipo} no juega en la Premier League.")
equipos_italianos = {"Juventus", "AC Milan", "Inter de Milán", "Napoli", "Roma", "Lazio"}
equipos_en_comun = equipos_premier_league.intersection(equipos_italianos)
print("Equipos que juegan en ambas ligas:", equipos_en_comun)
equipos_en_premier_no_en_italiana = equipos_premier_league.difference(equipos_italianos)
print("Equipos en la Premier League pero no en la Serie A:", equipos_en_premier_no_en_italiana)
equipos_en_italiana_no_en_premier = equipos_italianos.difference(equipos_premier_league)
print("Equipos en la Serie A pero no en la Premier League:", equipos_en_italiana_no_en_premier)
es_subconjunto = equipos_serie_a.issubset(equipos_italianos)
print("¿La Serie A es subconjunto de equipos italianos?", es_subconjunto)
