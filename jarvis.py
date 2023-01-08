import vosk
import sys
import torch
import config
import pyautogui as pg
import os
import speech_recognition as sr
import time
import random
import sounddevice as sd
import queue
import webbrowser
import datetime
import subprocess
import Microphone

# Variable Jarvis
language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
doc = 40000
speakers = 'aidar'
put_accent = True
put_yoo = True
device = torch.device('cpu')
Hello = "Здравствуйте, джарвис на связи!"
bye = "Досвидания" or "отключаюсь"
complite_command = "есть сер" or "запрос выполнен сер" or "готово"
error_command = "команда не распознана, отключаюсь" or "я вас не распознал повторите попытку" or "такой команды не существует"
see_ya = "Jarvis: " + "до встречи"
urlMusic = "https://www.youtube.com/watch?v=6yme5DtoLaQ&list=RD59Sy6ORiEIQ&index=4"
merry = "Jarvis: " + "как пожелаете"

# Variables Speaker
rec = sr.Recognizer()
rec.pause_threshold = 0.5

def Jarvis():
    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                              model='silero_tts',
                              language=language,
                              speaker=model_id)

    model.to(device)

    audio = model.apply_tts(text=Hello,
                            speaker=speakers,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yoo)

    print("Jarvis: " + Hello)
    sd.play(audio, sample_rate)
    time.sleep(len(audio) / doc)

def command_Error():
    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                              model='silero_tts',
                              language=language,
                              speaker=model_id)

    model.to(device)

    audio = model.apply_tts(text=error_command,
                            speaker=speakers,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yoo)

    print("Jarvis: " + error_command)
    sd.play(audio, sample_rate)
    time.sleep(len(audio) / doc)

def Bye():
    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                              model='silero_tts',
                              language=language,
                              speaker=model_id)

    model.to(device)

    audio = model.apply_tts(text=bye,
                            speaker=speakers,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yoo)

    print("Jarvis: " + bye)
    sd.play(audio, sample_rate)
    time.sleep(len(audio) / doc)

def SeeYa():
    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                              model='silero_tts',
                              language=language,
                              speaker=model_id)

    model.to(device)

    audio = model.apply_tts(text=see_ya,
                            speaker=speakers,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yoo)

    print("Jarvis: " + see_ya)
    sd.play(audio, sample_rate)
    time.sleep(len(audio) / doc)

def Time_and_date():
    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                              model='silero_tts',
                              language=language,
                              speaker=model_id)

    model.to(device)

    audio = model.apply_tts(text="Сейчас " + f'{now.hour} и {now.minute}',
                            speaker=speakers,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yoo)

    print("Jarvis: " + 'Cейчас ' + str(now.hour) + ':' + str(now.minute))
    sd.play(audio, sample_rate)
    time.sleep(len(audio) / doc)


def YouSure():
    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                              model='silero_tts',
                              language=language,
                              speaker=model_id)

    model.to(device)

    audio = model.apply_tts(text="вы уверены",
                            speaker=speakers,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yoo)

    print("Jarvis: " + "вы уверены?")
    sd.play(audio, sample_rate)
    time.sleep(len(audio) / doc)


def Music_Play():
    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                              model='silero_tts',
                              language=language,
                              speaker=model_id)

    model.to(device)

    audio = model.apply_tts(text=merry,
                            speaker=speakers,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yoo)

    print(merry)
    sd.play(audio, sample_rate)
    time.sleep(len(audio) / doc)

def Music_Stop():
    model, _ = torch.hub.load(repo_or_dir='snakers4/silero-models',
                              model='silero_tts',
                              language=language,
                              speaker=model_id)

    model.to(device)

    audio = model.apply_tts(text=merry,
                            speaker=speakers,
                            sample_rate=sample_rate,
                            put_accent=put_accent,
                            put_yo=put_yoo)

    print(merry)
    sd.play(audio, sample_rate)
    time.sleep(len(audio) / doc)


with sr.Microphone() as source:
    print("скажите команду...")
    rec.adjust_for_ambient_noise(source=source, duration=0.5)
    audio = rec.listen(source=source)
    query = rec.recognize_google(audio_data=audio, language='ru-RU').lower()
    print("вы: " + query)

    if(query == "джарвис"):
        Jarvis()
    elif(query == "отключись"):
        Bye()
        exit()
    elif(query == config.Shut_Down):
        YouSure()
    elif(query == 'да'):
        SeeYa()
        os.system('shutdown /s /t 0')
    elif(query == config.Restart):
        YouSure()
    elif(query == 'да'):
        SeeYa()
        os.system('shutdown /r /t 0')
    elif(query == config.Censored):
        os.system('')