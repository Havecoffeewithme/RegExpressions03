# author : Percy Ratheko

import re


text = """
Mike is 20  years old and George is 29!
My grandma is even 104 years old!

"""

ages = re.findall(r"\d{1,3}", text)
print(ages)

string1 = re.findall(r"mike", text, re.IGNORECASE)
print(string1)


print("-----------------------------------------------")

text2 = """
lira@wits.ca.za
mimo@mail.com
sandra.bcit@gmail.com
letlotlo_theko@yahoo.com
ICTPass#6077
BOSee
"""

password = re.findall(r"[a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+", text2)
#matching_Emails = re.fullmatch(r"^[a-zA-Z0-9.!]+@[a-]")

print("ALL our emails : ")
for k in password:
    print(k)
print()

print("lira's email : ")
password2 = re.findall(r"[a-zA-Z0-9+.]+@[\w]+\.[\w]+\.[\w]+", text2)

for v in password2:
    print(v)

print()
print("The gmail account : ")
password3 = re.findall(r"[a-zA-Z0-9+.%]*@gmail\.[\w]+", text2)
for k in password3:
    print(k)

print()
print("Anything but an Email : ")
pattern = r'^(?!.*[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}).*$'
password4 = re.findall(pattern, text2, re.MULTILINE)

for k in password4:
    if k.strip():
        print(k)


print("-------------------------------------------------------------------")
print()
series = """
Season 5 of Breaking Bad it is the best season in TV history        
Mad-Men is the second best series of all time 
"""

show = re.sub(r"\d{1,3}", "20", series)
#show2 = re.sub(r"[^mad$]", "xxx", series)


print(show)
#print(show2)




