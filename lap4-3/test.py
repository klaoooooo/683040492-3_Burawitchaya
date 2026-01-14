def calculate_gpa_static(credits  = [], grades = []):
    grades_dict = {
        'A' : 4.0,
        'B+' : 3.5,
        'B' : 3.0,
        'C+' : 2.5,
        'C' : 2.0,
        'D+' : 1.5,
        'D' : 1.0,
        'F' : 0.0
    }
    total_credits = sum(credits)
    total_point = 0

    if total_credits == 0:
        return 0.0
    
    for i in range (len(credits)):
        total_point += credits[i] * grades_dict.get(grades[i].upper())
    return total_point / total_credits

if __name__ == "__main__":
    # Example usage
    credits = [3, 3, 4]
    grades = ['A', 'B+', 'C']
    gpa = calculate_gpa_static(credits, grades)
    print(f"Calculated GPA: {gpa}")
