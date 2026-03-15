import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

class OrderClassifier:

    def __init__(self):

        self.training_data = [
            ("barcode logistics label", "Label"),
            ("product qr code label", "Label"),
            ("hospital patient wristband", "Wristband"),
            ("event entry wristband", "Wristband"),
            ("clothing price tag", "Tag"),
            ("retail hanging tag", "Tag"),
            ("outdoor advertising signage", "Signage"),
            ("store display sign board", "Signage")
        ]

        texts = [t[0] for t in self.training_data]
        labels = [t[1] for t in self.training_data]

        self.vectorizer = TfidfVectorizer()
        X = self.vectorizer.fit_transform(texts)

        self.model = LogisticRegression()
        self.model.fit(X, labels)

    def predict(self, text):

        X = self.vectorizer.transform([text])
        return self.model.predict(X)[0]