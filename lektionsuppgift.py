"""
Uppgift 1 del a
"""

# from random import randint

# def summa_av_slumptal(tol):
#     sum = 0
#     i = 0

#     while sum < tol:
#         sum += randint(0, 11)
#         i += 1

#     return sum, i

# summa, count = summa_av_slumptal(21)
# print(f"Summan av {count} slumptal är lika med {summa}.")

"""
Uppgift 2 del a
"""

# def sum_of_series(N):
#     return round(sum([1/2*1/2**k for k in range(N)]), 3)

# print(sum_of_series(10))

"""
Uppgift 3 del a
"""

# def convert_and_add(lst_1, lst_2):
#     return [float(lst_1[i]) + int(lst_2[i]) for i in range(len(lst_1))]

# lst_1 = ["1.1","2.4","11.0"]
# lst_2 = ["3","4","3"]

# print(convert_and_add(lst_1, lst_2))

"""
Uppgift 4 del a
"""

# def temp_average(temp_1, temp_2):

#     sorted_temp_2 = {y: x for x, y in temp_2.items()}
    
#     average = {}
#     for i in temp_1:
#         temp_1_val = temp_1[i]
#         temp_2_val = sorted_temp_2[i]
#         avg_temp = round((temp_1_val + temp_2_val) / 2, 2)
#         average[i] = avg_temp

#     return average

# temp_1 = {"12":-2.4,"13":-2.0,"14":-2.1}
# temp_2 = {-2.3:"12",-1.9:"13",-2.2:"14"}

# average = temp_average(temp_1,temp_2)
# for m in average:
#     print(f" Kl {m} var temperaturen {average[m]} grader Celsius.")

"""
Uppgift 5 del b
"""

# def resistance(lst):
#     return 

# rList1 = [3000, 3000, 3000]
# rList2 = [1000, 2000, 3000]
# print(resistance(rList1))
# print(resistance(rList2))

"""
Uppgift 6 del b
"""

# def sum_with_limit(lst, limit):
#     sum = 0
#     i = 0

#     while sum < limit and i < len(lst):
#         sum += lst[i]
#         i += 1
#     return i, sum

# x = [2, 5, 1, 4, 7, 3, 11,1,20]
# limit = 10
# count,summa = sum_with_limit(x, limit)
# print(f"The sum of {count} elements larger than {limit} is {summa}.")

"""
Uppgift 7 del b
"""

# def convert_cm_to_m(lengths_in_cm):
#     res = [int(lengths_in_cm[i])/100 for i in range(len(lengths_in_cm))]
#     return list(map(str, res))

# heights_in_cm = ["165", "161", "183", "195"]
# heights_in_m = convert_cm_to_m(heights_in_cm)
# for h_cm, h_m in zip(heights_in_cm, heights_in_m):
#     print(h_cm + " cm = " + h_m + " m.")

"""
Uppgift 8 del b
"""

# def list_of_cheap_meals(menu):
#     res = []
#     for key, value in menu.items():
#         if value < 100:  
#             res.append(key)         
#     return res

# menu = {"burger": 89,"pizza": 129,"salad": 99,"fish": 119}
# print(list_of_cheap_meals(menu))