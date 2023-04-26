from yt_dlp import YoutubeDL

YDL_OPTIONS = {
    'nocheckcertificate': True,
    'noplaylist':True,
    "quiet": True,
    'extract_flat': True,
    'format': 'bestaudio/best',
    'outtmpl': './music/%(title)s.%(ext)s'
}


playlist = {0: ['Taka - Último Trago', 'https://www.youtube.com/watch?v=hGQvHnNDQkk', 227.0]}
with YoutubeDL(YDL_OPTIONS) as ydl:
    # ydl.download("https://www.youtube.com/watch?v=xiZW1VoytEg", )
    while True:
        def play():
            url = playlist[0][1]
            ydl.download([url])
        
        def search(arg):
            videos = ydl.extract_info(f"ytsearch3:{arg}", download=False)
            for idx, video in enumerate(videos['entries']):
                print(str(idx+1) + ")",video.get('title'))
            if len(videos['entries']) == 0:
                print("Nenhum resultado encontrado")
                return
            video_num = input("Escolha o Video: ")
            if video_num == "":
                return
            title = videos['entries'][int(video_num) - 1]['title']
            url = videos['entries'][int(video_num) - 1]['url']
            duration = videos['entries'][int(video_num) - 1]['duration']
            playlist.update({len(playlist):[title, url, duration]})
        
        def removeMusic():
            for idx, video in enumerate(playlist.values()):
                print(str(idx) + ")",video[0])
            video_num = input("Escolha o Video: ")
            if video_num == "":
                return
            del playlist[int(video_num)]            
                            
        def showPlaylist():
            for idx, video in enumerate(playlist.values()):
                print(str(idx) + ")",video[0])
                
        
        pesquisa = int(input("""
0 - Sair
1 - Tocar
2 - Adicione uma musica a playlist
3 - Remover uma musica da playlist
4 - Mostrar Playlist
        
Digite a opção: """))
        
        if pesquisa == 0:
            break
        elif pesquisa == 1:
            play()
        elif pesquisa == 2:
            pesquisa = input("Digite o nome da musica: ")
            search(pesquisa)
        elif pesquisa == 3:
            removeMusic()
        elif pesquisa == 4:
            showPlaylist()
            
