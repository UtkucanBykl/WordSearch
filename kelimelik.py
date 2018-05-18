class Word:

    def __init__(self):
        self.__count = 2
        self.__word = ""
        self.__joker = False

    @property
    def count(self):
        return self.__count

    @property
    def word(self):
        return self.__word

    @property
    def joker(self):
        return self.__joker

    @word.setter
    def word(self, word):
        self.__word = str(word)

    @count.setter
    def count(self, count):
        if count > 2:
            self.__count = count
        else:
            self.__count = 1

    @joker.setter
    def joker(self, joker):
        try:
            self.__joker = bool(joker)
        except:
            self.__joker = False
            raise BaseException("Joker must be Bool")
