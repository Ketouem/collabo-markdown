import logging.config
import yaml


def init_logger(path):
    logging.config.dictConfig(yaml.load(open(path)))
