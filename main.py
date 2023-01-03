from nltk.tokenize import word_tokenize

from pattern.en import pluralize, singularize


class Bot():
    def __init__(self):
        self.words = []

    """Add words to the bot's vocabulary
    Param words: list of words to add
    Return: None
    """
    def add_words(self, words):
        self.words.extend(words)
    
    """Singularize the words in the bot's vocabulary
    Param words: list of words to singularize
    Return: list of singularized words
    """
    def singularize_words(words):
        tokens = word_tokenize(words)
        return [singularize(word) for word in tokens]

    """Pluralize the words in the bot's vocabulary
    Param words: list of words to pluralize
    Return: list of pluralized words"""

    def pluralize_words(words):
        tokens = word_tokenize(words)
        return [pluralize(word) for word in tokens]
    
    def __str__(self) -> str:
        return str(self.words)


def main():
    bot = Bot()
    bot.add_words(["dogs", "cats", "monkeys"])
    print(bot)

    print(bot.singularize_words("dogs cats monkeys"))
    print(bot.pluralize_words("dog cat ox"))

if __name__ == "__main__":
    main()

