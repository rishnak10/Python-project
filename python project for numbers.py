#Q2: Input two numbers n1 and n2 and write a menu driven program using UDF's to do the following:
 #      a Count the number of prime in it
  #     b Count the number of perfect numbers in it
   #    c Count the number of palindromes in it

print("\n1.Count the number of prime in it,"
      "\n2.Count the number of perfect numbers in it,"
      "\n3.Count the number of palindromes in it")

def prime(n1,n2):
    cnt=0
    for i in range(n1,n2+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            cnt+=1
    print("no of primes=",cnt)
def perfect(n1,n2):
    cnt1=0
   
    for i in range(n1,n2+1):
        sum=0
        for j in range(1,i):
            if i%j==0:
                sum+=j
        if sum==i:
            cnt1+=1
    print("no of perfect no=",cnt1)
def pall(n1,n2):
    cnt=0
    nn=0
    for i in range(n1,n2+1):
        x=i
        n=0
        while x>0:
            d=x%10
            n=n*10+d
            x=x//10    
        if n==i:
              cnt+=1
    print("no of pall=",cnt)        

n1=int(input("enter num1"))
n2=int(input("enter num2"))
if n1>n2:
    n1,n2=n2,n1
ans='y'
while ans=='y':
    ch=int(input("enter choice"))
    if ch==1:
        prime(n1,n2)
    if ch==2:
        perfect(n1,n2)
    if ch==3:
        pall(n1,n2)
    ans=input("do you want to continue: y/n")
