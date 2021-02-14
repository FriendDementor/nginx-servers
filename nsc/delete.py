import os
import shutil

# this is only one that can create files
# in the /html folder and /etc/nginx/sites-available/

# delete
# command to delete a web from server
#
# example:
# $ nginx delete example.com

# this function set the config and files to make
# a new page available to work
# for each execution of this function will delete
# two files: /html/domain/index.html
# and: /etc/nginx/sites-available/domain.conf
def delete_static(domain):
    conf_path = '/etc/nginx/sites-available/{}.conf'.format(domain)
    dir_path = '/html/{}/'.format(domain)
    bOk = os.path.exists(conf_path)
    bOk = bOk and os.path.exists(dir_path)
    if bOk:
        os.unlink(conf_path)
        shutil.rmtree(dir_path)
        return "OK"
    return "ERROR" # this error will show when the file exists
    # ls /etc/nginx/sites-available/
    # ls /etc/nginx/sites-enabled/
