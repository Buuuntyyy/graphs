
def match_student_to_schools(students, 
                            schools, 
                            student_preferences, 
                            school_preferences, 
                            capacities):
    """
    [Student-proposing version]
    
    Args:
        - students: list of student 
        - schools: list of school
        - student_preferences (dict): student -> list of school
        - school_preferences (dict): school <-> list of student
        - capacities (dict): school <-> number of places available
    
    Returns :
        tuple :
            - who_got_where (dict): student -> assigned school
            - iterations : to reach a stable matching
    """
 
    still_looking = list(students)
    schools_assignements = {school: [] for school in schools}    
    attempts = {student : 0 for student in students}
    
    iterations = 0

    while still_looking:  
        student = still_looking[0]

        student_attempt(student, schools_assignements, still_looking, attempts, student_preferences, school_preferences, capacities)
        iterations += 1

    who_got_where = {}

    for school, matched_students in schools_assignements.items():
        for student in matched_students:
            who_got_where[student] = school
    
    return who_got_where, iterations



def student_attempt(student, 
                    schools_assignements, 
                    still_looking, 
                    attempts, 
                    student_preferences, 
                    school_preferences, 
                    capacities):

    if attempts[student] >= len(student_preferences[student]):
        still_looking.remove(student)  
        print(f"{student}, nobody wants it")
        return
        
    school = student_preferences[student][attempts[student]]  # nxt
    attempts[student] += 1  


    # left places
    if len(schools_assignements[school]) < capacities[school]:  
        accept(student, school, schools_assignements, still_looking)
    # remains to compare
    else:
        worst_student = least_preferred(school, schools_assignements[school], school_preferences) 
        evaluate(student, school, worst_student, schools_assignements, still_looking, school_preferences) 



def least_preferred(school, 
                    current_students, 
                    school_preferences):
    
    return max(current_students, key=lambda s: school_preferences[school].index(s)) # higher index = less preferred



def evaluate(student, 
            school, 
            worst_student, 
            schools_assignements, 
            still_looking, 
            school_preferences):
    
    new_student_rank = school_preferences[school].index(student)  
    worst_rank = school_preferences[school].index(worst_student)  

    if new_student_rank < worst_rank:  
        # remove the worst
        schools_assignements[school].remove(worst_student)  
        still_looking.append(worst_student)

        accept(student, school, schools_assignements, still_looking)  
    

def accept(student, 
           school, 
           schools_assignements, 
           unassigned_students):
    
    schools_assignements[school].append(student)  
    if student in unassigned_students:
        unassigned_students.remove(student)  
