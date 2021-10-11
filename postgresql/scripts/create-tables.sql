DROP TABLE IF EXISTS "orders" CASCADE;
DROP TABLE IF EXISTS "users" CASCADE;
DROP TABLE IF EXISTS "delivery_status" CASCADE;
DROP TABLE IF EXISTS "contractor" CASCADE;
DROP TABLE IF EXISTS "ressource" CASCADE;
DROP TABLE IF EXISTS "planet" CASCADE;
DROP TABLE IF EXISTS "user_orders" CASCADE;
DROP TABLE IF EXISTS "ordered_to_contractor" CASCADE;
DROP TABLE IF EXISTS "contractor_sells_ressource" CASCADE;
CREATE TABLE "users" (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL
);
CREATE TABLE "delivery_status" (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);
CREATE TABLE "orders" (
    id SERIAL PRIMARY KEY,
    created_at BIGINT NOT NULL CHECK (created_at >= 0),
    price FLOAT NOT NULL,
    delivery_status INT REFERENCES delivery_status(id)
);
CREATE TABLE "contractor" (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    about TEXT,
    email TEXT,
    phone TEXT
);
CREATE TABLE "planet" (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);
CREATE TABLE "ressource" (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    planet_id INT REFERENCES planet(id) ON DELETE NO ACTION,
    price FLOAT NOT NULL
);
CREATE TABLE "user_orders" (
    user_id INT REFERENCES users(id) ON DELETE NO ACTION,
    order_id INT REFERENCES orders(id) ON DELETE NO ACTION,
    PRIMARY KEY (user_id, order_id)
);
CREATE TABLE "ordered_to_contractor" (
    order_id INT REFERENCES orders(id) ON DELETE NO ACTION,
    contractor_id INT REFERENCES contractor(id) ON DELETE NO ACTION,
    ressource_id INT REFERENCES ressource(id) ON DELETE NO ACTION,
    quantity FLOAT NOT NULL,
    PRIMARY KEY (order_id, contractor_id, ressource_id)
);
CREATE TABLE "contractor_sells_ressource" (
    contractor_id INT REFERENCES contractor(id) ON DELETE NO ACTION,
    ressource_id INT REFERENCES ressource(id) ON DELETE NO ACTION,
    PRIMARY KEY (contractor_id, ressource_id)
);