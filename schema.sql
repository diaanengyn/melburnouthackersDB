DROP TABLE IF EXISTS inventory;

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