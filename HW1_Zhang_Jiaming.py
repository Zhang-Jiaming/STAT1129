#Question 1
list1 = list(range(30, 61, 5))
reverse_list1 = list1[::-1]
reverse_list1.insert(0, 65)
print(reverse_list1)



#Question 2
list2 = []
for i in range(0, 21):
    list2.append(i)
list2.remove(0)
list2_length = len(list2)
list2_max = max(list2)
list2_min = min(list2)
list2_sum = sum(list2)

print("The length of the list is", list2_length)
print("The max value of the list is", list2_max)
print("The min value of the list is", list2_min)
print("The sum value of the list is", list2_sum)



#Question 3
weather = {"sunny":"play", "rainy":"watch TV", "cloudy":"walk"}
for j in weather:
    print("When", j, "let us", weather[j])
weather['snowy'] = "ski"
