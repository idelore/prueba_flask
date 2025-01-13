# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 12:32:43 2025

@author: idelore
"""


from flask import Flask, request, jsonify

import openai

app = Flask(__name__)

# Configura tu clave API de OpenAI
openai.api_key = "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"

# Prompt inicial que define el comportamiento del chatbot
BASE_PROMPT = "Eres un asistente amable y eficiente especializado en ayudar con dudas técnicas."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get("user_input", "")
    prompt = f"{BASE_PROMPT}\nUsuario: {user_input}\nChatGPT:"
    
    # Generar la respuesta del modelo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": BASE_PROMPT},
                  {"role": "user", "content": user_input}],
        max_tokens=100
    )
    
    reply = response['choices'][0]['message']['content']
    return jsonify({"reply": reply})

@app.route('/export', methods=['POST'])
def export():
    interactions = request.json.get("interactions", [])
    filename = "interactions.txt"
    with open(filename, "w") as f:
        for interaction in interactions:
            f.write(f"Usuario: {interaction['user']}\n")
            f.write(f"ChatGPT: {interaction['chatgpt']}\n\n")
    return jsonify({"message": f"Interacciones exportadas a {filename}"})

if __name__ == "__main__":
    app.run(debug=True)