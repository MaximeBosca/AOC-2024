right_list = []
left_list = []
with open('input.txt', 'r') as file:
    for line in file:
        left, right = line.strip().split("   ")
        left_list.append(int(left))
        right_list.append(int(right))
left_list.sort()
right_list.sort()

similarity_score = 0

previous_number = 0
previous_occurences = 0
right_index = 0
for i in range(len(left_list)):
    current_number = left_list[i]
    if current_number == previous_number:
        similarity_score += previous_occurences * previous_number
        continue
    occurences = 0
    while right_index < len(right_list) and right_list[right_index] <= current_number :
        right_number = right_list[right_index]
        if right_number == current_number:
            occurences += 1
        right_index += 1

    similarity_score += previous_occurences * previous_number

    previous_number = current_number
    previous_occurences = occurences


print(similarity_score)
