#!/usr/bin/python3
# Copyright© 2023 LinuxUsersLinuxMint
# Python Calcutator Lite Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
# Python Calcutator Lite All Rights Reserved under the GPL(General Public License).
# Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
# A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint

cmd=str("calc> ")

print("calc> Girebileceğiniz işlemler: ")
print("top\ncık\n\carp\nbol\nyuzde\n 1,2,3,4")
s1=float(input('{0} 1. sayiyi giriniz: '. format(cmd)))
s2=float(input('{0} 2. sayiyi giriniz: '. format(cmd)))
islem=input('{0} Gerçekleştirmek İstediğiniz İşlemi Giriniz: '. format(cmd))
if islem=="1": 
    print("{0} + {1} = {2}". format(s1,s2,s1+s2))  
elif islem=="2":
    print("{0} - {1} = {2}". format(s1,s2,s1-s2))
elif islem=="3":
    print("{0} * {1} = {2}". format(s1,s2,s1*s2))
elif islem=="4":
    print("{0} / {1} = {2}". format(s1,s2,s1/s2))
elif islem=="5":
    print("{0} % {1} = {2}". format(s1,s2,s1%s2))
else:
    print("Geçersiz İşlem")