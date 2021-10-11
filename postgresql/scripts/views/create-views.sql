CREATE VIEW ressource_catalog AS
 SELECT r.id,
    p.name AS planete,
    r.name AS ressource,
    r.price AS prix
   FROM planet p,
    ressource r
  WHERE p.id = r.planet_id;

CREATE VIEW orders_with_contractor AS
 SELECT otc.order_id,
    o.created_at AS order_date,
    r.name AS ressource,
    c.name AS contractor,
    u.username AS usersname
   FROM ordered_to_contractor otc
     JOIN user_orders uo ON otc.order_id = uo.order_id
     JOIN orders o ON uo.order_id = o.id
     JOIN contractor c ON otc.contractor_id = c.id
     JOIN ressource r ON otc.ressource_id = r.id
     JOIN users u ON u.id = uo.user_id;