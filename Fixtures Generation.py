import sys
import random

#receive input from user
usern = input('Enter username: ')
print ("Hello {}! Enter an even number of teams with 'quit' as the last team ".format(usern))
exit_loop = False
teams = []
while not exit_loop:
    team = input("Enter a team: ")
    
    if team == "quit":
        if not len(teams)%2:
            break
        print("The teams must be even! Enter at least one more team!")
        continue
    teams.append(team)

# Make such a data-structure of fixtures from teams entered
# Pick a random fixture and pop it from the list

next_team = 1
fixtures = []

teams2 = list(teams)
while len(teams) != 1:
    match = (teams[0], teams[next_team],)  # A pair of teams
    fixtures.append(match) # Add the pair to the fixtures
    if next_team == len(teams) - 1: # If possible fixtures for a single team are complete
        next_team = 1 # Reset next team
        del teams[0] # Remove team whose fixtures have been exhausted
        continue # Restart
    next_team += 1 # Switch to the next team in the list
print ("All the fixtures to be played by all the teams are: ")

# Random matches per matchday
# Matches equal to number of teams divided by 2

pairs = {}

while len(teams2) > 1:

    #Using the randomly created indices, respective elements are popped out
    r1 = random.randrange(0, len(teams2))
    elem1 = teams2.pop(r1)

    r2 = random.randrange(0, len(teams2))
    elem2 = teams2.pop(r2)

    # now the selecetd elements are paired in a dictionary
    pairs[elem1] = elem2

#The variable 'pairs' is now a dictionary of the form:
#{'Juventus' vs 'Bayern', 'Barcelona' vs 'Atletico', 'ManCity' vs 'RealMadrid'}

#Print the elements of the dictionary in the desired format:
i = 1

for key, value in pairs.items():
    print("Random Fixture {}: {} vs {}".format(i, key, value))
    i += 1
#print ("The pool of randomly generated fixtures are: \n")
print (fixtures)
