


from functools import reduce


name_1 = input("შეიყვანეთ პირველი მოსწავლის სახელი: ")
math_1 = int(input("შეიყვანეთ პირველი მოსწავლის მათემატიკის ქულა: "))
history_1 = int(input("შეიყვანეთ პირველი მოსწავლის ისტორიის ქულა: "))
geography_1 = int(input("შეიყვანეთ პირველი მოსწავლის გეოგრაფიის ქულა: "))

name_2 = input("შეიყვანეთ მეორე მოსწავლის სახელი: ")
math_2 = int(input("შეიყვანეთ მეორე მოსწავლის მათემატიკის ქულა: "))
history_2 = int(input("შეიყვანეთ მეორე მოსწავლის ისტორიის ქულა: "))
geography_2 = int(input("შეიყვანეთ მეორე მოსწავლის გეოგრაფიის ქულა: "))




lst_students = [
    (name_1, math_1, history_1, geography_1),
    (name_2, math_2, history_2, geography_2)
 ]


average_score = list(map(lambda x: (x[0], (x[1] + x[2] + x[3]) / 3), lst_students))
print(average_score)

filtered_lst_students = list(filter(lambda x: x[1] >= 85, average_score))
print(f"მოსწავბლეები რომელთა საშუალო ქულა 85-ზე მეტი ან ტოლია: {filtered_lst_students}")

reversed_average_score = list(map(lambda x: x[0], sorted(average_score, key=lambda x: x[1], reverse=True)))
print(reversed_average_score)


















































































