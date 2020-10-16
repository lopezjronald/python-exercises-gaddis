import numpy as np
import random
students = ['John', 'Mark', 'Luke', 'Matthew']
tests = [1, 2, 3, 4, 5, 6, 7, 8, 9]

student_tests = np.arange(len(students) * len(tests)).reshape(len(students), len(tests))

for student in range(len(students)):
    for test in range(len(tests)):
        student_tests[student][test] = random.randint(0, 100)



