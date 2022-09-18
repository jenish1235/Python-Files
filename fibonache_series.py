first_Integer = 1
second_integer = 0

for i in range(25):
    first_sum = first_Integer + second_integer
    second_integer = first_Integer
    first_Integer = first_sum
    if(i%2 == 0):
        print(first_sum)
    else:
        print(-first_sum)
