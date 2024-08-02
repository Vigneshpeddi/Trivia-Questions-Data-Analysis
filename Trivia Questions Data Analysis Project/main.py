import json
from scrapers import scrape_quizbreaker, scrape_brightful_trivia
from wc import generate_wordcloud, get_word_frequency, plot_word_frequency

def main():
    json_file = "trivia.json"

    scrape_quizbreaker()
    scrape_brightful_trivia()

    try:
        with open(json_file, "r") as file:
            data = json.load(file)
        questions = [item["Question"] for item in data]
        answers = [item["Answer"] for item in data]
        text = " ".join(questions + answers)
        generate_wordcloud(text)

        word_frequency = get_word_frequency(data)
        plot_word_frequency(word_frequency)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
