def main():
    import sys
    from add_student_grades_1 import add_student_grade_1
    from remove_students import remove_students
    from student_averages import student_averages
    username_password_dict = {'Momma': 'teacher345', 'Python': 'pycharm', 'RUBINA': 'redford' , 'lob':'by'}
    username_list = list(username_password_dict.keys())
    counter_authentication = 0
    student_score_dict = {}
    averages_dict = {}
    all_over_averages_dict = {}
    entered_pupil_score_1 = 0
    entered_pupil_score_2 = 0
    entered_pupil_score_3 = 0
    ## Authentication for client ##
    for x in range(10):
        username = input('Username? ')
        password = input('Password? ')
        if username in username_list and password == username_password_dict.get(username):
            print('Acess Granted')
            print('Welcome',username)
            break
        else:
            print('Acess denied. Please try again')
            counter_authentication += 1
        if counter_authentication == 9:
            print('Oh dear! Your username/password does not match our data.Please try again later.')
            sys.exit()

    student_list = list(input('Who are your students?').split(","))
    print(student_list)
    list_of_subjects = list(input('What subjects do you want to add ?').split(','))
    print(list_of_subjects)
    #list_of_subjects = list(input('What are the subjects that they took?'))

    #Ask user for choice
    while 1 < 2:
        print('''
        Welcome To Grade Central
        [1]-Enter Grades
        [2]-Remove Students
        [3]- Student Averages
        [4]-Average for the whole grade
        [5]-Exit
        
        ''')
        try:
            user_action = int(input('What would you like to do today?'))
        except ValueError as error:
            print('Wrong user input.')
            continue
        if user_action == 1:
            student_score_dict = add_student_grade_1(student_list,student_score_dict,list_of_subjects)
        elif user_action == 2:
            student_list, student_score_dict = remove_students(student_list,student_score_dict)
            print(student_score_dict)
            print(student_list)
        elif user_action == 3:
            averages_dict = student_averages(student_list , averages_dict , student_score_dict )
            print(averages_dict)
        elif user_action == 4:
            from all_over_average import  all_over_average
            all_over_average(list_of_subjects ,student_score_dict,all_over_averages_dict)
        elif user_action == 5 :
            print('goodbye')
            sys.exit()
        else:
            print('Wrong user input.' )


main()
