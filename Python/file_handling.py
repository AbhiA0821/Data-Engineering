import csv
import json

# -------------------------
# CSV Processing
# -------------------------

with open("patients.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# -------------------------
# JSON Processing
# -------------------------

patient = {
    "patient_id": 101,
    "name": "Rahul",
    "heart_rate": 82
}

with open("patient.json", "w") as file:
    json.dump(patient, file, indent=4)


with open("patient.json", "r") as file:
    data = json.load(file)

print(data)