# python expression nqs duam t printojm dicka me forloop e bejm me *
print('hi'*2)
a=10
a=3
print(a)


# print("reault"+a)
# strings can me "" ose ''
full_name='jon smith'
age= 20
is_true=True

# concate nje string me !data type me funciton str
print(full_name+str(age)+str(is_true ))


# input from the user
color=input('what is your favorite color?\n')
print("my favorite color is "+color)


# type conversion
birth_year=input('Birth year:\n')
age=2023-int(birth_year)
print(age) 
pound=input('enter weight in pounds')
kilo=float(pound)*2.204462
print(kilo)

# strings
#  perdorim singe ose doulbe quotes nqs vet strig duket t ket nj single quote ne e mledhim me ""
# strigns ARE ARRAYS OF BYTES
# python does not have a char data type
coruse="ardisa"
print(coruse[0])
# nqs duam te marrim char e fundit bejm -1
print(coruse[-1])
# nqs dua te bej nje substrign, copy or cloe a strign
cr=coruse[0:2]
# kufiri i dyt eshte excluded
print(coruse[0:2])
# ne perdorim strign format, qe mos te perdorim +, concate
# strign vendosi brenda {}
msg=f'{coruse} shkurtimi eshte {cr}'
msg2=coruse+cr
# msg2 eshte string concatination
print(msg)

# string fuctions
print(len(coruse))
# it creates a new strign
print(coruse.upper())
# nqs duam te gjejm indeksin e par nj strign
print(coruse.find("a"))
# replace funciton
name=input('enter name:\n')
print(coruse.replace(coruse,name))
# in operator
print("elta"in coruse)

# math operator
# power jo me ^ por me **
print(10**3)

# math functions
x=2.9
 
print(round(x))

# if statements
is_hot=True
is_cold=False
if is_hot:
    print("it's a hot day")
elif is_cold:
    print("it's a cold day")
else:
    print("it is a lovey day")
print("end of ifstatemnts")
# logical operator -> and or not