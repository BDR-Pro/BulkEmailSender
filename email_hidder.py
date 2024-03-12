import csv
'''

this script is used to hide the email addresses in the emails.csv file
to make it dummy file for testing the BulkSender.py script


'''

# Open the input file
with open('emails.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    data = list(reader)

# Hide email addresses
for row in data:
    for i in range(len(row)):
        if '@' in row[i]:
            email_parts = row[i].split('@')
            row[i] = email_parts[0] + '@' + '*' * len(email_parts[1])

# Write the modified data to the output file
with open('template.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(data)