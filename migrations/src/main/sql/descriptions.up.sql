ALTER TABLE rules
ADD COLUMN description VARCHAR(32);

UPDATE rules 
SET description = 'It''s a tie'
WHERE player1 = 'rock' AND player2 = 'rock';
UPDATE rules 
SET description = 'Paper covers rock'
WHERE player1 = 'rock' AND player2 = 'paper';
UPDATE rules 
SET description = 'Rock crushes scissors'
WHERE player1 = 'rock' AND player2 = 'scissors';
UPDATE rules 
SET description = 'Paper covers rock'
WHERE player1 = 'paper' AND player2 = 'rock';
UPDATE rules 
SET description = 'It''s a tie'
WHERE player1 = 'paper' AND player2 = 'paper';
UPDATE rules 
SET description = 'Scissors cuts paper'
WHERE player1 = 'paper' AND player2 = 'scissors';
UPDATE rules 
SET description = 'Rock crushes scissors'
WHERE player1 = 'scissors' AND player2 = 'rock';
UPDATE rules 
SET description = 'Scissors cuts paper'
WHERE player1 = 'scissors' AND player2 = 'paper';
UPDATE rules 
SET description = 'It''s a tie'
WHERE player1 = 'scissors' AND player2 = 'scissors';
