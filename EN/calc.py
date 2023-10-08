#!/usr/bin/python3
# Copyright© 2023 LinuxUsersLinuxMint
# Python Calcutator Lite Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
# Python Calcutator Lite All Rights Reserved under the GPL(General Public License).
# Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
# A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint

cmd=str("calc> ")

print("calc> Transactions you can enter: ")
print("Addition\nSubraction\n\Multiplication\nDivision\nPercentage\n 1,2,3,4")
n1=float(input('{0} Enter The 1st Number: '. format(cmd)))
n2=float(input('{0} Enter The 2st Number: '. format(cmd)))
process=input('{0} Enter the Transaction You Want to Perform: '. format(cmd))
if process=="1": 
    print("{0} + {1} = {2}". format(n1,n2,n1+n2))  
elif process=="2":
    print("{0} - {1} = {2}". format(n1,n2,n1-n2))
elif process=="3":
    print("{0} * {1} = {2}". format(n1,n2,n1*n2))
elif process=="4":
    print("{0} / {1} = {2}". format(n1,n2,n1/n2))
elif process=="5":
    print("{0} % {1} = {2}". format(n1,n2,n1%n2))
else:
    print("Invalid Process!")