
def match_schools_to_student(students, 
                             schools, 
                             student_preferences, 
                             school_preferences, 
                             capacities):
    """
    [School-proposing version]
    
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

    attempts = {school: 0 for school in schools}
    schools_assignements = {school: [] for school in schools}
    student_matches = {student: None for student in students}
    schools_available = [school for school in schools if capacities[school] > 0]
    
    iterations = 0

    while schools_available:
        school = schools_available[0]

        propose_students(school, schools_assignements, student_matches, schools_available, attempts, school_preferences, student_preferences, capacities)
        iterations += 1

    who_got_where = {}

    for school, matched_students in schools_assignements.items():
        for student in matched_students:
            who_got_where[student] = school
    return who_got_where, iterations


def propose_students(school, 
                          schools_assignements, 
                          student_matches, 
                          schools_available, 
                          attempts, 
                          school_preferences, 
                          student_preferences, 
                          capacities):
    
    while len(schools_assignements[school]) < capacities[school] and attempts[school] < len(school_preferences[school]):
        
        student = school_preferences[school][attempts[school]] # nxt student
        attempts[school] += 1

        assigned_school = student_matches[student] 

        if assigned_school is None: # nt mached
            assign(student, school, schools_assignements, student_matches)
        else:
            if prefers(student, school, assigned_school, student_preferences):
                schools_assignements[assigned_school].remove(student) 
                assign(student, school, schools_assignements, student_matches)

    filled = len(schools_assignements[school]) == capacities[school]
    proposed_to_all = attempts[school] == len(school_preferences[school])

    if filled:
        print(f"School '{school} has reached its capacity of {capacities[school]}")
    if proposed_to_all:
        print(f"School '{school}' has proposed to all students in its preference")

    # 2 cases : school filled | has proposed to all
    if filled or proposed_to_all:
        if school in schools_available:
            schools_available.remove(school)



def prefers(student, 
            new_school, 
            current_school, 
            student_preferences):
    
    pref_list = student_preferences[student]
    return pref_list.index(new_school) < pref_list.index(current_school)
   


def assign(
        student, 
        school, 
        schools_assignements, 
        student_matches):
    
    schools_assignements[school].append(student)
    student_matches[student] = school
    