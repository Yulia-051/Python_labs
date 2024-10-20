numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
i = 0
sum_num = 0
save_i = 0
while(i < len(numbers)):
   if numbers[i] !=None:
       sum_num+=numbers[i]
   else:
       save_i=i
   i+=1
result = sum_num/len(numbers)
numbers[save_i] = result
print("Измененный список:", numbers)
