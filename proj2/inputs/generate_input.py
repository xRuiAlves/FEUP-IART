import sys
import random

if (len(sys.argv) < 5):
    sys.stderr.write("Error: Not enough arguments.\n")
    sys.stderr.write("usage: " + sys.argv[0] + " <num_events> <num_rooms> <num_features> <num_students>\n")
    sys.exit(1)
    
num_events = int(sys.argv[1])
num_rooms = int(sys.argv[2])
num_features = int(sys.argv[3])
num_students = int(sys.argv[4])

header = "{} {} {} {}".format(num_events, num_rooms, num_features, num_students)
print(header)

num_students_per_event = min(num_students, max(1, (num_students//num_events)))

for i in range(num_rooms):
    room_size = max(1, random.randint(num_students_per_event-1, num_students_per_event+4))
    print(room_size)

for i in range(num_students):
    participations = ([1]*num_students_per_event) + ([0]*(num_events - num_students_per_event))
    random.shuffle(participations)
    for is_participating in participations:
        print(is_participating)

for i in range(num_rooms):
    num_contained_features = max(1, random.randint(num_features-2, num_features))
    room_features = ([1]*num_contained_features) + ([0]*(num_features - num_contained_features))
    random.shuffle(room_features)
    for feature in room_features:
        print(feature)

for i in range(num_events):
    num_needed_features = random.randint(1, min(3, num_features))
    event_features = ([1]*num_needed_features) + ([0]*(num_features - num_needed_features))
    random.shuffle(event_features)
    for feature in event_features:
        print(feature)