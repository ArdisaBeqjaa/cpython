import sys

ASK_FOR_INPUT=False
name=input('what is your name:\n')
age=input('enter age:\n')
age_int=int(age)-1
print(f'your name is:{name} and your age is {age_int}')
# second way we need to match the bracets with the argumets of the format funcion
print('your name is {} and your age is {}'.format(name,age))
# multiple input
x,y,z=input('enter 3 numners').split(" ") if ASK_FOR_INPUT else[1,2,3]
print(f"x{x} y{y}")
# split merr input kudo ku gjen space krijon nj array
# nk kemi array por list ,si arraylist ne java
# nk kemi turnery operator 

# how do we modify the list!!!!!!, RANGE

a=[1,2,3]
a1=a[0]
# unpack the elements
# multipe values 
# name arguments
# redirenct n nj file me file-sys.
# kjo file kur ka open ta printon n nj file, w 
# vec n colsoe file=sys.stdout

print('hello',"world",sep=",",file=open('open.txt','w'))
# iterate me for each ose me for loop
for x in a:
    print(x)

for i in range (len(a)):
    print (a[i])
    
    
