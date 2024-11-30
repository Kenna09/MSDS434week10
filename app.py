from flask import Flask, request, jsonify
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained model and tokenizer
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

@app.route("/ping", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get the input text
        input_data = request.get_json()
        text = input_data["text"]

        # Tokenize and predict
        inputs = tokenizer(text, return_tensors="pt")
        outputs = model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        positive_score = predictions[0][1].item()
        negative_score = predictions[0][0].item()

        return jsonify({
            "text": text,
            "positive_score": positive_score,
            "negative_score": negative_score,
            "sentiment": "positive" if positive_score > negative_score else "negative"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
