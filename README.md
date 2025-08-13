# Trampole file encoder
## Video Demo:  <URL HERE>
## Description:


#### What is the use of this program?
Did you ever felt the need to protect your data from others? if you are working with sensitive data and you like to somehow make your file unusable to other people you can encode your data using this program, it uses encoding techniques that make your data unreadable if you don't have the key to decode it.
So you encode your file with a password key. You remember the key and that's it, only you can access that data.
You can also use this program to split your file for more security and more options and possibilites.
Spliting a file would give you the the number of files you asked for, then you can keep all of it on one device, across multiple devices or even hand over every part to the members of a group so only if everyone agrees you could access the original file.


#### Encoding data:
When you run the project there are 4 options to choose,
    1: Encode a file
    2: List of encoded files in a directory
    3: Decode a file
    4: Split a file:
    5: Rejoin files:
    0: Exit
For encoding a file you must enter 1
after doing that you should provide a valid full path to your file in your computer and a key of your choice, then if the path is valid you will get a reply with a new path to your new file which is encoded form of your original file.

#### Decoding data:
Assuming you have a encoded file which is the ouput of this program, you can now decode it if you have the key,
if you don't have they key, you can't do anything.
After running the program you should enter 3 to decode your file, then the program will ask you a path and a key, if you enter both correctly you will get a new promp which shows you the new path to your decoded file.

#### Listing encoded files:
If you don't remember which files have been encoded, no problem, you can use the program itself to show you list of encoded files.
After running the program you should enter 2, then you should provide a valid path to a directory then wait a second for it to search in the directory for the encoded files. it doesn't matter if you chaned the encoded file's name or not, it will show you the list of file unless you didn't provided a valid path.

#### Split a file:
You can split your original file or encoded file to multiple pieces so you can store it in different devices for the maximum security. You can also give every piece to one of the members of a group so it could be only retrieved only if all the members decided to.

#### Rejoin files:
When you decided to retrieve the original file after you had split it, you can use this option and provide it with all the parts of the file, then it would make the original file for you

#### Importance of file names:
Feel free to change the encoded or decoded file's name since it has nothing to do with encoding, decoding or even identifying the encoded format. The purpose of the name is just to be appearant to user that which files are encoded and which files are not.

#### Hashing mechanism:
The hashing mechanism ensures you of the integrity of the orignal file after you had split it then rejoin it, if this hash is not equal to what was stored in the parts, you will give an Error that shows you there is a problem somewhere in the files.

#### Exiting:
Are you done with the program?
You should just enter 0 then the program will terminate itself.


#### Testing:
I wrote some tests for the program in pytest format, you should run test_project.py using pytest, if you made any change to the codes make sure tests show no error in the new version.

If you saw any bug in the program let me know in the issue section.
