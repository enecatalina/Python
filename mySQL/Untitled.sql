SELECT * FROM world.countries;
JOIN languages 
ON  languages.country_id = countries.id
WHERE languages.language = "Slovene"
ORDER BY  percentage ASC;

-- SELECT clients.first_name, clients.last_name, SUM(billing.amount)
-- FROM clients
-- JOIN billing ON clients.id = billing.clients_id;
-- GROUP BY  clients.id;