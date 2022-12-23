# -*- coding:utf-8 -*-

import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURRENT_DIR)
sys.path.extend([os.path.join(CURRENT_DIR, dir_) for dir_ in os.listdir(CURRENT_DIR)])

from gui.MainWindow import main


if __name__ == "__main__":
    #
    main()
