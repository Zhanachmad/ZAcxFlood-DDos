import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("pkg install python")
    os.system("pkg install python2")
    os.system("pkg install python3 python3 install-pip")
    os.system("pip install requests")
    os.system("pkg install flood")
   

elif c == "1":
    os.system("pkg install python")
    os.system("pkg install python2")
    os.system("pkg install python3 python3 install-pip")
    os.system("pip install requests")
    os.system("pip install flood")
   
print("Done.")
