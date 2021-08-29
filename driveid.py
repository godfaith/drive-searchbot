import os
import re
print("\n\n"\
      "        Bot can search files recursively, but you have to add the list of drives you want to search.\n"\
      "        Use the following format: (You can use 'root' in the ID in case you wan to use main drive.)\n"\
      "        teamdrive NAME      -->   anything that u likes\n"\
      "        teamdrive ID        -->   id of teamdrives in which u likes to search ('root' for main drive)\n"\
      "        teamdrive INDEX URL -->   enter index url for this drive.\n" \
      "                                     goto the respective drive and copy the url from address bar\n")
msg = ''
if os.path.exists('drive_folder'):
    with open('drive_folder', 'r+') as f:
        lines = f.read()
    if not re.match(r'^\s*$', lines):
        print(lines)
        print("\n\n"\
              "      DO YOU WISH TO KEEP THE ABOVE DETAILS THAT YOU PREVIOUSLY ADDED???? ENTER (y/n)\n"\
              "      IF NOTHING SHOWS ENTER n")
        while (1):
            choice = input()
            if choice == 'y' or choice == 'Y':
                msg = f'{lines}'
                break
            elif choice == 'n' or choice == 'N':
                break
            else:
                print("\n\n      DO YOU WISH TO KEEP THE ABOVE DETAILS ???? y/n <=== this is option ..... OPEN YOUR EYES & READ...")
num = int(input("    How Many Drive/Folder You Likes To Add : "))
count = 1
while count <= num :
    print(f"\n        > DRIVE - {count}\n")
    name  = input("    GOD's DRIVE      ")
    id    = input("    root                   ")
    index = input(" https://index.godtruth.workers.dev/0:    ")
    if not name or not id:
        print("\n\n        ERROR : Dont leave the name/id without filling.")
        exit(1) 
    name=name.replace(" ", "_")
    if index:
        if index[-1] == "/":
            index = index[:-1]
    else:
        index = ''
    count+=1
    msg += f"{name} {id} {index}\n"
with open('drive_folder', 'w') as file:
    file.truncate(0)
    file.write(msg)
print("\n\n    Done!")
