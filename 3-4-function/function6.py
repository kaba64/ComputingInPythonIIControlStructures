def reverse(a_string):
    rev = ""
    for i in range(len(a_string)-1, -1, -1):
        rev = rev + a_string[i]

    return rev

#You may change or add to the following lines.
#reverse("This string should be reversed!")
print(reverse("This string should be reversed!"))
