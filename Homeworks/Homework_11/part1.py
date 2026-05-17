

def dec_operations(func):
    def wrapper(*args,**kwargs):

        for arg in args:
            if arg < 0:
                print("მოქმედება ხდება მხოლოდ დადებით რიცხვებზე")
                return
        return func(*args, **kwargs)
    return wrapper




@dec_operations
def math_operations(a, b):

    print(f"ჯამი: {a + b}")
    print(f"სხვაობა: {a - b}")
    print(f"ნამრავლი: {a * b}")
    if b > 0:
        print(f"განაყოფი: {a / b}")
    else:
        print("ნულზე გაყოფა შეუძლებელია")

math_operations(10,5)