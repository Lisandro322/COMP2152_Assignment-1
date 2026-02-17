"""
Author: Lisandro Vasquez Matre
Assignment: #1
"""

# Step b: Create 4 variables
gym_member = "Alex Alliton" # String
preferred_weight_kg = 20.5  # Double
highest_reps = 25           # Integer
membership_active = True    # Boolean

# Step c: Create a dictionary named workout_stats
#This is a dictionary with the friends name "String" as the key and three diffrent integers tuples 
workout_stats = {"Alex":(30, 40, 50), 
                 "Jamie":(20, 20, 10), 
                 "Taylor":(60, 60, 60)}

# Step d: Calculate total workout minutes using a loop and add to dictionary
workout_stats["Alex_Total"] = 0
for stats in workout_stats["Alex"]:
    workout_stats["Alex_Total"] += stats

workout_stats["Jamie_Total"] = 0
for stats in workout_stats["Jamie"]:
    workout_stats["Jamie_Total"] += stats

workout_stats["Taylor_Total"] = 0
for stats in workout_stats["Taylor"]:
    workout_stats["Taylor_Total"] += stats

# Step e: Create a 2D nested list called workout_list
# workout_list is a 2d integer array where [i][0] = Yoga, [i][1] = running, [i][2] = weightlifting
workout_list = [[],[],[]]
for stat in workout_stats["Alex"]:
    workout_list[0].append(stat)
for stat in workout_stats["Jamie"]:
    workout_list[1].append(stat)
for stat in workout_stats["Taylor"]:
    workout_list[2].append(stat)

# Step f: Slice the workout_list

print("Yoga & Running list")
for row in workout_list:
    print("Yoga: " + str(row[0]) + " Running: " + str(row[1]))

print("weightlifting list")
for row in workout_list[-2:]:
    print(row[2])

# Step g: Check if any friend's total >= 120
name_key = list(workout_stats.keys())
print(name_key)
for i in range(len(workout_list)):
    if (workout_stats[name_key[i+3]] > 120):
        print(f"Great job staying active, {name_key[i]}!")

# Step h: User input to look up a friend

search_name = input("\nenter a name to search for: ")
if search_name in workout_stats:
    stats = workout_stats[search_name]
    total = workout_stats[f"{search_name}_Total"]
    print(f"{search_name} workout stats: {stats}, total: {total}")
else:
    print(f"Friend {search_name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes

highest = 0
lowest = 999
highest_name = ""
lowest_name = ""
for key in name_key[-3:]:
    current_total = workout_stats[key]
    
    if current_total > highest:
        highest = current_total
        highest_name = key
        
    if current_total < lowest:
        lowest = current_total
        lowest_name = key

print(f"{highest_name} has the highest total at {highest} minutes")
print(f"{lowest_name} has the lowest total at {lowest} minutes")