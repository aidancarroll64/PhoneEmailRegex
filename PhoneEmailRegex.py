#! python39

import re, pyperclip

# Create Regex object for phone numbers
phoneRegex = re.compile(r'''
(
((\d\d\d)| (\(\d\d\d\)))?       # area code (optional)
(\s|-)      # first seperator
\d\d\d        # first 3 digits
-        # seperator
\d\d\d\d        # last 4 digits
(((ext(\.)?\s) | x)
(\d{2,5}))? # extension (optional)
)
''', re.VERBOSE)

# Create REgex object for email addresses

emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com

[a-zA-z0-9_.+]+ # name part
@               # @ symbol
[a-zA-z0-9_.+]+ # domain name part
''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract email/phone numbers
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)

# Copy the extracted text to the clipboard

results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
