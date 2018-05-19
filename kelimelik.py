class Word:

    def __init__(self):
        self._count = 2
        self._word = ""
        self._joker = False

    @property
    def count(self):
        return self._count

    @property
    def word(self):
        return self._word

    @property
    def joker(self):
        return self._joker

    @word.setter
    def word(self, word):
        self._word = str(word)

    @count.setter
    def count(self, count):
        if count > 2:
            self._count = count
        else:
            self._count = 1

    @joker.setter
    def joker(self, joker):
        try:
            self._joker = bool(joker)
        except:
            self._joker = False
            raise BaseException("Joker must be Bool")
