# PasswordOrganizator-App
Password Organizer is a simple application written in Python that allows for the secure storage and generation of passwords in a CSV file, with customizable password length and file name options.


![project2-2](https://github.com/user-attachments/assets/9976c54d-0cba-450b-a457-bf20f2febec4)
# Usage

Adding a Password:

In the Website field, enter the name of the site.
Enter the password in the Password field or click Generate Password to automatically receive a random password.
Click Save Data to store the entry in a CSV file.

Resetting Entries:

If you want to clear the currently entered data, click Reset.

Changing Settings:

Click Settings to open the customization window.
Change the length of the generated password or the name of the CSV file in which passwords are stored.
Click Confirm Settings to save your changes.
Code Structure

Variables: 
Define initial values, including the CSV file name and password length.

Functions:

reset(): 
Clears the current entries from the fields.

save(): 
Saves the website name and password to the CSV file.

generate_password(): 
Generates a random password based on the entered length.

application(): 
Displays the main application window.

settings(): 
Displays the settings window.

select_settings():
Saves the customized settings.

# Contribution

Contributions are welcome! Feel free to create a pull request or open an issue for suggestions and improvements.

# License

This project is licensed under the MIT License.
