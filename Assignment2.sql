show databases;

use demo1;

create table salaries (depname varchar(25), empno int, salary int );

insert into salaries VALUES 
('develop', 11,5200),
('develop', 7, 4200),
('develop', 9, 4500),
('develop', 8, 6000),
('develop', 10, 5200),
('develop', 5, 3500),
('develop', 2, 3900),
('sales', 3, 4800),
('sales', 1, 5000),
('sales', 4, 4800);
select * from salaries;

SELECT empno FROM salaries ORDER BY salary DESC LIMIT 1;
