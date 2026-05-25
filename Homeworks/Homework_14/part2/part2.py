


def journal():
     while True:
        text = input("შეიყვანეთ ტექსტი ჭურნალში დასამატებლად(შეიყვანეთ exit პროგრამიდან გამოსასვლელად): ")
        if text == 'exit':
            break
        try:
            with open('journal.txt', 'a') as file:
                file.write(text + "\n")
        except Exception as e:
            print(e)

journal()











































































