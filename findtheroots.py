print("Finding the roots of a quadratic equation!")
print("Insert the equation's terms in the order of their degrees and follow the instructions.")
import math
a=int(input("Enter the first term's coefficient: "))
while a==0:
  a=int(input("If it is equal to zero, it's not a quadratic equation and we can't make the calculation. Insert a value different from 0: "))
b=int(input("Enter the second term's coefficient: "))
c=int(input("Enter the third term's coefficient: "))
delta=b**2-4*a*c
if delta>0:
  deltaroot=math.sqrt(delta)
  root1=(-b+deltaroot)/2*a
  root2=(-b-deltaroot)/2*a
  print("The equation roots are {} and {}".format(root1, root2))
elif delta==0:
  print(f"This equation has two equal roots, of value {(-b)/2*a}")
else:
  print("This equation has no real root.")
