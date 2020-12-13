import zipfile
import os
from string import punctuation


class TextLoader:
    def __init__(self, path):
        with zipfile.ZipFile(path, 'r') as zip_ref:
            zip_ref.extractall()
        self._name = os.path.splitext(path)[0]
        self.__files = os.listdir(self._name)
        self._pos = -1
    
    def __len__(self):
        return len(self.__files)

    def __iter__(self):
        return self
    
    @staticmethod
    def process_text(text):
        for i in punctuation:
            text = text.replace(i, '')
        return text.lower()

    def __next__(self):
        if self._pos == len(self) - 1:
            raise StopIteration()
        self._pos += 1
        path = self._name + '/' + self.__files[self._pos]
        with open(path, 'r') as inf:
            text = inf.read()

        with open(path, 'w') as ouf:
            ouf.write(TextLoader.process_text(text))

        return open(path, 'r')

if __name__ == '__main__':
    a = TextLoader('sample.zip')
    print(len(a))
    for i in a:
        print(i)
        break
