SELECT invoice.id                     AS invoice_id,
       invoice.account_id             AS invoice_account_id,
       invoice.invoice_date           AS invoice_invoice_date,
       invoice.invoice_number         AS invoice_invoice_number,
       invoice.invoice_amount         AS invoice_invoice_amount,
       user_1.id                      AS user_1_id,
       user_1.name                    AS user_1_name,
       user_1.surname                 AS user_1_surname,
       user_1.date_of_birth           AS user_1_date_of_birth,
       account_1.id                   AS account_1_id,
       account_1.login                AS account_1_login,
       account_1.password             AS account_1_password,
       account_1.user_id              AS account_1_user_id,
       product_stock_1.id             AS product_stock_1_id,
       product_stock_1.product_id     AS product_stock_1_product_id,
       product_stock_1.purchase_price AS product_stock_1_purchase_price,
       product_stock_1.quantity       AS product_stock_1_quantity,
       product_1.id                   AS product_1_id,
       product_1.name                 AS product_1_name,
       product_1.price                AS product_1_price,
       invoice_item_1.id              AS invoice_item_1_id,
       invoice_item_1.invoice_id      AS invoice_item_1_invoice_id,
       invoice_item_1.product_id      AS invoice_item_1_product_id,
       invoice_item_1.name            AS invoice_item_1_name,
       invoice_item_1.price           AS invoice_item_1_price,
       invoice_item_1.quantity        AS invoice_item_1_quantity,
       invoice_item_1.discount        AS invoice_item_1_discount
FROM invoice
       LEFT OUTER JOIN account AS account_1 ON account_1.id = invoice.account_id
       LEFT OUTER JOIN user AS user_1 ON user_1.id = account_1.user_id
       LEFT OUTER JOIN invoice_item AS invoice_item_1 ON invoice.id = invoice_item_1.invoice_id
       LEFT OUTER JOIN product AS product_1 ON product_1.id = invoice_item_1.product_id
       LEFT OUTER JOIN product_stock AS product_stock_1 ON product_1.id = product_stock_1.product_id