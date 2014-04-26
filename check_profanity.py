import urllib

def read_text():
    quotes = open("/Users/Zoe/Dropbox/CS/movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()

read_text()
    
'''def check_profanity():
    profanity_list = ["shit","damn"]
    file = open("/Users/Zoe/Dropbox/CS/movie_quotes.txt","r")
    lines = file.read()
    for profanity_words in profanity_list:
        check_profanity = lines.find(profanity_words)
        if check_profanity > 0:
            print("OH!Take care!")
    print("...Finish...")
   
check_profanity()'''
