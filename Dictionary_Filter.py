scores = {"Alice": 85, "Bob": 70, "Charlie": 95, "David": 60}
passing_students = {}
threshold = 75

for name, score in scores.items():
    if score >= threshold:
        passing_students[name] = score

print(f"Passing Students: {passing_students}")