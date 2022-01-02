DICTIONARY_FILE = "my_nouns_ru.csv"


def read_words(filename: str):
    try:
        with open(filename, "r", encoding='utf-8') as f:
            while True:
                try:
                    yield next(f).strip()
                except StopIteration:
                    break
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    it = iter(read_words(DICTIONARY_FILE))
    print(next(it))
    print(next(it))
    print(next(it))
