#!/usr/bin/python3
""" Copyright© 2023-2025 LinuxUsersLinuxMint
LinuxUsersLinuxMint Calcutator-Lite Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
LinuxUsersLinuxMint Calcutator-Lite All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-Calcutator-Lite
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-Calcutator-Lite"""

from Basic_Maths import *

cmd=str("calc> ")
error_dialog = "Invalid Process!"

print("calc> Transactions you can enter: ")
print("Addition\nSubraction\nMultiplication\nDivision\nPercentage\n1,2,3,4")
n1=float(input('{0} Enter The 1st Number: '. format(cmd)))
n2=float(input('{0} Enter The 2st Number: '. format(cmd)))
process=input('{0} Enter the Transaction You Want to Perform: '. format(cmd))
if process=="1": 
    addition(n1,n2)  
elif process=="2":
    Extraction(n1,n2)
elif process=="3":
    Multiplication(n1,n2)
elif process=="4":
    Division(n1,n2,"","Number cannot be 0 when dividing!")
elif process=="5":
    Percentage(n1,n2)
else:
    error_msg()