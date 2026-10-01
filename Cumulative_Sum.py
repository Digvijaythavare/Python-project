numbers = [1, 2, 3, 4]
cumulative_list = []
current_sum = 0

for num in numbers:
    current_sum += num
    cumulative_list.append(current_sum)

print(f"Cumulative Sum: {cumulative_list}")