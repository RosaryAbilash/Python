import win32clipboard
import time

old_clipboard = ""

while True:
    # Opening clipboard
    win32clipboard.OpenClipboard()
    # Getting Copied data
    data = win32clipboard.GetClipboardData()
    # closing clipboard
    win32clipboard.CloseClipboard()
    if old_clipboard != data:
        # Writing copied data to clipboard.txt file as apending mode
        with(open("clipboard.txt", "a+")) as file:
            file.write(data + "\n")
        old_clipboard = data
    
    # Sleep time 0.6 second
    time.sleep(0.6)