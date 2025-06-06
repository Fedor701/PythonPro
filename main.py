import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import random
import emoji

translator = Translator()

z = 0
p = 0

def script():
    for i in range(9):
        global z, p
        random_word_emoji = random.choice(words)
        print(random_word_emoji)
        random_word = emoji.replace_emoji(random_word_emoji, replace='')
        
        duration = 5  # секунды записи
        sample_rate = 44100

        print("Говори...")
        recording = sd.rec(
        int(duration * sample_rate), # длительность записи в сэмплах
        samplerate=sample_rate,      # частота дискретизации
        channels=1,                  # 1 — это моно
        dtype="int16")               # формат аудиоданных
        sd.wait()  # ждём завершения записи

        wav.write("output.wav", sample_rate, recording)

        recognizer = sr.Recognizer()
        with sr.AudioFile("output.wav") as source:
            audio = recognizer.record(source)
        
        # Блок кода с переводом слова
        translation = translator.translate(random_word, src='ru', dest='en')
        english_word = translation.text
        translation_emoji = translator.translate(random_word_emoji, src='ru', dest='en')
        english_word_emoji = translation_emoji.text       
        # 
        index = 2
        english_word_emoji = english_word_emoji[:index] + english_word_emoji[index].upper() + english_word_emoji[index + 1:]
        english_word = english_word.capitalize()
        
        try:
            text_n = recognizer.recognize_google(audio, language="en")
            
        except sr.UnknownValueError:             # - если Google не понял речь (шум, молчание)
            print("Не удалось распознать речь; Правильный ответ: ", english_word_emoji)
            text_n = "Не удалось распознать речь"
            z += 1
            print("Ваши очки: ", p)
            print("Количество ошибок: ", z)
            if z != 3 and p != 10:
                print('-----------------------------------')
   
        except sr.RequestError as e:             # - если нет интернета или API недоступен
            print(f"Ошибка сервиса: {e}")
            break
        
        text_n = text_n.capitalize()
        # english_word = english_word.capitalize()
        
        if  english_word == text_n:
            p += 1
            print("Молодец! Ты сказал:", english_word_emoji, ". И это правильный ответ.")
            print("Ваши очки: ", p)
            print("Количество ошибок: ", z)
            if z != 3 and p != 10:
                print('-----------------------------------')
        if  text_n != "Не удалось распознать речь" and english_word != text_n:
            z += 1
            print("Неправильно! Ты сказал:", "🌍",text_n, "; Правильный ответ: ", english_word_emoji)
            print("Ваши очки: ", p)
            print("Количество ошибок: ", z)
            if z != 3 and p != 10:
                print('-----------------------------------')
        if z == 3:
            print('=======================================================')
            print('Вы проиграли. Вы набрали 3 штрафных очка.')
            print('=======================================================')
            break
        if p == 10: 
            print('=======================================================')
            print('Вы прошли испытание. Вы набрали 10 очков.')
            print('=======================================================')
            break

print("Это приложение тебе поможет научиться правильно выговаривать английские слова!")
print("Правила: Тебе нужно выбрать классификацию слова. Затем тебе будет выдано слово по этой теме. \nСлово нужно будет перевести за 10 секунд на английский и произнести его правильное произношение. \nУ тебя будет 3 попытки отгадать 10 слов одной категории.")
print("Выбери категорию слова: животные, фрукты и овощи, предметы быта, природа, эмоции и действия, профессии, транспорт, цвета, части тела, разное.")
print('=======================================================')
choice_user = input("Твой выбор: ")
print('=======================================================')

if choice_user == 'животные':
    with open("animals.txt", "r", encoding="utf-8") as file:
        words = file.read().splitlines()
    script()
    
elif choice_user == 'части тела':
    with open("body_parts.txt", "r", encoding="utf-8") as file:
        words = file.read().splitlines()
    script()
    
elif choice_user == 'цвета':
    with open("colors.txt", "r", encoding="utf-8") as file:
        words = file.read().splitlines()
    script()

elif choice_user == 'эмоции и действия':
    with open("emotions_and_actions.txt", "r", encoding="utf-8") as file:
        words = file.read().splitlines()
    script()
    
elif choice_user == 'предметы быта':
    with open("household_items.txt", "r", encoding="utf-8") as file:
        words = file.read().splitlines()
    script()
    
elif choice_user == 'природа':
    with open("nature.txt", "r", encoding="utf-8") as file:
        words = file.read().splitlines()
    script()
    
elif choice_user == 'профессии':
    with open("professions.txt", "r", encoding="utf-8") as file:
        words = file.read().splitlines()
    script()
    
elif choice_user == 'транспорт':
    with open("transport.txt", "r", encoding="utf-8") as file:
        words = file.read().splitlines()
    script()

elif choice_user == 'разное':
    with open("various.txt", "r", encoding="utf-8") as file:
        words = file.read().splitlines()
    script()
    
elif choice_user == 'фрукты и овощи':
    with open("vegetables_and_fruites.txt", "r", encoding="utf-8") as file:
        words = file.read().splitlines()
    script()
    
else:
    print('Введите одну из доступных категорий.')

        
