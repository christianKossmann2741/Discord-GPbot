import openYBSB
import emoji

#The code speaks for it self kek

def handle_response(message, user_message) -> str:
    fw = open('history.txt', 'a+')
    fw.write("\n"+str(user_message)+": "+str(message))
    fw.close()
    return openYBSB.ai_it()