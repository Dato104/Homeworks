



def calculate(*args, operation):


    if operation == "sum":
        print(f"რიცხვების ჯამი: {sum(args)}")
    elif operation == "min":
        print(f"მინიმალური რიცხვი: {min(args)}")
    elif operation == "max":
        print(f"მაქსიმალური რიცხვი: {max(args)}")
    elif operation == "mult":
        count = 1
        for i in args:
            count *= i
        print(f"რიცხვთა ნამრავლი: {count}")




calculate(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, operation = "sum")
calculate(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, operation = "min")
calculate(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, operation = "max")
calculate(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, operation = "mult")



































































