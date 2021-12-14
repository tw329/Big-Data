from mrjob.job import MRJob

class Kmeans_3(MRJob):

    def dist(self,v,u):
        return ((u[0]-v[0])*(u[0]-v[0])+(u[1]-v[1])*(u[1]-v[1]))**(1/2)
      
    def mapper(self, _, line):
        start_mean = [[0, 0], [50, 50], [100, 100]]
        for l in line.split('\n'):
            x, y = l.split(',')
            data = [float(x),float(y)]
        min_dist=999999.0
        classes = 0

        for i in range(3):
            dist = self.dist(data, start_mean[i])
            if dist < min_dist:
                min_dist = dist
                classes = i
        yield classes, data
    
    def combiner(self,k,v):
        count = 0
        m_x=m_y=0.0
        for t in v:
            count += 1
            m_x+=t[0]
            m_y+=t[1]
        yield k, (m_x/count,m_y/count)

    def reducer(self, k, v):
        count = 0
        m_x=m_y=0.0
        for t in v:
            count += 1
            m_x+=t[0]
            m_y+=t[1]
        yield k, [m_x/count, m_y/count]
if __name__ == '__main__':
    Kmeans_3.run()