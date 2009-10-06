import os
import sys
from common.appenginepatch.main import *

#  add 'libs' and 'apps' to python path. 
currentpath = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(currentpath, "libs"))
sys.path.insert(0, os.path.join(currentpath, "apps"))

if __name__ == '__main__':
    main()