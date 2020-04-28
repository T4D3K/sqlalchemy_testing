PRAGMA foreign_keys = ON;

CREATE TABLE user
(
  id            INTEGER PRIMARY KEY SERIAL,
  name          VARCHAR(255),
  surname       VARCHAR(255),
  date_of_birth VARCHAR(10)
);

CREATE TABLE account
(
  id       INTEGER PRIMARY KEY SERIAL,
  login    VARCHAR(255),
  password VARCHAR(255),
  user_id  INTEGER,
  FOREIGN KEY (user_id) REFERENCES user (id)
);

CREATE TABLE product
(
  id    INTEGER PRIMARY KEY SERIAL,
  name  VARCHAR(255),
  price INTEGER
);

CREATE TABLE product_stock
(
  id             INTEGER PRIMARY KEY SERIAL,
  product_id     INTEGER,
  purchase_price INTEGER,
  quantity       INTEGER,
  FOREIGN KEY (product_id) REFERENCES product (id)
);

CREATE TABLE invoice
(
  id             INTEGER PRIMARY KEY SERIAL,
  account_id     INTEGER,
  invoice_date   TEXT,
  invoice_number VARCHAR(255),
  invoice_amount INTEGER,
  FOREIGN KEY (account_id) REFERENCES account (id)
);

CREATE TABLE invoice_item
(
  id         INTEGER PRIMARY KEY SERIAL,
  invoice_id INTEGER,
  product_id INTEGER,
  name       VARCHAR(255),
  quantity   INTEGER,
  price      INTEGER,
  discount   INTEGER
);
