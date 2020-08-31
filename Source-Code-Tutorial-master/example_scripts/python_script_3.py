#load the operating system package, os
import os
#use the os.system function to call a perl script from the command line
os.system("./compare_files.sh example_bad_file.fastq Filtered_example_bad_file.fastq")

