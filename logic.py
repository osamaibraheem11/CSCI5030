# This file will hold useful functions

import itertools

def tuple2list(ExTuple):
    ExList = list(itertools.chain(*ExTuple))
    return ExList 