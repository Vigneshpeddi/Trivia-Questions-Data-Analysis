import requests
from bs4 import BeautifulSoup
import json

def scrape_quizbreaker(url="https://www.quizbreaker.com/blog/trivia-questions", output_file="trivia.json", start_question="What does “www” stand for in a website browser?"):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        trivia_elements = soup.find_all(["p", "div", "span", "li", "h1", "h2", "h3", "h4", "h5", "h6"])

        questions = []
        answers = []
        is_question = False

        for element in trivia_elements:
            text = element.get_text(strip=True)
            if text == start_question:
                is_question = True
            if is_question and text.endswith("?"):
                questions.append(text)
            elif is_question and text.startswith("Answer: "):
                answers.append(text)

        qa_pairs = [{"Question": q, "Answer": a} for q, a in zip(questions, answers)]

        with open(output_file, "w") as json_file:
            json.dump(qa_pairs, json_file, indent=2)

        print(f"Quizbreaker Question and Answers written to {output_file}")

    else:
        print(f"Response Status Code: {response.status_code}")

def scrape_brightful_trivia(url="https://www.brightful.me/blog/general-trivia-questions/", output_file="trivia.json"):
    with open(output_file, "r") as file:
        existing_data = json.load(file)

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        trivia_elements = soup.find_all(["p"])

        questions = []
        answers = []
        is_question = False

        for element in trivia_elements:
            text = element.get_text(strip=True)
            if text.startswith("Q: "):
                is_question = True
                current_question = text.replace("Q: ", "")
            elif is_question and text.startswith("Answer: "):
                current_answer = text.replace("Answer: ", "")
                is_question = False
                questions.append(current_question)
                answers.append(current_answer)

        new_qa_pairs = [{"Question": q, "Answer": a} for q, a in zip(questions, answers)]

        all_qa_pairs = existing_data + new_qa_pairs

        with open(output_file, "w") as json_file:
            json.dump(all_qa_pairs, json_file, indent=2)

        print(f"Brightful Trivia Question and Answers written to {output_file}")

    else:
        print(f"Response Status Code: {response.status_code}")
