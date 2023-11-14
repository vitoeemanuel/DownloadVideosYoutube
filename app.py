from flask import Flask, render_template, request, redirect
from pytube import YouTube

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['url']
        try:
            yt = YouTube(video_url)
            stream = yt.streams.first()
            stream.download('downloads')  # Salva o vídeo na pasta 'downloads'
            return redirect('/')
        except Exception as e:
            error_message = f"Erro: {str(e)}"
            return render_template('index.html', error_message=error_message)

    return render_template('index.html', error_message=None)

if __name__ == '__main__':
    app.run(debug=True)
