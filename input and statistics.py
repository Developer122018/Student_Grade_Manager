import statistics
list_example = [2,3,4,5,6]
mean_of_list_example = statistics.mean(list_example)
median_of_list_example = statistics.median(list_example)
mode_of_list_example = statistics.mode(list_example)
#variance means the numbers that are different to the rest
#in python variance (when used) is printed as the amont of numbers which agree to the variance criter
variance_of_list_example = statistics.variance(list_example)
#standard deviation means the difference between means of different groups
#the code representitive for it is stdev
standard_deviaton_of_list_example = statistics.stdev(list_example)
print(mean_of_list_example,median_of_list_example,mode_of_list_example)
print(standard_deviaton_of_list_example , variance_of_list_example)