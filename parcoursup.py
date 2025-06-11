"""
[PARCOURSUP]
1. Initialisation
   - tous les étudiants sont libres
   - toutes les écoles ont des places vides selon leur capacité
   - on suit le nombre de propositions faites par chaque étudiant

2. Boucle Principale :
    - Tant qu'il reste des étudiants libres : 
        - Un étudiant libre propose à l'école la plus haute dans sa liste de préférences à laquelle il n'a pas encore candidater.
        - 2 cas possibles :
            - Si l'école a de place libre -> elle accepte temporairement l'étudiant
            - Si l'école est pleine : 
                - Elle compare l'étudiant avec le pire étudiant actuel chosi par l'école
                - Si le nouveau est mieux classé : elle remplace le pire étudiant
                - Sinon elle refuse la proposition
        - Les étudiants rejetés retournent dans la liste des étudiants libres

3. Fin : 
    - Plus aucun étudiant ne peut/veut faire de propositions
    - La solution est stable (aucun couple préféré mutuellement n'existe)
"""


def stable_matching(students, schools, student_preferences, school_preferences, capacities):
    """
    Finds a stable matching between students and schools using our Stable Matching algorithm.
    
    Parameters:
        - students: list of student 
        - schools: list of school
        - student_preferences: a dictionary student <-> list of school
        - school_preferences: a dictionary school <-> list of student
        - capacities: a dictionary school <-> number of places available
    
    Return a dictonary student <-> matched school
    """
 
    unassigned = list(students)
    matches = {school: [] for school in schools}    
    proposals = {student : 0 for student in students}
      

    while unassigned:  
        student = unassigned[0]
        make_proposal(student, matches, unassigned, proposals, student_preferences, school_preferences, capacities)
    
    results = {}
    for school, matched_students in matches.items():
        for student in matched_students:
            results[student] = school
    return results


def make_proposal(student, matches, unassigned, proposals, student_preferences, school_preferences, capacities):
    """
    The function is responsible for managing the logic of a student proposing to a school.
    """

    if proposals[student] >= len(student_preferences[student]):
        unassigned.remove(student)  # the student has proposed to all schools
        return 
        
    school = student_preferences[student][proposals[student]]  # get the next school in his preferences
    proposals[student] += 1  #  increment the proposal count for the student

    if len(matches[school]) < capacities[school]:  # left places in the school
        accept(student, school, matches, unassigned)
    else:
        worst_student = ranking_student(school, matches[school], school_preferences)
        evaluate_candidate(student, school, worst_student, matches, unassigned, school_preferences)


def ranking_student(school, current_students, school_preferences):
    """
    Finds the worst ranked student currently matched with the school.
    """
    worst = None
    worst_rank = -1
    for student in current_students:
        rank = school_preferences[school].index(student)
        if rank > worst_rank:
            worst_rank = rank
            worst = student
    return worst


def evaluate_candidate(student, school, worst_student, matches, unassigned, school_preferences):
    """
    Handles decision-making when a a school is already matched with a student. 
    """
    new_student_rank = school_preferences[school].index(student)  
    worst_rank = school_preferences[school].index(worst_student)  

    if new_student_rank < worst_rank:  
        matches[school].remove(worst_student)  
        unassigned.append(worst_student)
        accept(student, school, matches, unassigned)
    else:
        if student not in unassigned:
            unassigned.append(student)


def accept(student, school, matches, unassigned):
    """
    Accepts a proposal from a student to a school
    """
    matches[school].append(student)  # match
    if student in unassigned:
        unassigned.remove(student)  # remove the student 

def main():

    students = ["corentin", "flavien", 'yoann', 'pierre']
    schools = ["ecole1", "ecole2", "ecole3"]

    student_preferences = {
        "corentin": ["ecole1", "ecole2", "ecole3"],
        "flavien": ["ecole2", "ecole1", "ecole3"],
        "yoann": ["ecole3", "ecole1", "ecole2"],
        "pierre": ["ecole1", "ecole3", "ecole2"]
    }

    school_preferences = {
        "ecole1": ["corentin", "pierre", "flavien", "yoann"],
        "ecole2": ["flavien", "corentin", "yoann", "pierre"],
        "ecole3": ["yoann", "pierre", "corentin", "flavien"]
    }
    capacities = {
        "ecole1": 1,
        "ecole2": 1,
        "ecole3": 1
    }

    print("========FIRST TEST=========")
    results = stable_matching(students, schools, student_preferences, school_preferences, capacities)
    print("Résultats de l'algo stable :")
    for student, school in results.items():
        print(f"{student} est affecté à {school}")
    print("---------END OF TEST 1---------")

    print("=========2ND TEST==========")

    print("---------END OF TEST 2---------")


main()


















