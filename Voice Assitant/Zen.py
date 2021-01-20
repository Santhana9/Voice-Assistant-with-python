import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install speech_recognition
# pip install pipwin / pipwin install pyaudio
import wikipedia  # pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui  # pip install pyautogui / pip install Pillow
import psutil  # pip install psutil
import pyjokes

engine = pyttsx3.init()


def speak(said):
    engine.say(said)
    engine.runAndWait()


def time():
    timing = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(timing)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)


def greeting():
    speak("Hello ! This is Zen")
    # time()
    # date()
    hour = int(datetime.datetime.now().hour)
    if not hour < 6 and hour < 12:
        speak("Good Morning !")
    elif not hour < 12 and hour < 18:
        speak("Good Afternoon")
    elif not 18 > hour and hour < 24:
        speak("Good Evening!")
    else:
        speak("Good Night")
    speak(" How can I help you ")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        recognized_query = r.recognize_google(audio, language='en-in')
        print(recognized_query)

    except Exception as e:
        print(e)
        speak("I Can not get you !")
        return "None"
    return recognized_query


def send_email(_to_, _content_):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('EMAIL', 'PASSWORD')
    server.sendmail('EMAIL', _to_, _content_)
    server.close()


def screenshot():
    speak("What is the name of the image")
    file_name = take_command()
    img = pyautogui.screenshot()
    img.save('C:/screenshot/' + file_name + '.png')  # TODO remove this


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at {}".format(usage))
    battery = psutil.sensors_battery()
    speak("Battery percentage is")
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_joke())


if __name__ == "__main__":
    greeting()
    while True:
        query = take_command().lower()
        # Time
        if 'time' in query:
            time()

        # Date
        elif 'date' in query:
            date()

        # wikipedia search
        elif 'wiki' in query or 'wikipedia' in query:
            speak("Searching ....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        # Send Email
        elif 'send email' in query or 'send mail' in query:
            try:
                speak("What should I send?")
                content = take_command()
                speak("To who is this mail for")
                to = 'RECEIVER EMAIL'
                send_email(to, content)
                speak("Your Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send email")

        # Chrome Search
        elif 'google search' in query or 'chrome' in query:
            speak("What should I search? website or anything")
            take_command()
            if 'website' in query:
                speak("Please specify your website")
                chrome_path = 'C:/Program Files (x86)/Google/Chrome' \
                              '/Application/chrome.exe %s'  # TODO remove
                search = take_command().lower()
                wb.get(chrome_path).open_new_tab(search + '.com')
            else:
                speak("What should I Search")
                chrome_path = 'C:/Program Files (x86)/Google/Chrome' \
                              '/Application/chrome.exe %s'  # TODO remove
                search = take_command().lower()
                wb.get(chrome_path).open_new_tab(search)

                # log out your system
        elif 'log out' in query:
            os.system("shutdown -l")

        # shutdown your system
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        # restart your computer
        elif 'restart' in query or 'reboot' in query:
            os.system("shutdown /r /t 1")

        # play songs
        elif 'play song' in query or 'play' in query:
            songs_dir = 'YOUR SONG DIR'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        # remember function
        elif 'remember' in query:
            speak("what should I remember?")
            to_remember = take_command()
            speak('Alright you said me to remember' + to_remember)
            remember = open('data.txt', 'w')
            remember.write(to_remember)
            remember.close()

        # remember function contd.
        elif 'do you know anything' in query or 'did I tell you something' in query:
            remember = open('data.txt', 'r')
            speak('you said me remember that' + remember.read())

        # screen shot
        elif 'screenshot' in query:
            screenshot()
            speak('Taken a screen shot')

        # CPU Usage
        elif 'usage' in query or 'cpu' in query:
            cpu()

        # Jokes
        elif 'jokes' in query or 'joke' in query:
            jokes()

        # close the assistant
        elif 'offline' in query or 'sleep' in query:
            speak("Zen will always be there for your help")
            quit()
