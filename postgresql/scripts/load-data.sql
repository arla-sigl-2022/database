COPY users(username)
FROM '/tmp/scripts/data/users.csv' DELIMITER ',' CSV HEADER;

COPY planet(name)
FROM '/tmp/scripts/data/planets.csv' DELIMITER ',' CSV HEADER;

COPY ressource(planet_id,name,price)
FROM '/tmp/scripts/data/ressources.csv' DELIMITER ',' CSV HEADER;

COPY contractor(name,location,about,email,phone)
FROM '/tmp/scripts/data/contractors.csv' DELIMITER ',' CSV HEADER;

COPY contractor_sells_ressource(contractor_id, ressource_id)
FROM '/tmp/scripts/data/contractor_sells_ressource.csv' DELIMITER ',' CSV HEADER;

COPY delivery_status(name)
FROM '/tmp/scripts/data/delivery_status.csv' DELIMITER ',' CSV HEADER;

COPY orders(price,created_at,delivery_status)
FROM '/tmp/scripts/data/orders.csv' DELIMITER ',' CSV HEADER;

COPY ordered_to_contractor(order_id,contractor_id,ressource_id,quantity)
FROM '/tmp/scripts/data/ordered_to_contractor.csv' DELIMITER ',' CSV HEADER;

COPY user_orders(user_id,order_id)
FROM '/tmp/scripts/data/user_orders.csv' DELIMITER ',' CSV HEADER;
