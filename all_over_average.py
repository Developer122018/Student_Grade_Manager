def all_over_average(p_list_of_subjects,p_student_score_dict , p_average_dict):
    import statistics as s
    list_of_subjects = p_list_of_subjects
    average_dict = p_average_dict
    student_score_dict = p_student_score_dict
    subject_whose_average_to_be_calculated = str(input('Which subject would you like to calculate the average for?'))
    subject_whose_average_to_be_calculated = subject_whose_average_to_be_calculated.lower()

    if subject_whose_average_to_be_calculated in list_of_subjects:
        length_of_list_of_subjects = len(list_of_subjects)
        for x in range(0,length_of_list_of_subjects):
            if subject_whose_average_to_be_calculated == list_of_subjects[x]:
                my_list = [elem[x] for elem in student_score_dict.values()]
                my_list_int = map(int,my_list)
                mean_of_list = s.mean(my_list_int)
                average_dict[subject_whose_average_to_be_calculated] = mean_of_list
                print(average_dict)
                break
            else:
                pass
    else:
        print('Try again')