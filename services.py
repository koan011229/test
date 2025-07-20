import yt_dlp
import whisper

def transcribe_youtube(url: str, out_dir: str = "downloads", model_size: str = "small") -> str:
    # 1. 유튜브 다운로드 옵션
    ydl_opts = {
        'outtmpl': f'{out_dir}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
    }

    # 2. 다운로드 실행
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

    # 3. Whisper 모델 로드 및 전사
    model = whisper.load_model(model_size)
    result = model.transcribe(filename)

    # 4. 텍스트 결과 반환
    return result


#video_url = "https://www.youtube.com/watch?v=Wn8X5JMgBAk"  # 원하는 유튜브 링크
#transcribed_text = transcribe_youtube(video_url)
#print(transcribed_text)