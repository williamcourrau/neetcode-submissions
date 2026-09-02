-- Write your query below
select c.name
from customers as c
where c.id not in(select customer_id from orders)

