
# right now create from a static file

class Map:
    def __init__(self, map):
        l = [line.strip() for line in open(map).readlines()]
        print(l)
        self.map = [[None]*len(l[0]) for j in range(len(l))]
        for i in range(len(l[0])):
            for j in range(len(l)):
                tile = l[j][i]
                print(tile[j][i])
