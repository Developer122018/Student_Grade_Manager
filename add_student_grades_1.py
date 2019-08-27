def add_student_grade_1(p_student_list, p_student_score_dict , p_list_of_subjects):
    student_list = p_student_list
    student_score_dict = p_student_score_dict
    list_of_subjects = p_list_of_subjects
    entered_pupil_name=input('Which pupil would you like to add grades for?')
    entered_pupil_name = str(entered_pupil_name)
    scores_of_student = []

    if entered_pupil_name in student_list:
        length_of_subjects = len(list_of_subjects)
        for x in range(0,length_of_subjects):
            list_of_scores= input('Scores of '+entered_pupil_name+' '+list_of_subjects[x]+':')
            scores_of_student.append(list_of_scores)
        student_score_dict[entered_pupil_name] = scores_of_student
        print(student_score_dict)
    else:
        print('This student does not exist.Try again')

    return student_score_dict