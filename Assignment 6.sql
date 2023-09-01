show databases;

use demo1;

create table inventory (product_id int, warehouse_id int, date varchar(15), quantity int);

INSERT INTO inventory (product_id, warehouse_id, date, quantity)
VALUES
    (1, 101, '2023-09-01', 100),
    (1, 102, '2023-09-01', 150),
    (2, 101, '2023-09-01', 75),
    (2, 102, '2023-09-01', 120),
    (1, 101, '2023-09-02', 110),
    (1, 102, '2023-09-02', 160),
    (2, 101, '2023-09-02', 80),
    (2, 102, '2023-09-02', 130);

select * from inventory;

SELECT product_id, warehouse_id, SUM(quantity) AS total_quantity
FROM inventory
WHERE (product_id, warehouse_id, date) IN (
    SELECT
        product_id,
        warehouse_id,
        MAX(date) AS latest_date
    FROM inventory
    GROUP BY product_id, warehouse_id
)
GROUP BY product_id, warehouse_id;
