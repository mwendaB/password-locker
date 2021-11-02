# Password-Locker
This app has been created using python3.9.7
#### Author
Brian Mwenda 
#### created on 24th october 2021

## Description
This is a PasswordLocker application that serves to create users' accounts and even be able to display them. All this is possible by running short commands on the terminal which the user is met with on running python3 passwordlock.py on the terminal.

## Behavior-driven development
- These are the behaviours that the application implements for use by a user.
## As a user I would like:
- To create an account with my details - log in and password
- Store my existing login credentials
- Generate a password for a new credential/account

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|Open the application on the terminal | Run the command ```$ ./passwordlocker.py```|Hello Welcome to your Password locker... <br>* ca ---  Create New Account * li ---  Have An Account |
|Select  c| input username and password| Hello ```username```, Your account has been created succesfully! Your password is: ```password```|
|Select li  | Enter your password and username you signed up with| Abbreviations menu to help you navigate through the application|
|Store a new credential in the application| Enter ```CC```|Enter Account, username, password<br>choose ```ty``` to enter your password or ```gen``` for the application to generate a password for you |
|Display all stored credentials | Enter ```disp```|A list of all credentials that has been stored or ```You don't have any credentials``` |
|Find a stored credential based on account name|Enter ```find```| Enter the Account Name you want to find for and returns the account details|
|Delete credential that you don't want anymore|Enter ```del```|Enter the account name of the Credentials you want to delete and returns true if the account has been deleted and false if the account doesn't exixt|
|Exit the application| Enter ```ex```| The application exits| 
## Setup/Installation Requirements
Open your terminal
* Run
```
git clone https://github.com/mwendaB/password-locker
```

* No web dependencies needed.
* After cloning the repo you can either deside to run it on your visual studio codes terminal or the main Terminal
* Run in terminal using the command:
```
 python3 passwordlock.py
 ```

## Known Bugs
I havent encountered any bugs.
INcase you come across any feel free to correct me via Email.

## Technologies Used
Python3.9.7<br>
Terminal<br>
Pip

## Support and contact details
Incase of any contribution, comment or question please email me:<br>
**brianmwenda255@gmail.com**

### License
[MIT](License)
Copyright (c) 2021 **Brian Mwenda**