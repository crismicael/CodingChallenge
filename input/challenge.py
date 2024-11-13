import csv
import json

# Initialize empty list to store dictionaries
contacts = [] # This is the list of dictionaries
#Opens the file so we can read it, it can take up to 3 parameters the filename ("as in the above line"), the mode (r is read, w is write, a is append), and the encoding (utf-8 is the default)
with open("input2.tsv") as file:
    #.reader() is used to read the file into a list of lists, however it does not allow us to read the file into a dictionary
    #Creates an object that reads the TSV file
    tsv_file = csv.DictReader(file, delimiter="\t") # DictReader allows us to read the file into a dictionary. It reads the first row as headers (keys) and the rest of the rows as values
    
    # Loop through each row and create a dictionary
    for row in tsv_file: # This iterates through each row in the file
        # Create an empty dictionary
        contact = {}
        
        # Loop through each key and value in the row
        for key, value in row.items():
            # Only add the key-value pair if value is not empty
            if value:
                # Convert the key to lowercase and add to dictionary
                lowercase_key = key.lower() # Convert the key to lowercase
                contact[lowercase_key] = value # Add the key-value pair to the address dictionary
        
        # Add the contact to our list
        contacts.append(contact)

# Define a function that gets the zip code from a contact dictionary
def get_zip_code(contact):
    # 'contact' will be each dictionary from our list
    # This function simply returns the zip code for that contact
    return contact['zip']

# Use this function to sort the contacts
contacts.sort(key=get_zip_code)

# Print JSON output
print(json.dumps(contacts, indent=2))
