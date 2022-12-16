# -*- coding: utf-8 -*-

import os
import json


class Conf:

    PROJ_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self):
        self.filename = ""
    #     self.PROJ_DIR = self.load_conf(self.filename).get("proj_dir")

    def load_conf(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)

if __name__ == "__main__":
    pass