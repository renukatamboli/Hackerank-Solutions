import re
def fun(s):
    if(re.compile(r'^[a-z|A-Z0-9\-\_]+\@[a-zA-Z0-9]+[.][a-zA-Z]{0,3}$').match(s)):
                return True
    else:
                return False
        
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return filter(fun, emails)

if __name__ == '__main__':
    n = int(raw_input())
    emails = []
    for _ in range(n):
        emails.append(raw_input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails
