pip installl flask streamlit langchain openai

from flask import Flask, request
from langchain.document_loaders import YoutubeLoader
from langchain.llms import OpenAI
import streamlit as st

app = Flask(__name__)

OPENAI_API_KEY = "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"

def home():
    if request.method == 'POST':
        youtube_url = request.form['youtube_url']
        return process_youtube_url(youtube_url)
    return '''
        <html>
        <body>
            <h1>Enter YouTube URL:</h1>
            <form method="POST" action="/">
                <input type="text" name="youtube_url" placeholder="YouTube URL">
                <input type="submit" value="Submit">
            </form>
        </body>
        </html>
    '''

def process_youtube_url(youtube_url):
    loader = YoutubeLoader.from_youtube_url(youtube_url, add_video_info=True)
    result = loader.load()
    video_author = result[0].metadata['author']
    video_length = result[0].metadata['length']
    return f'''
        <html>
        <body>
            <h1>Result:</h1>
            <p>Found video from {video_author} that is {video_length} seconds long</p>
            <pre>{result}</pre>
        </body>
        </html>
    '''

@app.route('/')
def render_home():
    st.write('<h1>Enter YouTube URL:</h1>', unsafe_allow_html=True)
    youtube_url = st.text_input('YouTube URL', value='')
    if st.button('Submit'):
        result = process_youtube_url(youtube_url)
        st.write(result, unsafe_allow_html=True)

if __name__ == '__main__':
    app.run()
