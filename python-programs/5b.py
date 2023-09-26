import re

phone_regex = re.compile(r'\+\d{12}')
email_regex = re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}')
# Open the file for reading
with open('example.txt', 'r') as f:
# Loop through each line in the file
    for line in f:
# Search for phone numbers in the line
        matches = phone_regex.findall(line)
# Print any matches found

for match in matches:
    print(match)
matches = email_regex.findall(line)
# Print any matches found
for match in matches:
    print(match)
