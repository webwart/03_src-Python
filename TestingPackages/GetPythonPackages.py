#!/user/  .in Unix only
# Reference: unknown
# Author: Rainer Warth
# Description: - Lists all installed packages and prints them out. - prints help file
#              - shows path to package file.

import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])

for package in installed_packages_list:
    print(package)

# print(installed_packages_list)

# The help command gives me also a list of modules
print ("\n <<<<-----Demo of help() command ----------->>>>\n")
help("julia")
print ("\n <<<<-----Demo of help() command ----------->>>>\n")
help("biopython")
print ("\n <<<<-----Demo of help() command ----------->>>>\n")
help("selenium")
