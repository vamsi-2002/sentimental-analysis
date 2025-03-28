CREATE DATABASE amazon_reviews;

USE amazon_reviews;

CREATE TABLE iphone12_reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    review_title TEXT,
    review_text TEXT,
    style_name TEXT,
    colour VARCHAR(20),
    verified_purchase VARCHAR(15)
);
select * from iphone12_reviews;


