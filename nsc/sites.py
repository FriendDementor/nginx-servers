import os

# sites
# command to show a list of sites available and then sites enabled
#
# example:
# $ nginx sites
# sites available
# example.com
# foo.com
#
# sites enabled
# example.com
def sites():
    result_lines = []
    result_lines.append("sites available:")
    available_files = os.listdir("/etc/nginx/sites-available/")
    result_lines += [x[:-5] for x in sorted(available_files)]
    result_lines.append("")
    result_lines.append("sites enabled:")
    enabled_files = os.listdir("/etc/nginx/sites-enabled/")
    result_lines += [x[:-5] for x in sorted(enabled_files)]
    result_lines.append("")
    result_lines.append("")

    return '\n'.join(result_lines)
    # ls /etc/nginx/sites-available/
    # ls /etc/nginx/sites-enabled/