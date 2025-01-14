attendance = []
count = 0
for student in range(1, 11):
    track = input(f"Enter attendance for student {student} (P/A): ")
    track = track.upper()
    attendance += track
    
P = attendance.count("P")
A = attendance.count("A")

print(f"Total students present: {P}")
print(f"Total students absent: {A}")

print("Attendance record:")

for i in attendance:
    count += 1
    if i == "P":
        print(f"Student {count}: Present ")
    else:
        print(f"Student {count}: Absent")
        
        
    


    