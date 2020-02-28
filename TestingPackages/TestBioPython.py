# Name: TestBioPyhton.py
# Reference: biopython Tutorial http://biopython.org/DIST/docs/tutorial/Tutorial.html#htoc6
# Date: 23.12.2015
# Author: Rainer Warth
# Purpose: Learning and testing of biopython
# Related to: none
# Status: Installed biopython with the winpyhton package manager. Installation was succesful
# Next: Work the examples

print('Hello BioPython')
import Bio
print(Bio.__version__)
from Bio.Seq import Seq
my_seq = Seq("AGTACACTGGT")
my_seq
print(my_seq)
my_seq.alphabet
# >N: 2.4 Parsing sequence file formats
