import random
while True:
    print('Ban so 1 tung duoc so: ')
    a = int(input('Nhap so tu 1 den 6: '))
    b = random.randint(1,6)
    print('Ban so 2 tung duoc so: ')
    print(b)
    if a > b:
        print('Ban 1 thang')
    elif a == b:
        print('Hoa')
    else:
        print('Ban 2 thang')
    print('Ban co muon tiep tuc: ')
    print('1: yes')
    print('2: no')
    f = int(input("lua chon: "))
    if f != 1:
        break
print('ket thuc chuong trinh')
