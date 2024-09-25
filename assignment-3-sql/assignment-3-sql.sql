-- CFG SQL Project - A vets database, where there are owners in one table, and their pets in different species table.
-- This will be able to allow vets to have a table of owners and their details and then have species specific tables
-- which link back to the owners table so it's easy to view an owner and their pets. 
-- This will allow vets to access owner/pet data easily, and easily update weight and neutered status when needed.

-- Creates vets database
CREATE DATABASE vets;

-- To ensure you are using the correct database
USE vets;

-- reference table which holds the primary key and reference fields
CREATE TABLE owners (
    owner_id INT PRIMARY KEY AUTO_INCREMENT,
    owners_name VARCHAR(100) NOT NULL,
    post_code VARCHAR(20) NOT NULL,
    email VARCHAR(100) UNIQUE
);

-- Insert rows of data into owners table
INSERT INTO owners
(owners_name, post_code, email)
VALUES
('John Smith', 'LU1 3AR', 'john@smith.com'),
('Emily Johnson', 'MK40 1NE', 'emily@johnson.com'),
('Michael Brown', 'SG18 0AA', 'michael@brown.com'),
('Sarah Davis', 'LU7 1EU', 'sarah@davis.com'),
('David Wilson', 'MK45 1EX', 'david@wilson.com'),
('Laura Taylor', 'SG17 5BU', 'laura@taylor.com'),
('James Anderson', 'LU2 7UX', 'james@anderson.com'),
('Emma Thomas', 'MK42 9DF', 'emma@thomas.com'),
('Robert White', 'LU6 2SD', 'robert@white.com'),
('Linda Harris', 'MK41 7TL', 'linda@harris.com'),
('Chris Lewis', 'LU5 5BN', 'chris@lewis.com'),
('Rachel Clark', 'SG19 1DL', 'rachel@clark.com'),
('Paul Robinson', 'MK43 0AN', 'paul@robinson.com'),
('Sophie Walker', 'SG16 6AZ', 'sophie@walker.com'),
('Mark Hall', 'LU4 8BB', 'mark@hall.com');


-- Create a table called 'dogs' to be included in vets db, with the following columns
CREATE TABLE dogs (
	pet_id INT PRIMARY KEY,
    pet_name VARCHAR(50) NOT NULL,
    owner_id INT,
    year_born INT NOT NULL,
    month_born INT NOT NULL,
    breed VARCHAR(100) NOT NULL,
    colour VARCHAR(50),
    weight DECIMAL(5,2),
	is_neutered BOOLEAN NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES owners(owner_id) ON DELETE CASCADE
    );

-- Insert the following data into the dogs table within the vets db    
INSERT INTO dogs 
(pet_id, pet_name, owner_id, year_born, month_born, breed, colour, weight, is_neutered)
VALUES
(1, 'Buddy', 3, 2018, 3, 'Golden Retriever', 'Golden', 30.50, TRUE),
(2, 'Bella', 3, 2020, 6, 'Labrador', 'Black', 28.00, FALSE),
(3, 'Max', 4, 2017, 9, 'German Shepherd', 'Brown', 35.00, TRUE),
(4, 'Max', 1, 2019, 12, 'Beagle', 'Tricolor', 12.50, FALSE),
(5, 'Charlie', 2, 2021, 4, 'Bulldog', 'White', 25.00, TRUE),
(6, 'Daisy', 9, 2016, 7, 'Poodle', 'Apricot', 18.75, TRUE),
(7, 'Milo', 5, 2020, 8, 'Border Collie', 'Black and White', 22.00, TRUE),
(8, 'Rocky', 6, 2019, 10, 'Boxer', 'Fawn', 30.75, FALSE),
(9, 'Zoe', 7, 2021, 5, 'Cocker Spaniel', 'Golden', 14.20, TRUE),
(10, 'Lola', 8, 2017, 11, 'Dachshund', 'Brown', 8.50, FALSE);

-- Create a cats table with the same columns
CREATE TABLE cats (
	pet_id INT PRIMARY KEY,
    pet_name VARCHAR(50) NOT NULL,
    owner_id INT,
    year_born INT NOT NULL,
    month_born INT NOT NULL,
    breed VARCHAR(100) NOT NULL,
    colour VARCHAR(50),
    weight DECIMAL(5,2),
	is_neutered BOOLEAN NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES owners(owner_id) ON DELETE CASCADE
    );
    
-- Inserting data into cats table within vets db 
INSERT INTO cats 
(pet_id, pet_name, owner_id, year_born, month_born, breed, colour, weight, is_neutered)
VALUES
(1, 'Whiskers', 1, 2019, 4, 'Maine Coon', 'Brown Tabby', 8.50, TRUE),
(2, 'Mittens', 7, 2017, 8, 'Siamese', 'Cream and Brown', 6.75, FALSE),
(3, 'Shadow', 8, 2020, 11, 'British Shorthair', 'Gray', 7.00, TRUE),
(4, 'Luna', 3, 2018, 2, 'Bengal', 'Spotted Brown', 9.25, TRUE),
(5, 'Oliver', 10, 2021, 5, 'British Shorthair', 'Blue', 8.00, FALSE),
(6, 'Chloe', 6, 2016, 9, 'Sphynx', 'Pink', 5.50, TRUE),
(7, 'Simba', 13, 2019, 6, 'Abyssinian', 'Ruddy', 7.80, FALSE),
(8, 'Bella', 5, 2020, 3, 'Ragdoll', 'Seal Point', 6.30, TRUE),
(9, 'Cleo', 4, 2017, 10, 'Persian', 'White', 7.20, FALSE),
(10, 'Tiger', 9, 2018, 7, 'Maine Coon', 'Marbled Brown', 8.10, TRUE);

