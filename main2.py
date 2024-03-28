import time
def fact(n):
    fact = n
    for i in range(1, n): 
        fact = i*fact 
    return fact

n = 1
with open('loop.txt', 'a') as f:
    f.write('Num = int(input()) \nif Num==1: \n    print(Non prime)')

while True:
    n +=1
    with open('loop.txt', 'a') as f:

        if fact(n-1)%n == (n-1): #teorema de wilson
            f.write(f'\nelif Num=={n}')
            f.write('\n    print("Prime")')
            print(n, 'Prime')
        else:
            string = f'elif Num=={n}: \n\t print("Non prime")'
            f.write(f'\nelif Num=={n}:')
            f.write('\n    print("Non prime")')
            print(n, 'Non prime')
        time.sleep(0.05)


