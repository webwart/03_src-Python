#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020 Previous: 05.04.2016 First: 05.04.2016
#    Goals: Create test data 
#      Ref: https://pathlib.readthedocs.org/en/pep428/
#      Ref: https://docs.python.org/3/library/pathlib.html?highlight=pathlib#module-pathlib
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: broken
#       >N: --


# fobj_in = open("150916_Lines.txt")
fobj_out = open("150917_Lines.txt","w")
i = 1
for i in range(1000):
 #   print(line.rstrip())
    fobj_out.write('<tr>\n')
    fobj_out.write('   <td>Biobank '+ str(i)+ '</td>\n')
    fobj_out.write('   <td>Bern, Switzerland</td>\n')
    fobj_out.write('   <td><a title="Tumorbank Bern" href="http://www.tumorbank.unibe.ch/"><strong>Link</strong></a></td>\n')
    fobj_out.write('   <td></td>\n')
    fobj_out.write('</tr>\n')
    #i = i + 11
#fobj_in.close()
fobj_out.close()
