def calculate_average(scores):
    total = 0
    num = 0
    for score in scores:
        try:
            score = float(score)
            total += score
            num += 1
        except ValueError as e:
            print(f"calculate_average(): {e}")
    try:
       avg = total / num
    except:
       avg = 0
    return avg

def print_scores(all_scores):
  for s in range(len(all_scores)):
    print(f"Student {s+1}: {all_scores[s]}")

# main program
if __name__ == "__main__":
    grades_file = open('grades.txt', 'r')
    content = grades_file.read()

    all_scores = content.split()
    print_scores(all_scores)
    print(f"First student: {all_scores[0]}")
    print(f"Last student: {all_scores[-1]}")

    avg = calculate_average(all_scores)
    print(f"Class avg = {avg:.2f}")
    norm = 10
    print(f"Adjusted avg = {avg + norm:.2f}")