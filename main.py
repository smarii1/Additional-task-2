def read_data(file_path):
    students_scores = {}
    with open(file_path, 'r') as file:
        for line in file:
            name, score = line.strip().split()
            score = int(score)
            if name in students_scores:
                students_scores[name].append(score)
            else:
                students_scores[name] = [score]
    return students_scores

def calculate_averages(students_scores):
    students_averages = {}
    for student, scores in students_scores.items():
        students_averages[student] = sum(scores) / len(scores)
    return students_averages

def calculate_min_max(students_scores):
    all_scores = []
    for scores in students_scores.values():
        all_scores.extend(scores)
    highest_score = max(all_scores)
    lowest_score = min(all_scores)
    overall_average = sum(all_scores) / len(all_scores)

    score_counts = {}
    for score in all_scores:
        if score in score_counts:
            score_counts[score] += 1
        else:
            score_counts[score] = 1
    mode_score = None
    max_count = 0
    for score, count in score_counts.items():
        if count > max_count:
            max_count = count
            mode_score = score
    return highest_score, lowest_score, overall_average, mode_score

def write_results(file_path, students_averages, statistics):
    highest_score, lowest_score, overall_average, mode_score = statistics
    with open(file_path, 'w') as file:
        for student, average in students_averages.items():
            file.write(f"{student}: {average}\n")
        file.write("\n")
        file.write(f"Highest Score: {highest_score}\n")
        file.write(f"Lowest Score: {lowest_score}\n")
        file.write(f"Overall Average: {overall_average}\n")
        file.write(f"Mode Score: {mode_score}\n")

input_file = "s.txt"
output_file = "student_averages.txt"

students_scores = read_data(input_file)
students_averages = calculate_averages(students_scores)
statistic = calculate_min_max(students_scores)
write_results(output_file, students_averages, statistic)
