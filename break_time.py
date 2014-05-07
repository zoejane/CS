import time
import webbrowser

total_break = 1
break_count = 0

print("This program started on "+time.ctime())

while( break_count < total_break):
    time.sleep(10)
    webbrowser.open("http://www.pandora.com")
    break_count = break_count + 1
