import pandas

class Definition:
    """A class that takes a term and looks it up in the spreadsheet"""
    def __init__(self, term):
        self.term = term

    def get(self):
        df = pandas.read_csv(r'C:\Users\alexb\PycharmProjects\App-8-Instant-Dictionary-Webapp\data.csv')
        return tuple(df.loc[df['word']==self.term]['definition'])

if __name__ == '__main__':
    acid = Definition('acid')
    print(acid.get())