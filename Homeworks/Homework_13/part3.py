


try:
    number = int(input("Input a number: "))

except ValueError:
    print("Invalid input")

else:
    print(f"Result: {number ** 2}")

finally:
    print("Operation Completed")





















