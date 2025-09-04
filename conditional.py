'''print('welcome to the shop')
q=input('do you want to buy something? (yes/no): ')

if q=='yes':
    print('purchase 2kg of apples')
if q=='no':
    print('you do not want to buy anything' )
   
salary = 48000
da=0
if salary > 50000:
    da = .15          # 15% dearness allowance
total = salary + salary * da
print(f"total salary is {total}")'''


x=int(input('enter a number'))
y=int(input('enter a fees'))

if x>y:
    a= x - y
else:
    a= y - x