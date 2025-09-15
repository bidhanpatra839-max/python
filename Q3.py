def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if is_rotation(str1, str2):
    print("Yes, it is a rotation.")
else:
    print("No, it is not a rotation.")
