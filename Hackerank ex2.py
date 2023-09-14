k = int(input())

# Read the room number list and split it into a list of integers
room_numbers = list(map(int, input().split()))

# Create an empty dictionary to count the occurrences of each room number
room_count = {}

# Iterate through the room numbers and count their occurrences
for room in room_numbers:
    if room in room_count:
        room_count[room] += 1
    else:
        room_count[room] = 1

# Find the room number with only one occurrence (the Captain's room)
for room, count in room_count.items():
    if count == 1:
        captain_room = room
        break

# Print the Captain's room number
print(captain_room)
print(room_count)