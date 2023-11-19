import random

per_1_names = ["Maheen", "Ayden", "Tyler", "Austin", "Leo", "Jacob", "Anthony", "Carter", "Megan", "Broden", "Jaxon", "Shane",
               "Hayle", "Kaylannie", "Josh", "Makayla", "Aleaha", "Ruby", "Jayvien", "Liba", "Jackson", "Yowell", "Brayden", "Liliana", "Lily"]

per_1_groups = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}

for name in per_1_names:
    group_number = random.randint(1, 9)
    while len(per_1_groups[group_number]) == 3:
        group_number = random.randint(1, 9)
    per_1_groups[group_number].append(name)

print()
print("Group 1: ", per_1_groups[1])
print()
print("Group 2: ", per_1_groups[2])
print()
print("Group 3: ", per_1_groups[3])
print()
print("Group 4: ", per_1_groups[4])
print()
print("Group 5: ", per_1_groups[5])
print()
print("Group 6: ", per_1_groups[6])
print()
print("Group 7: ", per_1_groups[7])
print()
print("Group 8: ", per_1_groups[8])
print()
print("Group 9: ", per_1_groups[9])
print()
