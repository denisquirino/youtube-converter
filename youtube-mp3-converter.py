from pytube import YouTube
import moviepy.editor as mp
import re
import os
import PySimpleGUI as sg

sg.theme('DarkPurple')

layout = [
    [sg.Text('URL',size=(8,0)),sg.Input(size=(100,0),key='-URL-')],
    [sg.Text('Caminho',size=(8,0)),sg.Input(size=(100,0),key='-CAMINHO-')],
    [sg.Push(), sg.Button('Baixar'), sg.Push(), sg.Button('Cancelar'), sg.Push()],
    [sg.Output(size=(108,8))]
    ]

window = sg.Window('Download Áudio Youtube', layout=layout, finalize=True, enable_close_attempted_event=True)

while True:
    event, values = window.read()
    match(event):
        case 'Baixar':
            link = values["-URL-"]
            path = values["-CAMINHO-"]
            yt = YouTube(link)
            print("Baixando arquivo...\n")
            ys = yt.streams.filter(only_audio=True).first().download(path)
            for file in os.listdir(path):
                if re.search('mp4', file):
                    mp4_path = os.path.join(path, file)
                    mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
                    new_file = mp.AudioFileClip(mp4_path)
                    new_file.write_audiofile(mp3_path)
                    os.remove(mp4_path)
                    print("\nConversão de arquivo efetuada...")
                    sg.popup('Download realizado')
        case 'Cancelar':
            break
        case sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
            break
        case _:
            print(event, values)      
window.close()