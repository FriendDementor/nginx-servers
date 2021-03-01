import os
import subprocess

def execute(command):
    result = subprocess.check_output(command.split())
    return result.decode("utf-8")

# this is only one that can create files
# in the folder /etc/nginx/sites-enabled/

# enable creates a simbolic link from sites_available
#
# example:
# $ nginx enable example.com
def enable(domain):
    available_path = '/etc/nginx/sites-available/{}.conf'.format(domain)
    enabled_path = '/etc/nginx/sites-enabled/{}.conf'.format(domain)

    bOk = not os.path.exists(enabled_path)
    bOk = bOk and os.path.exists(available_path)
    if bOk:
        os.symlink(available_path, enabled_path)
        execute("nginx -s reload")
        return "OK"
    return "ERROR" # this error will show when the file exists

