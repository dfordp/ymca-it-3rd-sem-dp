#WAP TO FIND THE QUADRITIC EQN'S ROOTS
import math
a=int(input("Enter value of coffecient of x^2"))
b=int(input("Enter value of coffecient of x"))
c=int(input("Enter value of constant term"))
D=b*b-4*a*c
if(D<0):
    print("Roots are not real")
elif(D==0):
    print("Root are real and equal")
    ans=-b/2*a
    print(ans)
else:
    print("Roots are real and distis")
    d=math.sqrt(D)
    ans1=(-b+d)/2*a
    ans2=(-b-d)/2*a
    print(ans1)
    print(ans2)


#WAP TO TO READ TWO POSTIVE NO. AND PRINT ALL EVEN NP. BETWEEN THEM
a=int(input("Enter value of starting point"))
b=int(input("Enter value of starting point"))
if(a<0 or b<0):
    print("Invalid Input")
n=a+1
while(n<=b):
    if(n%2==0):
        print(n)
    n=n+1

#WAP TO READ A NO. AND RETURN IT'S SUM IF NO. IS EVEN AND PRODUCT IF NO. IS ODD

num=int(input("Enter value of no."))
sum=0
product=1
if(num%2==0):
    while(num>0):
        temp=num%10
        sum=sum+temp
        num=num//10
    print("sum =", abs(sum))
else:
    while(num>0):
        temp=num%10
        product=product*temp
        num=num//10
    print("product =",abs(product))

#Day before input date
Days_in_a_month=[31,28,31,30,31,30,31,31,30,31,30,31]

def isleap(year):
    if(year%400==0 or (year%4==0 and year%100!=0)):
        Days_in_a_month[1]=29
        
day=int(input("Enter day"))
month=int(input("Enter month"))
year=int(input("Enter year"))

nd=day
nm=month
ny=year

if(nd==1 and nm==1):
    nd=31
    nm=12
    ny=ny-1
elif(nd==1):
    nm-=1
    if(nm==2):
        isleap(ny)
    nd=Days_in_a_month[nm-1]
else:
    nd=nd-1
print(nd,"/",nm,"/",ny)

#WAP to print the sum of the series 

sum=0
l=1
h=8
while(l<=8 and h>=1):
    sum=sum+l**h
    l=l+1
    h=h-1
print(sum)

    

# problem Statement: Write a program to compute  using trapezoidal rule.

f = lambda n: ((2 * n) + 4)

def integrate (lower_range, upper_range, n):
     
    # Grid spacing
    grid_space = (upper_range - lower_range) / n
     
    # Computing sum of first and last terms
    # in above formula
    s = (f(lower_range) + f(upper_range))
 
    # Adding middle terms in above formula
    i = 1
    while i < n:
        s += 2 * f(lower_range + i * grid_space)
        i += 1
         
    # h/2 indicates (b-a)/2n.
    # Multiplying h/2 with s.
    return ((grid_space / 2) * s)

print(integrate(5, 10, 10000))   


#WAP # Python program for implementation
# of Bisection Method for
# solving equations
# The function is 2x3+4x2+x-3
def func(x):
    return 2*x**3+4*x**2+x-3

# Prints root of func(x)
# with error of EPSILON
def bisection(a,b):

    if (func(a) * func(b) >= 0):
        print("You have not assumed right a and b\n")
        return

    c = a
    while ((b-a) >= 0.01):

        # Find middle point
        c = (a+b)/2

        # Check if middle point is root
        if (func(c) == 0.0):
            break

        # Decide the side to repeat the steps
        if (func(c)*func(a) < 0):
            b = c
        else:
            a = c

    print("The value of root is : ","%.4f"%c)

# Driver code
# Initial values assumed
a =-200
b = 300
bisection(a, b)

