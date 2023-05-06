DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS shipment;

CREATE TABLE IF NOT EXISTS inventory
(
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT,
    sku          TEXT,
    description  TEXT,
    quantity     INTEGER,
    price        INTEGER,
    company_id   INTEGER
);

CREATE TABLE IF NOT EXISTS shipment
(
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_name TEXT,
    supplier_id   INTEGER,
    customer_id   INTEGER,
    start_time    TEXT,
    status        TEXT
);