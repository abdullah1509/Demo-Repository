show databases;
use demo1;
create table user_activity (user_id int, activity_date varchar(25), activity_type varchar(15));

INSERT INTO user_activity (user_id, activity_date, activity_type)
VALUES
    (1, '2023-09-01', 'login'),
    (2, '2023-09-01', 'click'),
    (3, '2023-09-01', 'purchase'),
    (1, '2023-09-02', 'click'),
    (2, '2023-09-02', 'login'),
    (3, '2023-09-02', 'click'),
    (4, '2023-09-02', 'login'),
    (1, '2023-09-03', 'click'),
    (2, '2023-09-03', 'purchase');

select * from user_activity;

SELECT 
    activity_date,
    ROUND(
        (COUNT(DISTINCT CASE WHEN activity_type IS NOT NULL THEN user_id END) * 100.0) 
        / COUNT(DISTINCT user_id), 2 ) 
  AS daily_engagement_rate
FROM user_activity
GROUP BY activity_date
ORDER BY activity_date;
