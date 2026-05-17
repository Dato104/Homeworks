

current_user = {
    "username": "Dato",
    "role": "Moderator"
}



def role_required(role):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if current_user["role"] != role:
                print("Permission denied!")
                return
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator

@role_required("Moderator")
def delete_user(user_id):
    print(f"User with id {user_id} has been deleted")

@role_required("editor")
def edit_user(user_id):
    print(f"User with id {user_id} has been updated")

@role_required("user")
def create_user(first_name):
    print(f"User {first_name} has been created")


delete_user(10)
edit_user(20)
create_user(current_user["username"])




























