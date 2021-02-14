import os
import shutil

# this is only one that can delete files
# in the /html folder and /etc/nginx/sites-enabled/

# disable
# command to disable a web from server
#
# example:
# $ nginx disable example.com

# for each execution of this function will delete
# this file: /etc/nginx/sites-enabled/domain.conf
def disable(domain):
    conf_path = '/etc/nginx/sites-enabled/{}.conf'.format(domain)
    bOk = os.path.exists(conf_path)
    if bOk:
        os.unlink(conf_path)
        return "OK"
    return "ERROR" # this error will show when the file exists
