# 3의 배수: fizz
# 5의 배수: buzz
# 15의 배수: fizzbuzz
# 나머지: 숫자(1-45) done

for i in range(1,45+1):
    if i%15==0:
        print('fizzbuzz')
    #elif i%3==0:
    #    print('fizz')
    #elif i%5==0:
    #    print('buzz')
    else:
        print(i)
