

secret_number = 10

while True:
    guess_number = int(input("Guess the secret number: "))
    if guess_number > secret_number:
        print("Too high")
    elif guess_number < secret_number:
        print("Too low")
    else:
        break

print("Correct!")





































