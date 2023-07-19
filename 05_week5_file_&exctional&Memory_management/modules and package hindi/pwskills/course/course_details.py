import os ,sys
from os.path import dirname , join , abspath

sys.path.insert(0, abspath(join(dirname(__file__),'..')))


def course():
    print("this is my course details")
