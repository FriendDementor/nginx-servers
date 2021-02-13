import argparse
import jinja2

from sites import sites_function # pylint: disable=import-error

# from .add import add
# from .delete import delete
# from .ssl import ssl
# from .enable import enable
# from .disable import disable

def consume_and_print(function):
    return lambda args: print(function(args))

# create the top-level parser
nsc_parser = argparse.ArgumentParser()
subparsers = nsc_parser.add_subparsers()

# create the parser for the "sites" command
parser_list = subparsers.add_parser('list')
parser_list.set_defaults(func=consume_and_print(sites_function))

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

