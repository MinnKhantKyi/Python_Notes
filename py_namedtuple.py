# typename = namedtuple('typename', 'values')
# eg. Point = namedtuple('Point', 'x y z')
# newP = Point(3,4,5)
# Now x=3, y=4, z=5. Values are seperated by space.

import collections
from collections import namedtuple

if __name__ == "__main__":
    
    Point = namedtuple('Point', 'a b c')
    newP = Point(1,2,3)
    print(newP)
    newP2 = Point._make(['11','12','13'])
    print(newP2)

    List_Point = namedtuple('List_Point', ['d','e','f'])
    newLP = List_Point(4,5,6)
    print(newLP)
    print(newLP[0], newLP[1], newLP[2])

    Dist_Point = namedtuple('Dist_Point', {'g':0, 'h':0, 'i':0})
    newDP = Dist_Point(7,8,9)
    print(newDP)
    print(newDP.g, newDP.h, newDP.i)
    print(newDP[0], newDP[1], newDP[2])
    print(newDP._fields)

    newDP = newDP._replace(g=10)
    print(newDP)

    newP2 = Dist_Point._make(['11','12','13'])
    print(newP2)