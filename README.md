# bootcampDados

Repositório contendo os conteúdos do Bootcamp DIO Bradesco - GenAI & Dados

# Descrição desafio 

🎙️ Conversando por Voz com o ChatGPT utilizando Whisper e Python
📌 Descrição do Projeto

Este projeto tem como objetivo desenvolver um sistema de conversação por voz utilizando Inteligência Artificial, integrando tecnologias de Speech-to-Text (STT) e Text-to-Speech (TTS).
A solução permite que o usuário faça perguntas por voz, que são interpretadas pelo modelo Whisper (OpenAI), processadas pelo ChatGPT, e respondidas em formato de áudio utilizando o Google Text-to-Speech (gTTS).

O projeto foi desenvolvido como parte de um desafio prático da Digital Innovation One (DIO), com foco na aplicação real de APIs de IA em Python.

# 🚀 Tecnologias Utilizadas

- Python 3.10+
- Whisper (OpenAI) – Reconhecimento de fala (Speech-to-Text)
- ChatGPT (OpenAI API) – Processamento de linguagem natural
- gTTS (Google Text-to-Speech) – Conversão de texto em voz
- python-dotenv – Gerenciamento de variáveis de ambiente

  # 🧠 Arquitetura da Solução

 O sistema segue o fluxo abaixo:

 🎤 Voz do usuário
   ->
📝 Whisper (Speech-to-Text)
   ->
🧠 ChatGPT (Processamento Inteligente)
   ->
🔊 gTTS (Text-to-Speech)
   ->
🎧 Áudio de resposta
