#!/usr/bin/env python3
# coding=utf-8

import argparse
import codecs
import logging
import re
import sys
from pathlib import Path

parser = argparse.ArgumentParser()
logger = logging.getLogger()


def _setup_logging(verbosity: int):
    logger.setLevel(1)
    stream = logging.StreamHandler(sys.stderr)
    formatter = logging.Formatter('[%(asctime)s - %(name)s - %(levelname)s] - %(message)s')
    stream.setFormatter(formatter)
    logger.addHandler(stream)

    if verbosity > 0:
        stream.setLevel(logging.DEBUG)
    else:
        stream.setLevel(logging.INFO)


def _add_arguments():
    parser.add_argument('-v', '--verbosity', action='count', default=0)
    parser.add_argument('file')
    string = parser.add_mutually_exclusive_group()
    string.add_argument('-s', '--match-string')
    string.add_argument('-t', '--text')


def main(args: argparse.Namespace):
    _setup_logging(args.verbosity)
    args.file = Path(args.file).resolve().expanduser()
    if args.match_string:
        match_string = re.split(r'[, ;]+', args.match_string)
        match_string = [int(s) for s in match_string]
    else:
        in_text = re.split(r'\W+', args.text.strip())
        match_string = [len(s) for s in in_text]

    logger.info(f'Using pattern {", ".join([str(m) for m in match_string])}')

    regex_string = [rf'\w{{{int(length)}}}'for length in match_string]
    regex_string = r'\W+?'.join(regex_string)
    regex_string = r'\W' + regex_string + r'\W'

    with codecs.open(str(args.file), 'r', errors='ignore', encoding='latin1') as file:
        corpus = file.read()

    pattern = re.compile(regex_string)
    logger.info('Searching corpus for pattern...')
    corpus_matches = re.findall(pattern, corpus)
    logger.info(f'{len(corpus_matches)} matches found in corpus')
    for m in corpus_matches:
        print(str(m).replace('\n', ' '))


def entry():
    _add_arguments()
    args = parser.parse_args()
    main(args)


if __name__ == '__main__':
    entry()
