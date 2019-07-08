num=raw_input('num= ')

if int(num) % 3==0 and int(num) % 7==0:
    print("3 and 7")
elif int(num) % 3==0:
    print("3")
elif int(num) % 7==0:
    print("7")
else:
    print 'none'
