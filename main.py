# importing libraries
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import speech_recognition as sr
import os
import webbrowser
import pyautogui

# create a speech recognition object
model = OllamaLLM(model='gemma3')
r = sr.Recognizer()
mic = sr.Microphone(device_index=2)

template = """
Você é um assistente virtual chamado jarvis e tem a tarefa de identificar ações
que o usuário deseja fazer e transcrever para alguma das possíbilidades

caso o usuário deseje abrir o navegador retorne 1
caso o usuário deseje abrir o bloco de notas retorne 2
"""

def ouvir_microfone():
    #Habilita o microfone para ouvir o usuario
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        #Chama a funcao de reducao de ruido disponivel na speech_recognition
        microfone.adjust_for_ambient_noise(source)
        #Avisa ao usuario que esta pronto para ouvir
        print("Diga alguma coisa: ")
        #Armazena a informacao de audio na variavel
        audio = microfone.listen(source)

    try:
        #Passa o audio para o reconhecedor de padroes do speech_recognition
        frase = microfone.recognize_google(audio,language='pt-BR')
        #Após alguns segundos, retorna a frase falada
        print("Você disse: " + frase)
        return frase.lower()
        #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
    except sr.UnkownValueError:
        print("Não entendi")
    return frase

def executar_comando(comando):
    if "abrir navegador" in comando:
        webbrowser.open('https://www.google.com')
    elif "abrir notepad" in comando:
        os.system('notepad.exe')
    elif "digitar teste" in comando:
        pyautogui.write("Este é um teste de automação por voz!", interval=0.1)
    else:
        print("Comando não reconhecido.")

c = ouvir_microfone()
executar_comando(c)

