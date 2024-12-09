#Advent of Code Day 1



import math 

#parse input

def read_input(input_file_dir):
    with open(input_file_dir, 'r') as file:
        lines = file.readlines()
    list1 = []
    list2 = []
    for line in lines:
        data = line.split()
        list1.append(int(data[0]))
        list2.append(int(data[1]))
    return list1, list2

#Part 1
def calculate_total_distance(list1, list2):
    list1.sort()
    list2.sort()
    total_distance = 0
    for i in range(len(list1)):
        total_distance += (math.fabs(list1[i] - list2[i]))
    return total_distance

#part 2
def calculate_similartiy_score(list1, list2):
    number_occurrence_map = {}
    similarity_score = 0
    for number in list2:
        if number not in number_occurrence_map:
            number_occurrence_map[number] = 1
        else:
            current_count = number_occurrence_map[number]
            number_occurrence_map[number] = current_count + 1
    for number in list1:
        if number in number_occurrence_map:
            count = number * number_occurrence_map[number]
            similarity_score += count
    return similarity_score
        
#main function 

if __name__ == '__main__':
    list1, list2 = read_input('./inputFile.txt')

    totalDistance = calculate_total_distance(list1, list2)
    score = calculate_similartiy_score(list1, list2)

    print(totalDistance)
    print(score)