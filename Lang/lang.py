#!/usr/bin/python3
""" Copyright© 2023-2026 OpenSoftware-World
OpenSoftware-World Calculator-Lite Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
OpenSoftware-World Calculator-Lite All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GitHub da yayınlanmaktadır Görüntülemek için: https://github.com/OpenSoftware-World/OpenSoftware-World-Calcutalor-Lite
A Copy of This Software is published on GitHub To view: https://github.com/OpenSoftware-World/OpenSoftware-World-Calculator-Lite"""

import sys
from Lib.Basic_Maths.Basic_Maths import *
from Lib.PyAppDevKit.pyappdevkit import *

about = "OpenSoftware-World-Calculator-Lite 2.5"

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if arg == "-tr":
            lang="tr"
        elif arg == "-en":
            lang="en"
        elif arg == "-about":
            print(about)
        elif arg == "-help":
            print("-tr -> Turkish")
            print("-en -> English")
            print("-about -> About")
            print("-help -> Help")
            print("-addition -> Addition")
            print("-extraction -> Extraction")
            print("-multiplication -> Multiplication")
            print("-division -> Division")
            print("-percentage -> Percentage")
            print("-mod -> Mod")
        elif arg == "-addition" or arg == "-add":
            n1=int(input("calc> Enter the 1st number: "))
            n2=int(input("calc> Enter the 2nd number: "))
            Addition(n1,n2,"",save_cfg=OFF,file_name="",save_err_msg="")
        elif arg == "-extraction" or arg == "-ext":
            n1=int(input("calc> Enter the 1st number: "))
            n2=int(input("calc> Enter the 2nd number: "))
            Extraction(n1,n2,"",save_cfg=OFF,file_name="",save_err_msg="")
        elif arg == "-multiplication" or arg == "-mul":
            n1=int(input("calc> Enter the 1st number: "))
            n2=int(input("calc> Enter the 2nd number: "))
            Multiplication(n1,n2,"",save_cfg=OFF,file_name="",save_err_msg="")
        elif arg == "-division" or arg == "-div":
            n1=int(input("calc> Enter the 1st number: "))
            n2=int(input("calc> Enter the 2nd number: "))
            Division(n1,n2,"","Number cannot be 0 when dividing!",save_cfg=OFF,file_name="",save_err_msg="")
        elif arg == "-percentage" or arg == "-per":
            n1=int(input("calc> Enter the 1st number: "))
            n2=int(input("calc> Enter the 2nd number: "))
            Percentage(n1,n2,"",save_cfg=OFF,file_name="",save_err_msg="")
        elif arg == "-mod":
            n1=int(input("calc> Enter the 1st number: "))
            n2=int(input("calc> Enter the 2nd number: "))
            Mod(n1,n2,"",save_cfg=OFF,file_name="",save_err_msg="")
        else:
            print("Invalid argument! Please type -help for more information!")
else:
    lang=input("Language: ")

if lang == "tr" or lang == "TR":
    error_dialog="Geçersiz işlem!"
    process_list = "calc> Girebileceğiniz işlemler: "
    process = "toplama\nçıkarma\nçarpma\nbölme\nyüzde hesaplama\nmod alma\nçıkış\nhakkında\n1,2,3,4,5,6,7,8"
    usr_input_n1 = "calc> 1. sayiyi giriniz: "
    usr_input_n2 = "calc> 2. sayiyi giriniz: "
    process_input = "calc> Gerçekleştirmek İstediğiniz İşlemi Giriniz: "
    div_err = "Bölme işleminde sayı 0 olamaz!"
elif lang == "en" or lang == "EN":
    error_dialog="Invalid Process!"
    process_list = "calc> Transactions you can enter: "
    process = "Addition\nSubraction\nMultiplication\nDivision\nPercentage\nMod\nexit\nabout\n1,2,3,4,5,6,7,8"
    usr_input_n1 = "calc> Enter the 1st number: "
    usr_input_n2 = "calc> Enter the 2nd number: "
    process_input = "calc> Enter the Transaction You Want to Perform: "
    div_err = "Number cannot be 0 when dividing!"
else:
    print("Invalid Language!")