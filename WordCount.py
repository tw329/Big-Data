from mrjob.job import MRJob

class MRWordCount(MRJob):
    '''count word frequency'''
    def mapper(self, _, line):
        words = line.split()
        for word in words:
            yield word.lower(), 1
    def reducer(self, key, values):
        yield key, sum(values)
if __name__ == '__main__':
    MRWordCount.run()