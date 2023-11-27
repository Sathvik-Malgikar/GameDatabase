create database GameDB;
use Gamedb;
drop table profiles;
create table profiles(name varchar(30) primary key , points int , level int, player_id varchar(20) , display_name varchar(16) ,password varchar(10) ,email varchar(50)  );
INSERT INTO profiles  
VALUES
("User1", 1200, 5, "I love gaming!", "Gamer1", "password1", "user1@example.com"),
("User2", 800, 3, "Gamer for life!", "Gamer2", "password2", "user2@example.com"),
("User3", 1500, 8, "Achievement hunter", "Gamer3", "password3", "user3@example.com"),
("User4", 600, 2, "Casual gamer", "Gamer4", "password4", "user4@example.com"),
("User5", 2000, 10, "Pro gamer", "Gamer5", "password5", "user5@example.com"),
("User6", 950, 4, "Team player", "Gamer6", "password6", "user6@example.com"),
("User7", 1700, 7, "Strategy master", "Gamer7", "password7", "user7@example.com"),
("User8", 700, 3, "High score chaser", "Gamer8", "password8", "user8@example.com"),
("User9", 1400, 6, "RPG enthusiast", "Gamer9", "password9", "user9@example.com"),
("User10", 1100, 5, "Puzzle solver", "Gamer10", "password10", "user10@example.com");

select * from profiles;

drop table cars;
create table cars(carID varchar(30) primary key , maxSpeed float , brandName varchar(30)  , modelName varchar(20) , colour varchar(16) ,ownerPlayerID varchar(20)  );
INSERT INTO cars (carID, maxSpeed, brandName, modelName, colour, ownerPlayerID)
VALUES
("vbUVYuyvuo67", 120.3, "Toyota", "Supra-mk4", "Crimson-red", "Gamer8"),
("4iLko3aWz6X", 140.2, "Ford", "Mustang", "Silver", "Gamer2"),
("Y5HtLjC9kZs", 110.8, "Chevrolet", "Camaro", "Blue", "Gamer4"),
("2gPjA1FvMws", 130.5, "Nissan", "GT-R", "Black", "Gamer6"),
("8ZqKu0LmRQn", 112.7, "Honda", "Civic", "White", "Gamer1"),
("fNvp9PjRxYd", 125.0, "BMW", "M3", "Silver", "Gamer7"),
("D3mW2bGqJzo", 138.4, "Audi", "A4", "Red", "Gamer3"),
("rKlFfO0zEj1", 118.9, "Mazda", "RX-7", "Yellow", "Gamer9"),
("1nCv5SxO2Jp", 132.1, "Porsche", "911", "Black", "Gamer5"),
("OaRyNwBh2Vp", 115.6, "Subaru", "Impreza", "Blue", "Gamer10");

select * from cars;

