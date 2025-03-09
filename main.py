import os
from time import strftime

import speech_recognition as sr
import pyttsx3
import webbrowser
import ollama
import datetime
import random


chatStr = ""


def chat(query):
    global chatStr
    # print(chatStr)

    chatStr += f"Ashritha: {query}\n Honey: "

    response = ollama.chat(
        model='mistral',
        messages=[{"role": "user", "content": chatStr}]
    )
    say(response['message']['content'])
    reply = response['message']['content']

    # Simulating the 'say' function (you can replace this with text-to-speech if needed)
    print(reply)

    chatStr += f"{reply}\n"
    return reply




def ai(prompt):
    text = f"Ollama response for Prompt: {prompt} \n *************************\n\n"

    try:
        response = ollama.chat(model='mistral', messages=[{'role': 'user', 'content': prompt}])
        text += response['message']['content']
    except Exception as e:
        text += f"\nError: {str(e)}"

    if not os.path.exists("AI"):
        os.mkdir("AI")


    filename = f"AI/{''.join(prompt.split('intelligence')[1:]).strip()}.txt"

    with open(filename, "w") as f:
        f.write(text)

    print(f"Response saved to {filename}")

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            # query = r.recognize_bing(audio, language= "en-in")
            print(f"User said: {query}")

            return(query)
        except Exception as e:
            return "Some Error Occurred. Sorry from Honey"


if __name__ == '__main__':
    print('PyCharm')
    say("Hello, I am Honey AI")
    while True:
        print("Listening....")
        query = takeCommand()



        # APPSSSSSSSSSSSSSSSSSSSSSSSS
        # todo: add more apps or features or anything

        apps = [["camera", "start microsoft.windows.camera:"], ["calculator", "start calc"],
                ["photos", "explorer.exe shell:AppsFolder\Microsoft.Windows.Photos_8wekyb3d8bbwe!App"],
                ["command prompt", "start cmd"], ["file explorer", "start explorer"], ["outlook", "start outlookmail:"],
                ["paint", "start mspaint"], ["word", "start winword"], ["powerpoint", "start powerpnt"],
                ["excel", "start excel"]]
        for app in apps:
            if f"Open {app[0]}".lower() in query.lower():
                say(f"Opening {app[0]} Ma'am....")
                os.system(app[1])




        # SITESSSSSSSSSSSSSSSSSSSS
        # todo: add more sites

        sites=[["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"],["Linkedin", "https://wwww.linkedin.com"], ["Twitter", "https://www.twitter.com"], ["gmail", "https://www.gmail.com"], ["instagram", "https://www.instagram.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} Ma'am....")
                webbrowser.open(site[1])


        if "open music" in query:
            musicPath = "C:\\Users\\varla\\Downloads\\flute-traditional-v1-251387.mp3"
            os.startfile(musicPath)     #we can also use os.system(f"open {musicPath}"

        elif "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Ma'am the time is {strfTime}")


        # if "open camera".lower() in query.lower():
        #     os.system(f"start microsoft.windows.camera:")

        # USINGGGGGG AI
        elif "using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Honey quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            say("Resetting chat Ma'am....")
            chatStr = ""
        else:
            print("Chatting....")
            chat(query)





            # say(query)




