def calculate_final_grade(scores, homework_weight=0.2, project_weight=0.2, exam_weight=0.6, bonus_points=0):

    if scores and len(scores) == 3 and all(0 <= score <= 100 for score in scores):
        
        bonus = bonus_points

        #check bonus
        if not isinstance(bonus,(int, float)) and 0 <= bonus <= 5:
            bonus = 0

        #check weights 
        if 0 > homework_weight > 1: 
            homework_weight = 0.2
        if 0 > project_weight > 1:
            project_weight = 0.2
        if 0 > exam_weight > 1:
            exam_weight = 0.6

        # check total weight
        total = homework_weight + project_weight + exam_weight
        if total != 1:
            homework_weight, project_weight, exam_weight = 0.2, 0.2, 0.6

        #return value
        return (scores[0] * homework_weight) + (scores[1] * project_weight) + (scores[2] * exam_weight) + bonus

        #if not, return None
    else:
        return None

def generate_student_report(name, grade=None, comments=None):
    if comments is None:
        return(f"Name: {name}\nFinal score: {grade}\nComments: \n{comments}")
    return(f"Name: {name}\nFinal score: {grade}\nComments: \n{''.join(comments)}")

            
            