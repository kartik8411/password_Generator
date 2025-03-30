import pyfiglet 
from colorama import Fore 
import string
import random

banner = pyfiglet.figlet_format('Passwd Generator', font='doom')
print(Fore.GREEN + banner)


if __name__== "__main__":
     s1 = string.ascii_lowercase
     #print(s1)
     s2 = string.ascii_uppercase
     #print(s2)
     s3 = string.digits
     #print(s3)
     s4 = string.punctuation
     #print(s4)

     plen = int(input("Enter password Length:\n"))
     s = []
     s.extend(list(s1))
     s.extend(list(s2))
     s.extend(list(s3))
     s.extend(list(s4))
     #print(s)
     random.shuffle(s)
     #print(s)
     print("Your password is: ")
     print("".join(s[0:plen]))

     #Reference
     #https://docs.python.org/3/library/string.html
   
