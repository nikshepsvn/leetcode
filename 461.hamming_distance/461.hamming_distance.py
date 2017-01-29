class Solution(object):
    def hammingDistance(self, x, y):
        binx = "{0:050b}".format(x);
        biny = "{0:050b}".format(y);
        count=0

        for x in range (0, len(binx)):
            if (int(binx[x])!=int(biny[x])):
                count+=1
        return count;