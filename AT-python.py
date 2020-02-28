#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: learn functions for strings.
#      Ref: --
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs 
#       >N: -- 
#  ------------------------------------ 

print ("Starting AT script")
dna = 'gattatatatt'
no_t=dna.count('t')
no_a=dna.count('a')
dna_lenght=len(dna)
gc_percent=(no_a+no_t)*100.0/dna_lenght
print (gc_percent)
print  ("------ Finished AT script ----------")
