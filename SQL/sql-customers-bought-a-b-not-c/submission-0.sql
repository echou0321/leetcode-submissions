-- Write your query below
SELECT customers.customer_id, customers.customer_name
FROM customers
WHERE
    EXISTS (SELECT 1 FROM orders WHERE customer_id = customers.customer_id AND product_name = 'A')
    AND EXISTS (SELECT 1 FROM orders WHERE customer_id = customers.customer_id AND product_name = 'B')
    AND NOT EXISTS (SELECT 1 FROM orders WHERE customer_id = customers.customer_id AND product_name = 'C')
ORDER BY customers.customer_name