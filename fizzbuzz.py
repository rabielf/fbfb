# if ~ else 1회로 fizzbuzz 

for i in range(1, 45+1) :
    if (i%3==0) or (i%5==0) :
        print('Fizz' * (i % 5 == 0) + 'Buzz' * (i % 3 == 0))
    else:
        print(i)
