import os
import time
import sys
red='\033[93m'
def main():
    os.system("clear")
    print("""Your termux to basic package Install 
                    
                    [01] Yes
                    [02] No""")
    user=str(input("Enter selec:"))
    if user == "01" or user == "1":
         pass
    elif user == "02" or user == "2":
          #sys.exit()
    else:
          print("your selec to rong")
          main()
    os.system("clear")
    print(red+"")
          
          
    
    