

"""
Main module
    Infinite loop
    Ask user for choice
    Call module according to user choice
    ask if user wants to continue or exit
    has a student list and grade dict
    call main

Module Add_student_grades
    takes input as student list, student to grades dict
    Ask for which student grades to be added
    Add grades for the student
    return grades


Module Remove student
    takes input as student list, student to grades dict
    Ask which student to be deleted
    Confirm that user wants to delete the student 
    Check if student is in the list else give warning message 
    Delete student
    return student list



Module student score average
    takes  student to grades dict
    Ask which student average to be calculated
    Convert score string to list
    calculate average
"""
student_list = ('Girisha','Sonu','Atul','Aadya','Anshu')
student_score_dict = {'Girisha':'93,98,96','Sonu':'89,87,81','Atul':'56,78,67','Aadya':'89,85,80','Anshu':'89,81,82'}

def add_student_grades_2(student_list, student_score_dict):
    print('''
    Welcome to Grade Enter Center
    [1] New Grade
    [2] Exit
    ''')

    #Want to add the pupil name to the dictionary
    #Get student name and makes in various subject and add them to dictionary
    user_action_2 = input('Which one would you like to choose(please select a number)')
    pupil_dict = {'Sonu': '86,89,91,94', 'Atul': '34,27,52,16', 'Girisha': '98,97,93,96'}
    if user_action_2 == '2':
        while 1 < 2 :
            to_exit_or_not = input('Would you like to exit ?')
            to_exit_or_not = to_exit_or_not.lower()
            if to_exit_or_not == 'yes':
                print('Goodbye')
                break
            if to_exit_or_not == 'no':
                pass
            else:
                to_exit_or_not = input('Would you like to exit(Yes or No)?')
                to_exit_or_not = to_exit_or_not.lower()

    if user_action_2 == '1':
        while 1 < 2 :
            name_grade_input = input('Which pupil would you like to add grades for?' )
            if name_grade_input in pupil_dict:
                grade_input = input('What grade should he/she get? ')
                new_set = {name_grade_input:grade_input}
                pupil_dict.__contains__({new_set})
                print(pupil_dict)
add_student_grades_2(student_score_dict, student_list)