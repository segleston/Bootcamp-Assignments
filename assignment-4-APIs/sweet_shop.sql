CREATE DATABASE sweet_shop;

USE sweet_shop;

CREATE TABLE sweets(
	sweet_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description VARCHAR(200),
    stock_quantity INT NOT NULL,
    category VARCHAR(50),
    flavour VARCHAR(50),
    ingredients VARCHAR(250) NOT NULL
);

INSERT INTO sweets (name, price, description, stock_quantity, category, flavour, ingredients)
VALUES 
('sherbet lemon', 0.50, 'hard lemon-flavored candy with a fizzy sherbet center.', 200, 'hard boiled sweets', 'lemon', 'sugar, citric acid, natural lemon flavor, sodium bicarbonate'),
('liquorice allsorts', 1.50, 'a mix of colorful, layered sweets made with liquorice.', 150, 'liquorice', 'liquorice', 'sugar, treacle, gelatin, liquorice extract, coconut'),
('rhubarb and custard', 0.75, 'classic boiled sweet with a tangy rhubarb half and creamy custard half.', 180, 'boiled sweets', 'rhubarb and custard', 'sugar, glucose syrup, citric acid, natural flavors, coloring'),
('pear drops', 0.60, 'traditional boiled sweet with a distinctive pear flavor and aroma.', 120, 'hard boiled sweets', 'pear', 'sugar, glucose syrup, natural pear flavor, citric acid, coloring'),
('toffee', 1.00, 'chewy and rich traditional english toffee.', 140, 'toffee', 'caramel', 'butter, sugar, golden syrup, cream');

CREATE TABLE orders(
	customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    sweet_ordered VARCHAR(100) NOT NULL,
    total_cost DECIMAL(10, 2) NOT NULL
)

SELECT * FROM orders;



SELECT * FROM sweets;
