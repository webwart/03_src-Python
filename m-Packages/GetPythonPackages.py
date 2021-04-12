#!/user/  .in Unix only
# -*- coding: utf-8 -*-

#  ------------------------------------
#  Porject: LEARN - usage of pip module on command line, but some rare cases within program
#   Author: Rainer Warth
#  Version: 10-14-201 Previous: -- First: --
#    Goals: Understand creation, development and packaging with typical python tools
#      Ref: https://pip.pypa.io/en/stable/quickstart/   on  CLI
#      Ref: https://pip.pypa.io/en/stable/user_guide/#using-pip-from-your-program  usage from a programm
#    Satus: broken (link, module, file is missing)> - <bug (false output , script does not run)> - <runs> -  
#    Satus: Using PIP from within a script is not recommandet.
#       >N: Explore better tools.


# Reference: https://pip.pypa.io/en/stable/user_guide/#using-pip-from-your-program
# Author: Rainer Warth
# Description: - Lists all installed packages and prints them out. - prints help file
#              - shows path to package file.
# NOTE: This script does not 

import subprocess
import pip
# installed_packages = pip.get_installed_distributions()
# installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
#      for i in installed_packages])
reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
# for package in installed_packages_list:
#    print(package)
print(reqs)
# print(installed_packages_list)

# The help command gives me also a list of modules
print ("\n <<<<-----Demo of help() command ----------->>>>\n")
help("julia")
print ("\n <<<<-----Demo of help() command ----------->>>>\n")
help("biopython")
print ("\n <<<<-----Demo of help() command ----------->>>>\n")
help("selenium")
