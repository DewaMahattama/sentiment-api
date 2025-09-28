from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
model_path = r"C:\Users\DELL\Documents\Kuliah\SMT4\PKL\KOMINFO-PROJECT\sentiment-api-python\indobert-berita"
sentiment_model = pipeline("sentiment-analysis", model=model_path)

label_map = {
    "LABEL_0": "negatif",
    "LABEL_1": "netral",
    "LABEL_2": "positif",
}

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    raw_result = sentiment_model(text)
    raw_label = raw_result[0]['label']
    score = raw_result[0]['score']

    mapped_label = label_map.get(raw_label, raw_label)

    result = {
        'label': mapped_label,
        'score': score
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False, port=5001)
