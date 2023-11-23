# Google drive image embedder

import webbrowser as wb

if __name__ == "__main__":
    print("The content must have a valid ID and must have public access")
    link = input("Google Drive Content URL: ")
    split_link = link.split("/")

    # The URL usually looks like this:
    # ['https:', '', 'drive.google.com', 'file', 'd', '[id]', 'view?usp=drive_link']
    content_id = split_link[5]

    # Tweak the link to https://drive.google.com/uc?export=view&id=[id]
    tweaked_link = f'https://drive.google.com/uc?export=view&id={content_id}'
    print(tweaked_link)

    wb.open(tweaked_link)

