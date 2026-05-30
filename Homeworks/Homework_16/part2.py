
class Profile:
    def __init__(self, password):
        self.__password = password

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        if password != self.__password:
            return f"Password is incorrect"
        return f"Password is correct"

    def change_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            return f"Password changed successfully"
        return f"Password is incorrect"

profile_1 = Profile("paris123")

print(profile_1.password)
print(profile_1.check_password("paris123"))
print(profile_1.change_password("paris123", "paris2"))
print(profile_1.password)




























