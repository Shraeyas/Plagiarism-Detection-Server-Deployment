from flask import Flask, render_template, request, jsonify
from document_similarity import get_document_similarity
from sentence_similarity import get_sentence_similarity
import re

app = Flask (__name__)

@app.route ('/')
def homepage ():
    return render_template ('bot.html')

@app.route ('/api/document_similarity', methods = ['POST'])
def get_similarity ():
    document_0 = request.form['doc_0']
    document_1 = request.form['doc_1']
    _document_0 = re.sub(r"[^a-zA-Z0-9]","", document_0)
    _document_1 = re.sub(r"[^a-zA-Z0-9]","", document_1)
    document_similarity = get_document_similarity (_document_0, _document_1)
    sentence_similarity = get_sentence_similarity (_document_0, _document_1)

    dict = {}
    dict ["doc_similarity"] = document_similarity
    dict ["sen_similarity"] = sentence_similarity

    return jsonify (dict)

if __name__ == '__main__':
    app.run ()
