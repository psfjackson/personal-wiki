# School subjects
subjects = ['physics', 'calculus', 'poetry', 'history']

# Subject grades
grades = [98, 97, 85, 88]

# Manual 2D list for subjects and grades
gradebook = [['physics', 98], ['calculus', 97], ['poetry', 85], ['history', 88]]
#print (gradebook)

#Add computer science grades
gradebook.append(['computer science', 100])

#Add visual arts grades
gradebook.append(['visual arts', 93])

#print (gradebook)

#Updating visual arts grade
gradebook[-1][-1] = gradebook[-1][-1] + 5
#print (gradebook)

#Converting poetry grade from numerical to pass/fail
gradebook[2].remove(85)
gradebook[2].append('Pass')
print (gradebook)

#Adding last years grades
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

full_gradebook = gradebook + last_semester_gradebook
print ('')
print (full_gradebook)
