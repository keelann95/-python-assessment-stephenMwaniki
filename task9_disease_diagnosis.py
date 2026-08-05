
# a. Welcome message
print("=" * 45)
print("     WELCOME TO JESHI HOSPITAL")
print("=" * 45)

# b. Capture patient details
patient_name = input("Enter patient name: ")
gender = input("Enter gender: ")
age = input("Enter age: ")
residence = input("Enter place of residence: ")

# c. Capture two symptoms
print("\nCommon symptoms include: fever, headache, chills, cough,")
print("thirst, fatigue, joint pain, chest pain")
symptom1 = input("Enter Symptom 1: ").strip().lower()
symptom2 = input("Enter Symptom 2: ").strip().lower()

symptoms = {symptom1, symptom2}

# d. Match symptom pairs to a diagnosis
if symptoms == {"fever", "headache"}:
    diagnosis = "Malaria"
elif symptoms == {"fever", "chills"}:
    diagnosis = "Malaria"
elif symptoms == {"fever", "fatigue"}:
    diagnosis = "Typhoid"
elif symptoms == {"headache", "fatigue"}:
    diagnosis = "Typhoid"
elif symptoms == {"cough", "chest pain"}:
    diagnosis = "Pneumonia"
elif symptoms == {"fever", "cough"}:
    diagnosis = "Pneumonia"
elif symptoms == {"thirst", "fatigue"}:
    diagnosis = "Diabetes"
elif symptoms == {"thirst", "headache"}:
    diagnosis = "Diabetes"
else:
    # e. Handle unrecognized symptom combinations
    diagnosis = "Unrecognized symptom combination. Please consult a doctor."

# f. Display formatted output
print("\n" + "=" * 45)
print("           DIAGNOSIS REPORT")
print("=" * 45)
print(f"Patient Name  : {patient_name}")
print(f"Gender        : {gender}")
print(f"Age           : {age}")
print(f"Residence     : {residence}")
print("-" * 45)
print(f"Symptom 1     : {symptom1}")
print(f"Symptom 2     : {symptom2}")
print("-" * 45)
print(f"Diagnosis     : {diagnosis}")
print("=" * 45)