-- Create another table but for exotic pets. Removing month_born NOT NULL due to nature of exotic pets
CREATE TABLE exotics (
	pet_id INT PRIMARY KEY,
    pet_name VARCHAR(50) NOT NULL,
    owner_id INT,
    year_born INT NOT NULL,
    month_born INT,
    species VARCHAR(100) NOT NULL,
    colour VARCHAR(50),
    weight DECIMAL(5,2),
	is_neutered BOOLEAN,
    FOREIGN KEY (owner_id) REFERENCES owners(owner_id) ON DELETE CASCADE
    );

-- insert data into exotics table
INSERT INTO exotics 
(pet_id, pet_name, owner_id, year_born, month_born, species, colour, weight, is_neutered)
VALUES
(1, 'Spike', 3, 2018, 6, 'Iguana', 'Green', 4.50, NULL),
(2, 'Ziggy', 3, 2019, NULL, 'Parrot', 'Red and Green', 0.75, NULL), 
(3, 'Bubbles', 5, 2020, NULL, 'Axolotl', 'Pink', 0.30, NULL),
(4, 'Slinky', 11, 2017, NULL, 'Snake', 'Brown and Yellow', 1.20, NULL),
(5, 'Gizmo', 11, 2021, NULL, 'Ferret', 'White and Brown', 1.50, TRUE),
(6, 'Thor', 12, 2016, NULL, 'Tarantula', 'Black', 0.20, NULL),
(7, 'Cleo', 13, 2018, NULL, 'Chameleon', 'Multicolored', 0.60, NULL),
(8, 'Loki', 6, 2019, 5, 'Bearded Dragon', 'Orange', 0.55, NULL),
(9, 'Apollo', 8, 2017, 9, 'Hedgehog', 'Brown and White', 0.80, NULL),
(10, 'Pepper', 9, 2020, 3, 'Gecko', 'Yellow and Black', 0.15, NULL); 


-- Deletes record from exotics where the id is 11 and pets name is Gizmo.
DELETE FROM exotics
WHERE
pet_id = 5
AND
pet_name = 'Gizmo';

-- selecting all rows/columns from exotics table
SELECT *
FROM exotics
ORDER BY pet_id;

-- Select all from cats table where pets name is Luna
SELECT * 
FROM cats
WHERE 
pet_name = 'Luna';

-- Select all from dogs, ordered by pet id descending
SELECT * 
FROM dogs 
ORDER BY 
pet_id 
DESC;

-- Selecting name, breed, colour and weight from dog table where the owner id is 6
SELECT pet_name, breed, colour, weight
FROM dogs
WHERE
owner_id = 6;

-- Updating weight of dog called Buddy with owner_id of 3
UPDATE dogs
SET
weight = 28
WHERE
dogs.pet_name =
'Buddy'
AND
owner_id = 3;

-- Select only unique pet names from the dogs table
SELECT DISTINCT pet_name
FROM dogs;

-- Counts all rows in dogs table
SELECT COUNT(*)
FROM dogs;

-- Selecting max weight to get the heaviest dog, and then selecting name and weight from that query to 
-- get the name and weight of the heaviest dog from the dogs table
SELECT pet_name, weight
FROM dogs
WHERE weight = (SELECT MAX(weight) FROM dogs)
ORDER BY pet_name;

-- inner join owners and dogs on owner_id, and then selecting the owners and their pets/breed/weight
-- using alias' for tables.
SELECT o.owners_name, d.pet_name, d.breed, d.weight
FROM owners o
INNER JOIN dogs d ON o.owner_id = d.owner_id
ORDER BY owners_name;

-- Finding all pets for each owner in the owners table with a left join. So this returns
-- all data from the owners table, and data from dog/cat/exotics where they meet the 
-- ON statement
SELECT o.owners_name, d.pet_name AS dog, c.pet_name AS cat, e.pet_name AS exotic_pets
FROM owners o
LEFT JOIN dogs d ON o.owner_id = d.owner_id
LEFT JOIN cats c ON o.owner_id = c.owner_id
LEFT JOIN exotics e ON o.owner_id = e.owner_id
ORDER BY owners_name;

-- Re: Normalisation: I did think about making a pets table instead of having all animals 
-- seperated into species, and I would have done this if the requirements didn't need
-- three tables. 

-- Selecting all dogs, their name and their weight with the unit added
SELECT dogs.pet_name, CONCAT(dogs.weight, 'kg') 
FROM dogs;

-- Selecting owners name and email and making owners name uppercase and email lowercase
SELECT UPPER(owners_name), LOWER(email)
FROM owners;

-- Procedure to update dogs weight:
DELIMITER // 
CREATE PROCEDURE UpdatePetWeight(petID INT, newWeight DECIMAL(5,2))
BEGIN
     UPDATE dogs SET weight = newWeight WHERE pet_id = petID;
END//
DELIMITER ;

-- Call procedure to update entered dogs weight
CALL UpdatePetWeight(1, 32.50);

-- Check to ensure weight has been updated
SELECT *
FROM dogs
WHERE pet_id = 1;







