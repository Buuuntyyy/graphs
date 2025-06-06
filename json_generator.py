import json
import random

def json_generator():
    # Paramètres de génération
    num_schools = int(input("How many schools are available for students ? (Choose an integer)\n"))
    num_students = int(input("How many Student are serenading the schools ?\n"))

    # Générer les noms
    school_names = [f"School {i+1}" for i in range(num_schools)]
    student_names = [f"Student {i+1}" for i in range(num_students)]

    # Générer les écoles avec des capacités et des préférences aléatoires
    schools = []
    for name in school_names:
        capacity = random.randint(10, 50)  # ou une valeur fixe si tu préfères
        preferences = random.sample(student_names, len(student_names))
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
    data = {
        "schools": schools,
        "students": students
    }

    # Sauvegarder dans un fichier JSON
    with open("large_matching_data.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Fichier JSON généré avec succès avec {num_schools} écoles et {num_students} étudiants.")

    school_table = {
        "schools": [
            {
                "name": school["name"],
                "preferences": school["preferences"]
            }
            for school in data["schools"]
        ]
    }

    students_table = {
        "students": [
            {
                "name": students["name"],
                "preferences": students["preferences"]
            }
            for students in data["schools"]
        ]
    }