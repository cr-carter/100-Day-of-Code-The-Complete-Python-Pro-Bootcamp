import requests
import json

response = requests.get('https://opentdb.com/api.php?amount=20')
question_import = json.loads(response.text)
questions = question_import["results"]
question_data = []
for item in questions:
    if item["type"] == "boolean":
        question_data.append({"text": item["question"], "answer": item["correct_answer"]})

