
"""
num = int (input("Enter number: "))
temp = num
rev = 0
while(num>0):
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
    if(temp == rev):
        print("The {0} is palindrome." .format(temp))
    else:
        print("The {0} is not a palindrome." .format(temp))

"""
""""
string = 'python'
rev_str = " "
for s in string:
    rev_str = s + rev_str
    print(rev_str)
    """
"""
s = input("Enter a string: ")
for word in s.split():
    print(word[::-1],end= " ")
"""

str1 = input("Enter a string: ")
index = -1
while index >= -(len(str1)):
    print("subscript[",index,"] : " + str1[index])
    index += -1