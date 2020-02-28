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
