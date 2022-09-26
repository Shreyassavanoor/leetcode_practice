# We will consider two strings close if one can be obtained from the other, using the following operations:

# swap any two symbols in one of the strings,
# swap occurrences of any two existing symbols in one of the strings (for example, if your string contains both as and bs, you can change all as to bs and all the bs to as).
# Now you want to write a method that finds out whether the given strings are considered close, by the definition above.

# Example

# For A = "abbzccc" and B = "babzzcz", the output should be
# closeNames(A, B) = true.

# One possible way to transform "abbzccc" to "babzzcz" is this:

# "abbzccc" (this string is className)
# "babzccc" (swap positions of the first two characters)
# "babczzz" (switch all c and z characters)
# "babzzcz" (swap positions of the characters at indices 3 and 5; this string is now methodName)

# For A = "abcbdb" and B = "bbbcca", the output should be closeNames(A, B) = false.

from collections import Counter
def classNames( A, B):
    # count characters
    dictA = Counter(A)
    dictB = Counter(B)

    # we can't add new characters, only swap
    if dictA.keys() != dictB.keys() or len(A) != len(B):
        return False

    a_val_list = list(dictA.values())
    a_val_list.sort()
    b_val_list = list(dictB.values())
    b_val_list.sort()
    if a_val_list != b_val_list:
        return False

    return True

print(classNames("abbzccc", "babzzcz")) # True
print(classNames("abbbzcc", "babzzcz")) # True
print(classNames("abbbzcz", "babzzcz")) # True
print(classNames("abbczcz", "babzzcz")) # False
print(classNames("abbbzcf", "babzzcz")) # False
print(classNames("abbzzca", "babzzcz")) # False