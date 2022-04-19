import logging
import sys
import os.path
from typing import List

from src.libs.DBExtractor import DBExtractor


def main(args: List[str]):
    try:
        basepath = os.getcwd()
        config_json_string = '\config\exercise-atlax360.json'
        config_full_string = basepath + config_json_string
        os.path.isfile(config_full_string)
        try:
            extractor = DBExtractor(basepath, config_full_string)
        except Exception:
            print("Can't load configuration file %s" % config_full_string)
        if len(args) != 1: print("missing required argument target file")
        else:
            extractor.extract(args[0])
    except Exception as e:
        logging.info(e)


main(sys.argv[1:])
