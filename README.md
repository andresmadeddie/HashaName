# Hash a Name

Hash a Name is a web application that explores an alternative way to generate passwords from an easy-to-remember word.
**motto: "Change your password, NOT your keyword"**


## Motivation
The world is full of people looking for distinct solutions. Some people use the same password for everything because
they do not like the idea of remembering a different password for each site. Moreover, change them every several days.

The password manager market gives several solutions to this problem.
Nevertheless, the power of holding the passwords goes to the sites for above the user.
Likewise, the friendly interface could be complex for some kinds of users.
This alternative looks for an easy way to give back the holding power to the users with simplicity.

## Tech/Build With:
* HTML
* CSS
* JavaScript
* Python
* Flask
* SQL

## Functionality:
The central idea of this alternative is to **keep it simple** using **one keyword for everything.**  There are three elements in this system:
1. The keyword
2. The logarithm
3. The password algorithm key (PAK)

**The keyword**
The keyword is an easy-to-remember word like the name of the user.

**The algorithm**
It is a process with several inputs that outputs the password.

**PAK (Password algorithm key)**
It is a list of random data use as inputs for the logarithm.

Basically, the logarithm generates a strong password from an easy-to-remember word and the random values from the "PAK".
The password and the keyword are never stored, but the "PAK".
If the user wants to query his password, he needs the saved "PAK" plus his keyword (stored only in his head).
If the user wants to change the password or get a new one for another site, he only needs to change the PAK.

In this way, even if someone has access to the logarithm and PAK, that someone still does not know what PAK is the one needed,
and even if he knows which PAK to use, the keyword still safe in the mind of the user.

**INPUT / OUTPUT (What the WebApp do)**:
**Input**: a word (only upper or lower case alphabet characters)
**Output**: a password with these features:
* At least 8 characters long
* 1 uppercase
* 1 lowercase
* 1 number
* 1 symbol

## Functions:
* Generate Password
* Query Password (user will always get the same password unless push the change button).
* Change PAK (Password's Algotithm Key) to generate a new password with the same word.
* Register Users can store their PAK
                                * Data(PASSWORD'S ALGORITHM KEYS).
* Register Users can restore or delete previously stored PAKs.
* Close account(all data related is deleted).

## Posibles future Implementations to develop:
Register and Guest users could download a ".exe" file with the selected PAK, so he/she can query his password through his device offline(security)

## DESCRIPTION OF BUTTONS AND INPUTS FIELDS
### Intro layout:
#### Head
* Help: Leads to the current layout.
* Register: Leads to the register layout.
* Log In: Leads to the login layout.

#### Main
* Log In: Leads to the login layout
* Guest Mode: Leads to the Guest layout.
* Register: Leads to the Register layout.

### Guest Mode:
#### Head
* HashaName: When pressed leads you to the intro layout.
* Help: Leads to the current layout.

#### Main
* Insert Keyword: Insert an easy-to-remember word like your name. Only accepts alphabet characters, and is case insensitive(Keep it easy).
* Get Password: Get a password with the current "password's algorithm key". This button will be activated to push after input some data in the "Insert Keyword" field.
* Change PAK: Push to change the password. This button will change the values of the current PAK to provide a new password.
* Password: This field shows the generated password from where you can Copy&Paste.

### User Mode:
#### Head
* HashaName: When pressed leads to the Main layout.
* Main: Main layout, where the action occurs.
* Account: Option to close your account. This will delete all your store data without the possibility to recover.
* Help: Leads to the current layout.
* Log Out: Log out session.

#### Main
* Insert Keyword: Insert an easy-to-remember word like your name. Only accepts alphabet characters, and is case insensitive(Keep it easy)
* Get Password: Get a password with the current "password's algorithm key". This button will be activated to push after input some data in "Insert Keyword"
* Change PAK: Push to change the password. This button will change the values of the current PAK to provide a new password.
* Password: This field shows the generated password from where you can Copy&Paste.
* Save Current PAK: Store the current PAK. This button will be activated after input some data in the "Key's name" field.
* Key's name: Give a name to the PAK. (ex: Facebook, Gmail, Pepito, etc)

#### Stored keys Table
* Delete All: Will delete all stored data.
* Delete: Delete only the PAK in the row.
* Recover: Recover the PAK in the row.

## THINGS TO KNOW:

### What is PAK or PASSWORD'S ALGORITHM KEYS?
It is a list of randomly selected data use in the algorithm to generate the password

### What means Case Insensitive?
It just means that it doesn't matter if you write with a mix of upper and lower cases (ex:RobeRt, roBERt, robert, ROBERT is the same). So, KEEP IT SIMPLE, no need to remember if you input like Robert or robert, for the algorithm is the same.

### How do I CREATE a password?
1. Place your keyword (ex:robert) in the Insert Keyword field
2. Push the "Get password" button
3. Your password will appear next "Password:"

### How do I SEE my password?
1. Place your keyword (ex:robert) in the Insert Keyword field
2. Push the "Get password" button
3. Yes, it is exactly as you created the password, just make sure you have not pushed the "Change PAK" button. If you do so without saving, your password will be lost forever and ever. (Only register users can store data, Guest do not have this option... so, register ;P)

### How do I SAVE my password?
You don't save your password. Instead, you save the PAK(password's algorithm key) that generates your password with the keyword(maybe your name) that only you know and will always remember(KEEP IT SIMPLE).

1. Write a name in the "PAK's name" field.(ex: Facebook, Gmail, Pepito, etc)
2. Press the "Save" button. (Remember the button will not be activated until you input a value in the "PAK's name" field)
3. Look at the Stored PAKs' table. (There appears a new row with your designed name and an option to recover or delete)

### How do I CHANGE my current password?
1. Just push the "Change PAK" button. (remember that the previous PAK will be lost forever unless you save it")
2. Use the same keyword as usually(ex:robert)
3. voila!!! new password

### How do I RECOVER a password from a stored PAK?
1. Look in the table the stored PAK you want to recover. you have the PAK`s names and Date/Time for reference.
2. Push the "Recover" button next to your choice.
3. Input your keyword(ex:robert). Remember: The field is case insensitive.
4. voila!!... the generated password is your password.

<!--https://medium.com/@er.bharat1992/writing-readme-md-markdown-file-file-bd711d1afbfa#:~:text=How%20to%20create%20readme.md%20file%2C%20have%20a%20look,click%20the%20%E2%80%98open%20preview%20to%20the%20side%E2%80%99%20icon.-->
