#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: Learn to use join-function
#      Ref: --
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs
#       >N: --
#  ------------------------------------ 


# DNA algorithem
seqs = ['A','C','G','T']
print(seqs)
print(''.join(seqs))
print(";".join(seqs))  
seqs.append('U')
print(seqs)
