n=int(input())
b = 0
def devide(a):
    e=list(map(int,str(a)))
    x=a+sum(e)
    return x
#a는 x의 생성자다

while devide(b)!=n:
    if b==n:
        break
    else:
        b+=1




print(b)