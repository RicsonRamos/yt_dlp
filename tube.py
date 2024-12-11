from yt_dlp import YoutubeDL

video_links = ['https://youtube.com/live/SUyycXw4jTg',
'https://www.youtube.com/live/ITc0oDwY3CA',
'https://youtube.com/live/ITc0oDwY3CA',
'https://youtube.com/live/_xWV-HIaGPM',
'https://youtube.com/live/KKegoBYobxY',
'https://youtube.com/live/C4lRMBOc-EQ',
'https://youtube.com/live/3cyokYhCq7w',
'https://youtu.be/cN8ZdmP7sJc',
'https://youtu.be/XJN50KMJ1Q0',
'https://youtu.be/nJgITKqratg'
]
path_to_download = r"E:\Documentos\VsCode\pytube"


# Configurações para o yt_dlp

ydl_opts = {
    'format': 'best[height<=1080]',
    'outtmpl': f'{path_to_download}/Aula-%(autonumber)s-%(title)s.%(ext)s',
}

# Realizando o download dos vídeos
with YoutubeDL(ydl_opts) as ydl:
    ydl.download(video_links)


print(f"Download concluído! O vídeo foi salvo em: {path_to_download}")
