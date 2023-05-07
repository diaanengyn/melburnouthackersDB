DROP TABLE IF EXISTS inventory;
DROP TABLE IF EXISTS shipment;
DROP TABLE IF EXISTS step;
DROP TABLE IF EXISTS company;

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

CREATE TABLE IF NOT EXISTS step
(
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    shipment_id    INTEGER,
    transporter_id INTEGER,
    start_time     TEXT,
    end_time       TEXT,
    status         TEXT,
    start_loc      TEXT,
    end_loc        TEXT
);

CREATE TABLE IF NOT EXISTS company
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    name     TEXT,
    email    TEXT,
    password TEXT
);