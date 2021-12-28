# This python script takes a user supplied text file of sample identifiers found in 
# fastq file names and saves these identifiers to a list; use this list to find and copy relevant fastq files to a user specified directory
# a csv file is written that contains rows for sample identifiers and their forward and reverse read filepaths, respectively

# activate conda environment
# terminal:
# conda activate 'env_name'
# VS code:
# View -> command palatte –> Python: Select Interpreter to locate your conda env

# import packages
from os import write
from pathlib import Path
from shutil import copy2
from pandas import DataFrame
from csv import writer

# open sample_keep file to get list of sample identifiers to keep
keep = []
with open('Sample_keep.txt', 'r') as keep_nums:
    keep = keep_nums.read().splitlines()

# create path variables
fastq_path_R1 = Path('./fastq_R1')
fastq_path_R2 = Path('./fastq_R2')
keep_path = Path('./keep')

# use lists (indexed and ordered) within each for loop for forward (R1) and reverse (R2) reads
cols_R1 = ['SampleID', 'filename_R1']
cols_R2 = ['SampleID', 'filename_R2']
row_R1 = []
row_R2 = []

# Forward reads *R1_001.fastq.gz
# if 0th item of name.split is in keep list, copy file to keep dir
# assign 0th item of name.split to variable SampleID
# assign filepath to FileNameR1 variable
# append each variable to ith row of list 'row_R1'
for filepath in fastq_path_R1.glob('*'):
    if filepath.name.split('_')[0] in keep:
        copy2(filepath, str(keep_path) + f'/{filepath.name}')
        SampleID = filepath.name.split('_')[0]
        FileNameR1 = filepath.name
        row_R1.append([ str(SampleID), str(FileNameR1) ]) 

# create dataframe of SampleId and FileNameR1 from for loop with appended rows       
df1 = DataFrame(row_R1, columns = cols_R1)

# repeat for loop for reverse reads *R2_001.fastq.gz, fastq_path_R2, and list 'row_R2'
for filepath in fastq_path_R2.glob('*'):
    if filepath.name.split('_')[0] in keep:
        copy2(filepath, str(keep_path) + f'/{filepath.name}')
        SampleID = filepath.name.split('_')[0]
        FileNameR2 = filepath.name
        row_R2.append([ str(SampleID), str(FileNameR2) ]) 

# create dataframe of SampleId and FileNameR2 from for loop with appended rows       
df2 = DataFrame(row_R2, columns = cols_R2)

# leftjoin df2 to df1 on common column SampleID
df3 = df1.merge(df2, on=[ "SampleID" ], how='left')

# write csv of df3 (three columns: SampleID, FileNameR1, FileNameR2)
df3.to_csv("SampleID_fastq.csv", header = True, index = False)