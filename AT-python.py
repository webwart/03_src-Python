#!/user/  .in Unix only
print ("Starting AT script")
dna = 'gattatatatt'
no_t=dna.count('t')
no_a=dna.count('a')
dna_lenght=len(dna)
gc_percent=(no_a+no_t)*100.0/dna_lenght
print (gc_percent)
print  ("------ Finished AT script ----------")
