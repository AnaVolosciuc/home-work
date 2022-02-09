num = 0
while num < 100:
    num = num + 1
    if num > 10 and num < 20:
        print (str(num) + ' protentov')
    elif (num % 10) == 1 and num != 11:
        print (str(num) + ' protent')
    elif (num % 10) < 5 and (num % 10) > 0:
        print (str(num) + ' protenta')
    else:
        print (str(num) + ' protentov')

