# get the second from the date
from datetime import datetime

dt = datetime.now()


def is_odd(n):
    if n % 2 == 0:
        raise ValueError('The value %d is not odd.' % n)
    else:
        return n


try:
    print("This value is ODD -> %d" % is_odd(dt.second))
except Exception as e:
        print str("Danger! %s" % e)
