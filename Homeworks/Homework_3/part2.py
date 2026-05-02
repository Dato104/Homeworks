


score = input("შეიყვანეთ თქვენს მიერ მიღებული ქულა: ")
print(f"თქვენი ქულაა: {score}")

attendance = input(f"შეიყვანეთ თქვენი დასწრების მაჩვენებელი: ")

print(f"თქვენი დასწრებაა: {attendance}%")

score = int(score)
attendance = int(attendance)

if score > 60 and attendance > 75:
    print("თქვენ ჩააბარეთ!!!")
else:
    print("თქვენ ვერ ჩააბარეთ")































