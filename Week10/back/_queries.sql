-- SQLite
SELECT *
FROM api_productitem;
INSERT INTO api_productitem(name, price, description, count, is_active)
VALUES ('iPhone 11', 599, 'Great phone', 3, TRUE),
    ('iPhone 12', 799, 'Great phone', 2, TRUE),
    ('Samsung S10', 599, 'Great phone', 0, FALSE),
    ('TV Samsung', 699, 'Great TV', 5, TRUE),
    ('iPhone XR', 499, 'Great phone', 0, FALSE);
DELETE FROM api_productitem;

CREATE TABLE api_productitem(
    id INTEGER PRIMARY KEY,
    name VARCHAR(96),
    price REAL DEFAULT 0,
    description TEXT(512) DEFAULT '',
    count INTEGER DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE
);

SELECT *
FROM api_category;
INSERT INTO api_category(name)
VALUES ('phones'),
    ('tvs'),
    ('games'),
    ('computers'),
    ('books');
DELETE FROM api_category;

DROP TABLE api_category;

CREATE TABLE api_category(
    id INTEGER PRIMARY KEY,
    name VARCHAR(96)
);