#!/usr/bin/python3

import os
import sys

from parser import nsc_parser # pylint: disable=no-name-in-module

# parse the args and call whatever function was selected
if __name__ == '__main__':
    args = nsc_parser.parse_args()
    if len(vars(args)) == 0:
        nsc_parser.print_help()
    else:
        args.func(args)