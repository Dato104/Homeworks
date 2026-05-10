


dct_1 = {
    "name": "akaki",
    "age": 19,
    "location": "Tbilisi",
    "hobby": "gaming"
}


dct_2 = {
    "name": "anano",
    "age": 20,
    "iq": 160,
    "friends": 8
}





def dct_union(d1, d2):
    dct_3 = {}


    for key in d1:
        if key in d2:
            dct_3[key] = [d1[key], d2[key]]
        else:
            dct_3[key] = d1[key]

    for key in d2:
        if key not in dct_3:
            dct_3[key] = d2[key]

    return dct_3

print(dct_union(dct_1, dct_2))























































