



lst = ["math", "biology", "math", "history", "art", "history"]




def counter(lst):
    dct = {}
    for subject in lst:
        if subject not in dct:
            dct[subject] = 1

        else:
            dct[subject] += 1

    return dct

print(lst)
print(counter(lst))























































