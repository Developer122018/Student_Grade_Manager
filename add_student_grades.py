def add_student_grade(p_student_list, p_student_score_dict ,  p_input_string_1 , p_input_string_2 , p_input_string_3 ,
p_entered_pupil_score_1 , p_entered_pupil_score_2 , p_entered_pupil_score_3):
    student_list = p_student_list
    student_score_dict = p_student_score_dict
    input_string_1 = p_input_string_1
    input_string_2 = p_input_string_2
    input_string_3 = p_input_string_3
    entered_english_score = p_entered_pupil_score_1
    entered_maths_score = p_entered_pupil_score_2
    entered_pupil_score_3 = p_entered_pupil_score_3
    entered_pupil_name=input('Which pupil would you like to add grades for?')
    entered_pupil_name = str(entered_pupil_name)

    if entered_pupil_name in student_list:
        input_string_1 = "Scores for " + entered_pupil_name + " in maths."
        input_string_2 = "Scores for " + entered_pupil_name + " in english."
        input_string_3 = "Scores for " + entered_pupil_name + " in science."
        input_string = input_string_1 , input_string_2 , input_string_3
        entered_english_score = input(input_string_1)
        entered_maths_score = input(input_string_2)
        entered_pupil_score_3 = input(input_string_3)
        entered_pupil_score = [entered_english_score ,entered_maths_score ,entered_pupil_score_3]
        student_score_dict[entered_pupil_name] = entered_pupil_score
    else:
        print('This student does not exist.Try again')

    return student_score_dict