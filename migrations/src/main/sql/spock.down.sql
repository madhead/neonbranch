DELETE FROM rules
WHERE player1 IN ('spock', 'lizard')
   OR player2 IN ('spock', 'lizard');
