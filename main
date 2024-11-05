import yt_dlp

def download_youtube_video(url):
    ydl_opts = {
        'format': 'bestvideo[height>=1080]+bestaudio[ext!=opus]/best[height>=1080]',
        'outtmpl': '%(title)s.%(ext)s',  # Nome do arquivo de saída
        'merge_output_format': 'mp4',    # Formato final do vídeo
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',     # Garantir que o vídeo esteja em formato MP4
        }],
        'postprocessor_args': ['-c:a', 'aac', '-b:a', '192k'],  # Converter áudio para AAC
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download concluído com sucesso!")
    except Exception as e:
        print(f"Erro durante o download: {e}")

# URL do vídeo que deseja baixar
video_url = input("Digite a URL do vídeo do YouTube: ")
download_youtube_video(video_url)
