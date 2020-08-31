import pysam
import sys
import time

#use the first item in the command line following the code as the file to process
filename = sys.argv[1]
#specify the output name
out_filename = "clean_" + str(sys.argv[1])
# ambigious = set(['M', 'D', 'R', 'N', 'K', 'Y', 'S', 'B', 'H', '-', 'V', 'W'])
#specify a set of good nucleotides
good = set(["A", "C", "G", "T"])
#use pysam to open the input file and output file at the same time
with pysam.FastxFile(sys.argv[1]) as fh, open(out_filename, mode='w') as fout:
    #loop over each sequence entry in the fastq file 
    x = 0
    for entry in fh:
        #set a variable for a bad nucleotide equal to false
        found_a_bad_nuc = False
        # print(entry.name)
        # print(entry.sequence)
        # print(entry.comment)
        # print(entry.quality)
        x += 1
        #check for ambigous bases that are not A, T, C or G
        #by looping over every nucleotide within the sequence of the fastq file
        for nuc in entry.sequence:
            #check if the nucleotide in uppercase matches the good set listed above
            if nuc.upper() not in good:
                #if there is a nucleotide that isn't in the good list, set our variable to true as a flag
                found_a_bad_nuc = True
                #stop going over this sequence and move to the next sequence
                break

            #if we don't find a bad nucleotide
            else:
                #go to the next step
                pass

        #after going through a sequence, check if we found a bad nucleotide or not
        if found_a_bad_nuc == False:
            #if we didn't find any bad nucleotides, write the entire4 line of fastq data to the output file
            fout.write(str(entry))
            #add a new line at the end of the entry so the following fastq file starts on its own line
            fout.write("\n")
        #if we did find a bad nucleotide, pass and go to the next sequence
        else:
            pass

