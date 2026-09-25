students = {

'student1':{'name': 'Rocky','score':85},  
'student2':{'name': 'Travis', 'score': 90},
'student3':{'name': 'Kendrick', 'score': 78},
'student4':{'name': 'Aubrey', 'score':95},
'student5':{'name':'Jack','score':81}
}

total=0

for student,marks in students.items():
   student_score = marks["score"]
   total += student_score

print("The average of the students are:",total/len(students))

Max = max(info['score'] for info in students.values())
print('The highest score is:',Max)

Min = min(info['score'] for info in students.values())
print("The lowest score is:",Min)

key = input("Enter a candidate's name: ")

for candidate in students.values():
    if candidate["name"].lower() == key.lower():
        print(candidate)
        break
else:
        print("Oops..looks like the candidate does not exist.")

print(students)