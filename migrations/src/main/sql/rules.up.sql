CREATE TABLE rules
(
    player1 VARCHAR(8) NOT NULL,
    player2 VARCHAR(8) NOT NULL,
    winner  VARCHAR(8),

    PRIMARY KEY (player1, player2)
);

INSERT INTO rules
VALUES ('rock', 'rock', NULL),
       ('rock', 'paper', 'paper'),
       ('rock', 'scissors', 'rock'),

       ('paper', 'rock', 'paper'),
       ('paper', 'paper', NULL),
       ('paper', 'scissors', 'scissors'),

       ('scissors', 'rock', 'rock'),
       ('scissors', 'paper', 'scissors'),
       ('scissors', 'scissors', NULL);
