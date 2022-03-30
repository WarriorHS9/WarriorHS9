import os
import random
import speech_recognition
import pyaudio
import webbrowser as wb
import pyautogui as p
import keyboard as k
from datetime import datetime
import win10toast
import lxml

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
toast = win10toast.ToastNotifier()
while True:
    def music():
        name = input('введите название песни: ')
        wb.open('www.youtube.com')
        #clicks that press on coordinates, if they press wrong, just change the first 2 numbers
        p.click(32, 988, 2, 5)
        p.click(701, 123, 2, 3)
        k.write(name)
        p.click(1341, 124, 1, 3)
        p.click(1545, 112, 2, 5)
        p.click(691, 361, 1, 1)

    def listen():
        try:
            with speech_recognition.Microphone() as mic:

                sr.adjust_for_ambient_noise(source= mic, duration= 0.5)
                audio = sr.listen(source = mic)
                query = sr.recognize_google(audio_data = audio, language = 'ru-RU').lower()
            return query
        except speech_recognition.UnknownValueError:
            return 'Тебя не слышно'

    def hello():
        return 'привет братишка'

    def open_browser():
        os.startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

    def open_zoom():
        os.startfile(r"C:\Users\KolyaN\AppData\Roaming\Zoom\bin\Zoom.exe")

    def reminder():
        print('Introduce the time when you will take the reminder: ')
        now = datetime.now()
        hour = str(input('Introduce the hour: '))
        minutes = str(input('Introduce the minutes: '))
        acutual_hour = str(now.strftime("%H"))
        actual_minute = str(now.strftime("%M"))
        print('Tell us the task')
        query = listen()
        if acutual_hour == hour and actual_minute == minutes:
            toast.show_toast('Your reminder', '{query}')
        else:
            print('smth is wrong')

    def main():
        query = listen()
        if query == 'привет':
            print(hello())
        elif query == 'музыка':
            print(music())
        elif query == 'открыть браузер':
            print(open_browser())
        elif query == 'урок':
            print(open_zoom())
        elif query == 'напомни':
            print(reminder())
        else:
            print('я тебя не понимаю ( ')

    if __name__ == '__main__':
        main()
