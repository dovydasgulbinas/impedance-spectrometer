import math, random



class SineIterable(object):
    def __init__(self, xmin, xmax):
        self.xrange = range(xmin, xmax)

    def __iter__(self):
        for x in self.xrange:
            yield math.sin(x) + random.random() * 1.0
            #yield random.random()



if __name__ == '__main__':
    iter_sine = SineIterable(0,200)

    for y in iter_sine:
        print(y)

    sins = [y for y in iter_sine]

    print(sins)