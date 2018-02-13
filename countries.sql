select countries.name, languages.language, languages.percentage from countries
join languages on countries.id = languages.country_id
where languages.language = "Slovene"
order by languages.percentage desc;

select countries.name as counrty_name, count(cities.name) as number_of_cities from countries
join cities on countries.id = cities.country_id
group by countries.id
order by count(cities.name) desc;

select cities.name, cities.population from countries
join cities on countries.id = cities.country_id
where countries.name = "Mexico" and cities.population > 500000
order by cities.population desc;

select countries.name, languages.language, languages.percentage from countries
join languages on countries.id = languages.country_id
where languages.percentage > 89
group by countries.id
order by languages.percentage desc;

select countries.name, countries.population, countries.surface_area from countries
where countries.surface_area < 501 and countries.population >100000;

select countries.name, countries.government_form, countries.capital, countries.life_expectancy from countries
where countries.government_form = "Constitutional Monarchy" and countries.capital > 200 and countries.life_expectancy > 75;

select countries.name as country_name, cities.name as city_name, cities.district, cities.population from countries
join cities on countries.id =  cities.country_id
where countries.name = 'Argentina' and cities.district = 'Buenos Aires' and cities.population >500000;

select countries.region, count(countries.name) from countries
group by countries.region
order by count(countries.name) desc;
