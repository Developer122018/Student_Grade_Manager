def student_averages(p_student_list, p_averages_dict , p_student_score_dict):
    import statistics as s
    student_list = p_student_list
    averages_dict = p_averages_dict
    student_score_dict = p_student_score_dict
    student_whose_average_to_be_calculated = input("Which student's average do you want to calculate? ")

    if student_whose_average_to_be_calculated in student_list:
        value_from_dict = student_score_dict.get(student_whose_average_to_be_calculated)
        average_of_person = sum(int(value_from_dict))/len(value_from_dict)
        averages_dict[student_whose_average_to_be_calculated] = average_of_person
    else:
        print('This student is not defined.')

    return averages_dict
