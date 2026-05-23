

def safe_get_value(dictionary, key):

    try:
        return dictionary[key]
    except KeyError:
        print(f"Key {key} doesn't exist")



print(safe_get_value({'name': "Dato", 'age': "16"}, "subject"))




































