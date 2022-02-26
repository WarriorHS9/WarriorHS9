import os
import random
import speech_recognition
import pyaudio
import webbrowser as wb
import pyautogui as p
import keyboard as k
import datetime
import win10toast
print('main functions of this app are oppening files(zoom, browser), puttiong on music from youtube, and greet you')
sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5
toast = win10toast.ToastNotifier()
def music():
    name = input('введите название песни: ')
    wb.open('www.youtube.com')
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


def task():
    print('Что будем делать сегодня? ')
    query = listen() 
    with open('list.txt', 'a') as file:
        file.write(f'!{query}\n')
    return f'Задача {query} добавлена в список.'

def open_browser():
    os.startfile(r"C:\Users\KolyaN\AppData\Local\Programs\Opera GX\launcher.exe")

def open_zoom():
    os.startfile(r"C:\Users\KolyaN\AppData\Roaming\Zoom\bin\Zoom.exe")
def reminder():
    query = listen()
    print('Introduce the time when you will take the reminder: ')
    year = int(input('Introduce the year:'))
    day = int(input('introduce the day: '))
    hour = int(input('intruduce the hour: '))
    min = int(input('introduce the minutes: '))
    toast.show_toast('U have a reminde', '{query}')
def main():
    query = listen()
    if query == 'привет':
        print(hello())
    elif query == 'добавить задачу':
        print(task())
    elif query == 'музыка':
        print(music())
    elif query == 'открыть браузер':
        print(open_browser())
    elif query == 'урок':
        print(open_zoom())
    else:
        print('я тебя не понимаю ( ')

if __name__ == '__main__':
    main()