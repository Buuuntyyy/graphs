import json
import pandas as pd 

from student_proposes import match_student_to_schools
from school_proposes import match_schools_to_student
import json_generator


def load_data():
    with open("schools.json", 'r', encoding='utf-8') as f:
        df_schools = pd.json_normalize(json.load(f)["schools"])
    with open('students.json', 'r', encoding='utf-8') as f:
        df_students = pd.json_normalize(json.load(f)["students"])

    students = df_students['name'].tolist()
    schools = df_schools['name'].tolist()

    student_preferences = df_students.set_index('name')['preferences'].to_dict()
    school_preferences = df_schools.set_index('name')['preferences'].to_dict()
    capacities = df_schools.set_index('name')['capacity'].to_dict()

    return students, schools, student_preferences, school_preferences, capacities

def main():

    json_generator.json_generator()

    students, schools, student_preferences, school_preferences, capacities = load_data()

    results_student, days_students = match_student_to_schools(students, schools, student_preferences, school_preferences, capacities)
    results_school, days_schools = match_schools_to_student(students, schools, student_preferences, school_preferences, capacities)

    df_student = pd.DataFrame(list(results_student.items()), columns=['Student', 'School (student proposes)'])
    df_school = pd.DataFrame(list(results_school.items()), columns=['Student', 'School (school proposes)'])
    print(pd.merge(df_student, df_school, on='Student'))

    print(days_students, "iterations for students proposing")
    print(days_schools, "iterations for schools proposing")

    output = {
        "student_proposing": {
            "matching": results_student,
            "iterations": days_students
        },
        "school_proposing": {
            "matching": results_school,
            "iterations": days_schools
        }
    }

    with open("results.json", "w") as f:
        json.dump(output, f, indent=4)


if __name__ == "__main__":
    main()