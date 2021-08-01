#one vending machine have unlimited candies
x=int(input("enter hom many candies you want"))
i=1
while i<=x:
 print(i,"candy")
 i=i+1
print('THANK YOU')

#if incase vending machine having 5 candies only

available_candies=5
x=int(input("enter how many candies you want"))
i=1
while i<=x:
 if i>available_candies:
  print('oops...!')
  print("out of stock")
  break
 print(i,"candy")
 i=i+1
print("THANK YOU")
