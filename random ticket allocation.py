import random

total_tickets = 6  # Total number of tickets available
interested_people = {'Kehinde': 4, 'Kevin': 2, 'Dave': 3, 'Tyrone': 2, 'Alice': 5}  # Dictionary with names and number of tickets each person wants

# Calculate the total number of tickets requested by all interested people
total_requested_tickets = sum(interested_people.values())

# Determine the number of winners (no more than 2)
num_winners = min(2, total_tickets)

# Create a list of all interested people
people_list = list(interested_people.keys())

# Randomly select the winners
winners = set(random.sample(people_list, num_winners))

# Calculate the total number of tickets assigned to the winners
total_assigned_tickets = sum([interested_people[winner] for winner in winners])

# Allocate the remaining tickets to the non-winners
tickets_left = total_tickets - total_assigned_tickets
for person in interested_people.keys():
    if person not in winners:
        interested_people[person] = min(interested_people[person], tickets_left)

# Print out the results
print("The winners are: ", ", ".join(winners))
print("Ticket allocation:")
for person, num_tickets in interested_people.items():
    print(person + ": " + str(num_tickets))

    
# We first define the total number of tickets available and the number of tickets requested by each interested person. We then calculate the total number of tickets requested by all interested people and determine the number of winners (up to a maximum of 2). We create a list of all interested people and randomly select the winners./
# We then calculate the total number of tickets assigned to the winners and allocate the remaining tickets to the non-winners. We do this by iterating over all interested people who did not win and assigning them the minimum of the number of tickets they requested and the number of tickets left.
# Finally, we print out the winners and the final allocation of tickets to all interested people. Note that in this version of the script, all interested people are taken into consideration even if there aren't enough tickets for all of them.
