

def hashFunc(n, size):

   return n%size
    

L=[]
size=int(input('Enter the original size of your list:'))
for i in range(size):
    L.append(None)

mySize=int(input('Enter the number of values you want to enter:'))

for i in range(mySize):
    num=int(input('Enter value {}:'.format(i+1)))
    index=hashFunc(num, mySize)
    L.insert( index, num)

print('All the values are entered successfully________')

print('Displaying your elements according to their index numbers:')

for i in range(size):
    print('myList[{}] = {}'.format(i, L[i]))

#print(L)
