# Python program to demonstrate the use of sets and perform set operations # Managing student enrollments in multiple exams
# Sample student enrollments
cet_students = {"Alice", "Bob", "Charlie", "David"} 
jee_students = {"Charlie", "Eve", "Frank", "Alice"}
neet_students = {"George", "Hannah", "Alice", "Eve"} # Display the enrollments
print("Students enrolled in CET:", cet_students) 
print("Students enrolled in JEE:", jee_students) 
print("Students enrolled in NEET:", neet_students) # Union: Students appearing for at least one exam
all_students = cet_students.union(jee_students, neet_students)
print("\nStudents appearing for at least one exam:", all_students)
#Intersection: Students appearing for all three exams
common_students = cet_students.intersection(jee_students, neet_students) 
 print("\nStudents appearing for all three exams:", common_students)
# Difference: Students appearing for CET but not JEE cet_not_jee = cet_students.difference(jee_students) print("\nStudents appearing for CET but not JEE:", cet_not_jee)
# Symmetric Difference: Students appearing in CET or JEE but not both cet_or_jee_not_both = cet_students.symmetric_difference(jee_students) print("\nStudents appearing in CET or JEE but not both:", cet_or_jee_not_both) # Check if a specific student is enrolled in any exam
student_name = "Alice"
is_enrolled = student_name in all_students
print(f"\nIs {student_name} enrolled in any exam?", is_enrolled) # Add a new student to a specific exam enrollment cet_students.add("Ivy")
print("\nUpdated CET enrollment after adding Ivy:", cet_students) # Remove a student from an exam enrollment jee_students.discard("Frank")
print("\nUpdated JEE enrollment after removing Frank:", jee_students)