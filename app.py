from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS 
from dotenv import load_dotenv
import openai
import os
from gtts import gTTS
import uuid

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
STATIC_FOLDER = "static"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

def transcrever_audio(caminho_audio):
    with open(caminho_audio, "rb") as audio:
        transcricao = openai.audio.transcriptions.create(
            file=audio,
            model="whisper-1"
        )
    return transcricao.text

def perguntar_chatgpt(texto):
    resposta = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente educado e claro."},
            {"role": "user", "content": texto}
        ]
    )
    return resposta.choices[0].message.content

def texto_para_voz(texto):
    nome_arquivo = f"resposta_{uuid.uuid4().hex}.mp3"
    caminho = os.path.join(STATIC_FOLDER, nome_arquivo)

    tts = gTTS(text=texto, lang="pt-br")
    tts.save(caminho)

    return nome_arquivo

@app.route("/audio", methods=["POST"])
def receber_audio():
    if "audio" not in request.files:
        return jsonify({"erro": "Nenhum áudio enviado"}), 400

    audio = request.files["audio"]

    nome_audio = f"{uuid.uuid4().hex}.wav"
    caminho_audio = os.path.join(UPLOAD_FOLDER, nome_audio)
    audio.save(caminho_audio)

    texto_usuario = transcrever_audio(caminho_audio)

    resposta_chatgpt = perguntar_chatgpt(texto_usuario)

    audio_resposta = texto_para_voz(resposta_chatgpt)

    return jsonify({
        "transcricao": texto_usuario,
        "resposta": resposta_chatgpt,
        "audio_url": f"http://localhost:5000/static/{audio_resposta}"
    })

@app.route("/static/<path:filename>")
def servir_audio(filename):
    return send_from_directory(STATIC_FOLDER, filename)
    

if __name__ == "__main__":
    app.run(debug=True)
