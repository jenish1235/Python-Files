
#  HP of Characters = 45 points
# The game has 3 difficulty settings: Easy , Medium , Hard
#  Depending on what difficulty is selected the health obtained by the character from medkits will differ.         
# The more hard the dfficulty the less HP player gets.


#  Code starts here===>

import random

health = 50
difficulty = 1

potion_health = int(random.randint(25, 50)/difficulty)

total_health = health + potion_health
print(total_health)