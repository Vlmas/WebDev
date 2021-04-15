DROP TABLE api_company;
DROP TABLE api_vacancy;
DELETE FROM api_company;

SELECT * FROM api_company;
SELECT * FROM api_vacancy;

CREATE TABLE api_company(
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) DEFAULT '',
    description TEXT DEFAULT '',
    city VARCHAR(60) DEFAULT '',
    address TEXT DEFAULT ''
);

SELECT * FROM api_vacancy;