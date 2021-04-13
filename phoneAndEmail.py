#! python3

import re, pyperclip

#Create a regex for phone numbers
phoneRegex = re.compile(r'''
(
((\d\d\d)|(\(\d\d\d\)))?  #area code (optional)
(\s|-)                    #first seperator
\d\d\d                    #first 3 digits
-                         #second seperator
\d\d\d\d                  #last 4 digits
(((ext(\.)?\s)|x)         #extension word-part
(\d{2,5}))?               #extension number-part
)
''', re.VERBOSE)

#Create a regex for email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+            #name part
@                          #@ symbol
[a-zA-Z0-9_.+]+            #domain name
''', re.VERBOSE)

#Get the text off the clipboard
text = pyperclip.paste()

#Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
    
#Copy the extracted email/phone to the clipboard, concatonate newline between each string
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
print(results)


