import time, requests, os

os.system('cls')
print("\n    ██▀███   ▄▄▄        ▄████ ▓█████     ▄▄▄       ██▓ ▒█████  \n"
"   ▓██ ▒ ██▒▒████▄     ██▒ ▀█▒▓█   ▀    ▒████▄    ▓██▒▒██▒  ██▒\n"
"   ▓██ ░▄█ ▒▒██  ▀█▄  ▒██░▄▄▄░▒███      ▒██  ▀█▄  ▒██▒▒██░  ██▒\n"
"   ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█  ██▓▒▓█  ▄    ░██▄▄▄▄██ ░██░▒██   ██░\n"
"   ░██▓ ▒██▒ ▓█   ▓██▒░▒▓███▀▒░▒████▒    ▓█   ▓██▒░██░░ ████▓▒░\n"
"   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ░▒   ▒ ░░ ▒░ ░    ▒▒   ▓▒█░░▓  ░ ▒░▒░▒░ \n"
"     ░▒ ░ ▒░  ▒   ▒▒ ░  ░   ░  ░ ░  ░     ▒   ▒▒ ░ ▒ ░  ░ ▒ ▒░ \n"
"     ░░   ░   ░   ▒   ░ ░   ░    ░        ░   ▒    ▒ ░░ ░ ░ ▒  \n"
"      ░           ░  ░      ░    ░  ░         ░  ░ ░      ░ ░  \n")
print("   https://github.com/adambielat / https://github.com/adambielat/rage-aio\n\n"
      "   1 -  Webhook Spammer ")

def menuFunction():
    menuChoice = int(input("\n   Type number of tool you'd like to use: "))
    if (menuChoice == 1):
        os.system('cls')
        inputFunction()



def inputFunction():
    webhookURL = input("\n\n   Please paste the webhook URL: ")
    result = (requests.get(webhookURL))
    if (result.status_code == 200):
        message = input("\n   Enter the spam message: ")
    else:
        os.system('cls')
        print("Please enter a valid webhook URL.")
        webhookSpammer()
    sleepTime = int(input("\n   Enter a sleep time in seconds: "))
    messageCount = int(input("\n   Enter amount of messages to send: "))
    while (messageCount > 0):
        sent = requests.post(webhookURL, json = {'content': message})
        if (sent.status_code == 204):
            print("Sent message:", message)
            print("Messages left:", messageCount,"\n")
            messageCount=messageCount-1
            time.sleep(sleepTime)
        else:
            print("Message failed to send, webhook might have gotten deleted.")
            messageCount=messageCount-1
            time.sleep(sleepTime)
    menuFunction()
            


menuFunction()