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
            extractor = DBExtractor(config_full_string)
        except Exception:
            print("Can't load configuration file %s" % config_full_string)

        if len(args) != 1: print("missing required argument target file")
        else: extractor.extract(args[0])
    except:
        print("Can't locate %s" % config_full_string)
    finally:
        dump_csv = basepath + args[0]
        exits_csv = os.path.isfile(dump_csv)
        # todo ending class
        logging.INFO("Data dumped to csv on %s and gziped on %s" % basepath)


main(sys.argv[1:])
