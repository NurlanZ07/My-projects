def m():
    a= int(input("type the a"))
    b= int(input("type the b"))
    c= int(input("type the c"))

    print(sol(a,b,c))
def sol(a,b,c):
    return ((pow(b,2)-4*a*c)**(1/2))
m()
