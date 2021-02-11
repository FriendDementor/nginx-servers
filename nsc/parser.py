#!/usr/bin/python3

import argparse
import jinja2

from .sites import sites
# from .add import add
# from .delete import delete
# from .ssl import ssl
# from .enable import enable
# from .disable import disable

# create the top-level parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

# create the parser for the "sites" command
parser_list = subparsers.add_parser('list')
parser_list.set_defaults(func=sites)

# # create the parser for the "add" command
# parser_add = subparsers.add_parser('add')
# parser_add.add_argument('domain')
# parser_add.set_defaults(func=add)

# # create the parser for the "ssl" command
# parser_ssl = subparsers.add_parser('ssl')
# parser_ssl.add_argument('domain')
# parser_ssl.set_defaults(func=ssl)

# # create the parser for the "enable" command
# parser_enable = subparsers.add_parser('enable')
# parser_enable.add_argument('domain')
# parser_enable.set_defaults(func=enable)

# # create the parser for the "disable" command
# parser_disable = subparsers.add_parser('disable')
# parser_disable.add_argument('domain')
# parser_disable.set_defaults(func=disable)

# parse the args and call whatever function was selected
if __name__ == '__main__':
    args = parser.parse_args()
    if len(vars(args)) == 0:
        parser.print_help()
    else:
        args.func(args)
