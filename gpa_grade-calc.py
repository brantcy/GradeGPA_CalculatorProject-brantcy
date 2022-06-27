##############################################################################
# Sofware Req Doc: grade-calc Task List.docx
# Release Date: 14Jun22
# Code Author: Chenoweth, Brant
#
# Description:  
#   grade-calc.py is a Python program designed to calculate individual course
#   grades and provide average as well as letter grade, additionally it will
#   calculate an overall GPA. Detailed requirements are available via the 
#   "grade-calc Task List.docx" file.
##############################################################################
# Req 1    Allow the user to enter the course name and credit value.
course = input(f'Please enter the name of your course: ')
while True:
    cred = input(f'How many credits is your {course.title()} course worth?\n\
Please enter a whole number between 1 and 9:')
    if cred not in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
        print('Please enter a positive number.')
    else:
        cred = int(cred)
        break
print(f'\nYour {course.title()} course is worth {cred} credits.')
print(f"\nLet's get some assignment groups entered and grading weights \
established for your {course} course.\n")
# Req 2    Allow the user to enter assignment groups and weights.
assn_groups = {}
# Remind that group weight total must equal 100!
print("Sum of group weights must equal 100! \
\nUse whole numbers for percentages 'i.e. 35 for 35%'")   
req_2 = True
while req_2:
    # Prompt for group name and weight value.
    group = input("\nPlease enter group name: ")
    weight = input("Please enter the weight for this category: ")
    # Store the response in the dictionary.
    assn_groups.update({group:int(weight)})
# Req 2.1 Find out if more entries are required by checking weights total.
    repeat = assn_groups.values()
    print(f"Current weights are:")
    for current in assn_groups.items():
        print(current)
    repeat = sum(repeat)
    print(f"Current weight total is: {repeat}")
    if repeat == 100:
        req_2 = False
# Req 3    Ask user to enter number of assignments for each group.
grp_names = []
grp_weights = []
assn_tot = []
req_3 = True
while req_3:
    for x, y in assn_groups.items():
        quantity = input(f"\nPlease enter number of assignments for {x}: ")
        grp_names.append(x)
        grp_weights.append(y)
        assn_tot.append(quantity)
    if len(assn_tot) == len(assn_groups):
        req_3 = False
grp_weights = list(map(int, grp_weights))
assn_tot = list(map(int, assn_tot))

print(assn_groups)        
print(assn_tot)
print(grp_weights)
print(grp_names)






# Req 4    Make function that:
    # 4.1  Allows user to enter a grade for the number of
    #      assignments in a particular group.
    # 4.2  Calculates and returns the average grade for that group.
grade_amnt = []
g_avg = int()


req_4a = True
while req_4a:
    for grp in grp_names:
        temp_grade = input(f"\nEnter grade for each {grp}: ")
        for asn in assn_tot:
            div = int(asn)
            assn_grades.append(temp_grade)
        if asn -1 == 0:
            break
    if len(assn_grades) == len(grp_names):
        assn_grades = list(map(int, assn_grades))
        grp_total = sum(assn_grades)
        answer = (grp_total//div)
        g_avg = int(answer)
        req_4a = False

# Req 5    Make function that:
    #      Uses each group grade avg to find course avg using given weights.
    #      Returns the course avgerage


# Req 6    Make function that:
    #      Takes course average grade and assigns a letter grade per table.
    #      Returns a letter grade for the course.


# Req 7    Ask user if they want to calculate the grade for another course.
    # Yes  > re-run necessary code to do so, including this rerun step.
    # No   > Ask if they would like the program to calculate the overall GPA.
        # Yes  > Using a function, calculate semester GPA.
        # No   > Provide calc summary and thank them for using the program.
        # Else > For invalid entries, have them re-enter an answer.

# Req 8    Provide summary of calculations displayed in an organized manner.