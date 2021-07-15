# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re
n = int(input())
for i in range(0,n):
    mail = input().split()
    if(re.match(r'^\<[a-zA-Z0-9][a-zA-Z0-9-.,_]+\@[a-zA-Z]+\.[a-zA-Z]{1,3}\>',mail[1])):
        mail[1] = mail[1].replace("<","").replace(">","")
        print(email.utils.formataddr(tuple(mail)))
    
    
