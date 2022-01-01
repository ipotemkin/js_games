import pandas as pd
from random import randint


DICTIONARY_FILE = "my_nouns_ru.csv"


class Dictionary:

    def __init__(self):
        self.words = pd.DataFrame()
        self.load(DICTIONARY_FILE)

    def load(self, filename):
        try:
            self.words = pd.read_csv(filename)  # loading the dictionary
        except FileNotFoundError:
            print("Ошибка при загрузке словаря!")
            exit()

    def get_words_count(self):
        return int(self.words.size) - 1

    def get_word_with_pk(self, pk: list[int]):
        return list(self.words.loc[pk]['word'])

    def get_random_words(self, n: int):
        max_words = self.get_words_count()
        if n > max_words:
            print("Длина списка больше словаря")
            exit()
        pk_lst = []
        for i in range(0, n):
            while True:
                temp = randint(0, max_words)
                if temp not in pk_lst:
                    break
            pk_lst.append(temp)
        return self.get_word_with_pk(pk_lst)

    def make_words_from_letters(self, game_word) -> set:
        """
        Makes words from the GAME_WORD's letters using the dictionary
        :return: a set of words
        """

        df_words = self.words.loc[self.words['word'].apply(self.check_word_from_letters, game_word=game_word)]
        return set(df_words['word'])

    def check_word_from_letters(self, word, game_word) -> bool:
        """
        Checks whether the word consists of the GAME_WORD's letters - the special function to use
        in the dictionary's dataframe.
        :param word: the word to check
        :param game_word: the word that supplies letters
        :return: True if the word consists of the GAME_WORD's letters, False if not
        """

        for letter in word:
            if letter in game_word:
                game_word = game_word.replace(letter, '', 1)
            else:
                return False
        return True

    def has_word(self, word: str) -> bool:
        """
        Checks whether the word is in the dataframe dictionary
        :param word: the word to find
        :return: True if the word exists or False if not
        """

        result_df = self.words.loc[self.words.word == word]
        if result_df.shape[0] > 0:
            return True
        return False


words = Dictionary()
print(words.get_random_words(5))
