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

NUM_TIMESLOTS = 9 * 5

header = "{} {} {} {}".format(num_events, num_rooms, num_features, num_students)
print(header)

max_slot_identifier = NUM_TIMESLOTS * num_rooms

if num_events >= max_slot_identifier:
    sys.stderr.write("Error: Too many events for the available rooms.\n")
    sys.exit(2)

solution = [i for i in range(max_slot_identifier)]
random.shuffle(solution)
solution = solution[:num_events]

events_features = []
rooms_features = [[0 for i in range(num_features)] for j in range(num_rooms)]
students_events = []
needed_room_sizes = [0 for i in range(num_rooms)]
events_num_attendees = [0 for i in range(num_events)]

students_occupied_timeslots = [[0 for i in range(NUM_TIMESLOTS)] for j in range(num_students)]

# events needed features
for i in range(num_events):
    num_features_in_event = random.randint(1, num_features)
    event_features = [1 for i in range(num_features_in_event)] + [0 for i in range(num_features - num_features_in_event)]
    random.shuffle(event_features)
    events_features.append(event_features)

# rooms features to make solution valid
for event_number in range(num_events):
    timeslot_identifier = solution[event_number]
    room_number = timeslot_identifier % num_rooms
    for feature_number in range(num_features):
        rooms_features[room_number][feature_number] = rooms_features[room_number][feature_number] or events_features[event_number][feature_number]
for room_number in range(num_rooms):
    for room_feature in range(num_features):
        if not rooms_features[room_number][room_feature]:
           rooms_features[room_number][room_feature] = 1 if (random.random() < 0.8) else 0

# which events students are attending
for student_id in range(num_students):
    student_events = []
    for event_number in range(num_events):
        timeslot_identifier = solution[event_number]
        timeslot = timeslot_identifier // num_rooms
        if not students_occupied_timeslots[student_id][timeslot]:
            if (random.random() < 0.4):
                student_events.append(1)
                students_occupied_timeslots[student_id][timeslot] = 1
                events_num_attendees[event_number] += 1
            else:
                student_events.append(0)
        else:
            student_events.append(0)
    students_events.append(student_events)

# room sizes
for event_number in range(num_events):
    timeslot_identifier = solution[event_number]
    room_number = timeslot_identifier % num_rooms
    needed_room_sizes[room_number] = max(needed_room_sizes[room_number], events_num_attendees[event_number])
    
for i in range(num_rooms):
    if needed_room_sizes[i] == 0:
        needed_room_sizes[i] = random.randint(num_students - 1, num_students + 1)
    else:
        needed_room_sizes[i] += num_students//2



# build input file

# room size
for size in needed_room_sizes:
    print(size)

# students events attendance
for student_attendances in students_events:
    for is_attending in student_attendances:
        print(is_attending)

# room features
for room_features in rooms_features:
    for has_feature in room_features:
        print(has_feature)

# event needed features
for event_features in events_features:
    for needs_feature in event_features:
        print(needs_feature)
