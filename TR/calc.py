#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
LinuxUsersLinuxMint Calcutator-Lite Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
LinuxUsersLinuxMint Calcutator-Lite All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-Calcutator-Lite
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-Calcutator-Lite"""

from Basic_Maths import *

cmd=str("calc> ")
error_dialog = "Geçersiz İşlem!"

print("calc> Girebileceğiniz işlemler: ")
print("toplama\nçıkarma\nçarpma\nbölme\nyüzde alma\n1,2,3,4,5")
s1=float(input('{0} 1. sayiyi giriniz: '. format(cmd)))
s2=float(input('{0} 2. sayiyi giriniz: '. format(cmd)))
islem=input('{0} Gerçekleştirmek İstediğiniz İşlemi Giriniz: '. format(cmd))
if islem=="1": 
    addition(s1,s2)
elif islem=="2":
    Extraction(s1,s2)
elif islem=="3":
    Multiplication(s1,s2)
elif islem=="4":
    Division(s1,s2,"","Bölme işleminde sayı 0 olamaz!")
elif islem=="5":
    Percentage(s1,s2)
else:
    error_msg()