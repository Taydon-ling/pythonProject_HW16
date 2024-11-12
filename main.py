a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = b**2-4*a*c

if a == 0:
    print("No root")
elif d > 0:
    print("The are two roots, which are", (-b - d ** 0.5)/(2*a),"and", (-b + d ** 0.5)/(2*a))
elif d == 0:
    print("There is oen root, which is", (-b)/(2*a))
elif d < 0:
    print("There is no real root")
else:
    print("error")

quit()
