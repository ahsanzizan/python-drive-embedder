# Google drive image embedder

import webbrowser as wb
import pyperclip as clip
import datetime as dt

if __name__ == "__main__":
    print("The content must have a valid ID and must have public access")
    link = input("Google Drive Content URL: ")
    split_link = link.split("/")

    # The URL usually looks like this:
    # ['https:', '', 'drive.google.com', 'file', 'd', '[id]', 'view?usp=drive_link']
    content_id = split_link[5]

    # Tweak the link to https://lh3.google.com/u/0/d/[id]
    tweaked_link = f'https://lh3.google.com/u/0/d/{content_id}'

    # Copy to clipboard
    clip.copy(tweaked_link)
    print(f'URL: {tweaked_link}')

    with open("history.txt", "a+") as history:
        now = dt.now()
        stringified_now = now.strftime("%d/%m/%y %H:%M:%S")
        history.write(stringified_now, ":", tweaked_link)

    wb.open(tweaked_link)

