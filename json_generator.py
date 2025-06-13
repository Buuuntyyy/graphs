import json
import random
from faker import Faker

def json_generator():
    fake_student = Faker('en_US')
    fake_schools = Faker()

    prefixes = ['Universite', 'Institut', 'Ecole', 'Academie', 'College', 'Universite Technologique']
    locations = [fake_schools.city() for _ in range(10)]
    fields = ['des Sciences', 'de Technologie', 'd\'Ingenierie', 'de Medecine', 'des Arts', 'du Droit']

    # Paramètres de génération
    num_schools = int(input("How many schools are available for students ? (Choose an integer)\n"))
    num_students = int(input("How many Student are serenading the schools ?\n"))
    available_capacity = int(input("Choose the maximum capacity of schools ? (Minimum : 5)")) ; assert available_capacity > 5, "Max capacity must greater than 5"
    # Générer les noms
    school_names = [f"{random.choice(prefixes)} {random.choice(locations)} {random.choice(fields)}" for i in range(num_schools)]
    student_names = [f"{fake_student.first_name()}" for i in range(num_students)]

    # Générer les écoles avec des capacités et des préférences aléatoires
    schools = []
    total_capacity = 0
    for name in school_names:
        capacity = random.randint(5, available_capacity)  # ou une valeur fixe si tu préfères
        preferences = random.sample(student_names, len(student_names))
        total_capacity = capacity + total_capacity
        schools.append({
            "name": name,
            "capacity": capacity,
            "preferences": preferences
        })

    # Générer les étudiants avec des préférences aléatoires
    students = []
    for name in student_names:
        preferences = random.sample(school_names, len(school_names))
        students.append({
            "name": name,
            "preferences": preferences
        })

    # Regrouper les données
    data1 = {
        "schools": schools,
    }

    data2 = {
        "students": students
    }

    # Sauvegarder dans un fichier JSON
    with open("schools.json", "w") as f:
        json.dump(data1, f, indent=4)

    with open("students.json", "w") as f:
        json.dump(data2, f, indent=4)

    print(f"JSON file successfuly generated {num_schools} school and {num_students} students.")
    print("Total capacity is : " + str(total_capacity))