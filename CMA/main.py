import tensorflow as tf
import transformers
from flask import Flask, render_template, request
import numpy as np
from huggingface_hub import from_pretrained_keras
import tensorflow_hub as hub

app = Flask(__name__)


class BertSemanticDataGenerator(tf.keras.utils.Sequence):
    """Generates batches of data."""

    def __init__(
            self,
            sentence_pairs,
            labels,
            batch_size=32,
            shuffle=True,
            include_targets=True,
    ):
        self.sentence_pairs = sentence_pairs
        self.labels = labels
        self.shuffle = shuffle
        self.batch_size = batch_size
        self.include_targets = include_targets
        # Load our BERT Tokenizer to encode the text.
        # We will use base-base-uncased pretrained model.
        self.tokenizer = transformers.BertTokenizer.from_pretrained(
            "bert-base-uncased", do_lower_case=True
        )
        self.indexes = np.arange(len(self.sentence_pairs))
        self.on_epoch_end()

    def __len__(self):
        # Denotes the number of batches per epoch.
        return len(self.sentence_pairs) // self.batch_size

    def __getitem__(self, idx):
        # Retrieves the batch of index.
        indexes = self.indexes[idx * self.batch_size: (idx + 1) * self.batch_size]
        sentence_pairs = self.sentence_pairs[indexes]

        # With BERT tokenizer's batch_encode_plus batch of both the sentences are
        # encoded together and separated by [SEP] token.
        encoded = self.tokenizer.batch_encode_plus(
            sentence_pairs.tolist(),
            add_special_tokens=True,
            max_length=128,
            return_attention_mask=True,
            return_token_type_ids=True,
            pad_to_max_length=True,
            return_tensors="tf",
        )

        # Convert batch of encoded features to numpy array.
        input_ids = np.array(encoded["input_ids"], dtype="int32")
        attention_masks = np.array(encoded["attention_mask"], dtype="int32")
        token_type_ids = np.array(encoded["token_type_ids"], dtype="int32")

        # Set to true if data generator is used for training/validation.
        if self.include_targets:
            labels = np.array(self.labels[indexes], dtype="int32")
            return [input_ids, attention_masks, token_type_ids], labels
        else:
            return [input_ids, attention_masks, token_type_ids]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/checkMyAnswer")
def checkMyAnswer():
    return render_template("checkMyAnswer.html")

@app.route("/answers")
def answers():
    return render_template("answers.html")


model = from_pretrained_keras("keras-io/bert-semantic-similarity")
# model = tf.keras.models.load_model('saved_model_pooja.h5')
# model = tf.keras.models.load_model(
#        ('saved_model_pooja.h5'),
#        custom_objects={'TFBertMainLayer':hub.TFBertMainLayer}
# )
labels = ["Contradiction", "Perfect", "Neutral"]


def check_similarity(sentence1, sentence2):
    sentence_pairs = np.array([[str(sentence1), str(sentence2)]])
    test_data = BertSemanticDataGenerator(
        sentence_pairs, labels=None, batch_size=1, shuffle=False, include_targets=False,
    )
    probs = model.predict(test_data[0])[0]

    labels_probs = {labels[i]: float(probs[i]) for i, _ in enumerate(labels)}
    return labels_probs

    # idx = np.argmax(proba)
    # proba = f"{proba[idx]*100:.2f}%"
    # pred = labels[idx]
    # return f'The semantic similarity of two input sentences is {pred} with {proba} of probability'


@app.route("/predict", methods=["POST"])
def predict():
    if request.method == 'POST':
        student_ans = request.form.get('student_ans')
        model_ans = request.form.get('model_ans')
        print(student_ans)
        print(model_ans)
        text = check_similarity(student_ans, model_ans)
        print(text)

        con_val = int(text["Contradiction"] * 100)
        per_val = int(text["Perfect"]*100)
        neu_val = int(text["Neutral"]*100)

        dict = {}
        dict['Contradiction'] = con_val
        dict['Perfect'] = per_val
        dict['Neutral'] = neu_val
        dict['student_ans'] = student_ans
        dict['model_ans'] = model_ans
        dict['marks'] = per_val 
        return render_template('answers.html', dict=dict)
    return render_template("index.html")


@app.route("/result")
def result():
    return render_template("result.html")


if __name__ == '__main__':
    app.run()
