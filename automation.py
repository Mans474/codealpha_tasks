import re
import os
import shutil

# Input and output file names
input_file = "data.txt"
output_file = "emails.txt"

# Checking if input file exists
if os.path.exists(input_file):

    # Reading file content
    with open(input_file, "r") as file:
        content = file.read()

    # Extracting email addresses using regex
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

    # Saving emails to another file
    with open(output_file, "w") as file:
        for email in emails:
            file.write(email + "\n")

    # Creating backup of output file
    shutil.copy(output_file, "emails_backup.txt")

    print("Email addresses extracted successfully!")
    print("Saved in:", output_file)

else:
    print("Input file not found!")
