import json

students = {
    "Name": "Mannanvirr",
    "Marks": 100
}

with open ("student.json", "w") as file:
    json.dump(students, file)