INSERT INTO rules
VALUES ('rock', 'spock', 'spock'),
       ('rock', 'lizard', 'rock'),

       ('paper', 'spock', 'paper'),
       ('paper', 'lizard', 'lizard'),

       ('scissors', 'spock', 'spock'),
       ('scissors', 'lizard', 'lizard'),

       ('spock', 'rock', 'spock'),
       ('spock', 'paper', 'paper'),
       ('spock', 'scissors', 'spock'),
       ('spock', 'spock', NULL),
       ('spock', 'lizard', 'lizard'),

       ('lizard', 'rock', 'rock'),
       ('lizard', 'paper', 'lizard'),
       ('lizard', 'scissors', 'scissors'),
       ('lizard', 'spock', 'lizard'),
       ('lizard', 'lizard', NULL);
