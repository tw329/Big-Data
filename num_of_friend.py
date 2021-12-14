from mrjob.job import MRJob

class MRWordCount(MRJob):
    '''count word frequency'''
    def mapper(self, _, line):
        (ID, name,age, Num_friends) = line.split(',')
        for i in age:
            yield age, Num_friends
    def reducer(self, key, values):
        yield key, sum(values)
if __name__ == '__main__':
    MRWordCount.run()