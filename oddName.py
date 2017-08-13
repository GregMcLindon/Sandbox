"""Greg McLindon"""
def main():
    """Program to print every second letter of a string"""
name_valid = False
string_name = ""
while not name_valid:
    string_name = input("What is your name?")
    if len(string_name) == 0:
        print("Enter a valid name")
    else:
        name_valid = True
print(string_name[::2])