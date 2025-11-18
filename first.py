'''a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)  #20 power of 30/exponenation

print(a%b)    #remainder'''
'''
total=1
for num in range(10,20):
    total=total+num
    print(total)
'''
 



'''x=10
print(x)

x=[2,4,5,6,1,2,5.6]


p=str(input('enter your name'))
marks=int(input('enter your marks'))


print('name is ',a ,'marks is ',20)


print("How old are you?", end=': ')
age = input()
print("How tall are you?", end=': ')
height = input()
print("How much do you weigh?", end=' :')
weight = input()
print(f"So, you're {age} old, {height} tall and {weight} heavy.")'''



'''a = "python easy"
a = "python easy"
print(a[1])

print(a[-2])'''
'''
a = "python easy"
print(a[1])
print(a[2])'''

'''
from rembg import remove
from PIL import image


input_path='pawan kalyan.jpg'
output_path='pawan kalyanjsp.jpg'

inp=image.open(input_path)
output=remove(inp)
output.save(output_path)
image.open(output_path)'''

'''nums=[1,2,3,4]
for i in nums:
    nums.remove(i)
    print(nums)'''
import numpy as np

x=np.array([[2,4][5,11],[3,4]])
print(x.mean())