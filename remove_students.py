def remove_students(p_student_list,p_student_score_dict):
    student_list = p_student_list
    student_score_dict = p_student_score_dict
    student_to_be_removed = input('Which student do you want to delete?')

    if student_to_be_removed in student_list:
        student_list.remove(student_to_be_removed)
        if student_to_be_removed in student_score_dict:
            del student_score_dict[student_to_be_removed]
    else:
        print('This student is not in the list. Please try again')

    return student_list, student_score_dict