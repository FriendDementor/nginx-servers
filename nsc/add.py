import os
import stat
from jinja2 import Template

# this is only one that can create files
# in the /html folder and /etc/nginx/sites-available/

# add
# command to add a new site to the server
#
# example:
# $ nginx add example.com

# this function set the config and files to make
# a new page available to work
# for each execution of this function will create
# two files: /html/domain/index.html
# and: /etc/nginx/sites-available/domain.conf
def add_static(domain):
    conf_path = '/etc/nginx/sites-available/{}.conf'.format(domain)
    dir_path = '/html/{}/'.format(domain)
    bOk = not os.path.exists(conf_path)
    bOk = bOk and not os.path.exists(dir_path)
    if bOk:
        os.mknod(conf_path)
        os.mkdir(dir_path)
        os.mknod(dir_path+'index.html')

        file_r = open('/nsc/templates/domain.conf', 'r')
        template_config = file_r.read()
        file_r.close()
        t = Template(template_config)

        text_file = open(conf_path, "w")
        text_file.write(t.render(domain=domain))
        text_file.close()

        file_r = open('/nsc/templates/index.html', 'r')
        template_html = file_r.read()
        file_r.close()
        t = Template(template_html)

        text_file = open(dir_path+'index.html', "w")
        text_file.write(t.render(domain=domain))
        text_file.close()

        os.chmod(dir_path+'index.html', stat.S_IRGRP | stat.S_IROTH | stat.S_IRUSR)

        return "OK"
    return "ERROR" # this error will show when the file exists
    # ls /etc/nginx/sites-available/
    # ls /etc/nginx/sites-enabled/
