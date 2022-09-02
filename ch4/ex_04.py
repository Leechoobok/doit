#1
'''
#def is_odd(number):
#    if number %2 == 1:
#        return True
#    else:
#        return False
is_odd = lambda x: True if x % 2 == 1 else False
print(is_odd(3))
print(is_odd(4))
'''

#2
#'''
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
        return result / len(args)
#'''

#3
'''
input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다." % total)
'''

#4
'''
print("you""need""python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you","need","python"]))
'''

#5
'''
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt",'r')
print(f2.read())
f2.close()
'''

#6
'''
user_input = input("저장할 내용을 입력하세요")
f = open("test.txt", 'a')
f.write(user_input)
f.close()
'''


#7
'''
f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f=open('test.txt', 'w')
f.write(body)
f.close()
'''