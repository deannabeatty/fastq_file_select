# file_select

This repository contains a python script to select fastq files with a user supplied text file of sample 
identifiers found in the fastq file names. Files are copied to a new directory (keep) and a csv file is 
written with rows for sample identifiers and their forward and reverse read file names, respectively. The output 
csv file and directory (keep) of fastq files are used for uploading fastq files to NCBI.

Language:
Python version 3.10.0 

Package manager:
Miniconda \
Miniconda installation instructions can be found here: https://docs.conda.io/en/latest/miniconda.html

Create a conda environment 

 ```conda create --name $ENVIRONMENT_NAME``` 

Activate your conda environment 

```conda activate $ENVIRONMENT_NAME``` 

Install dependencies (pandas) within your conda environment

```conda install $pandas``` 

See documentation for other conda commands:
https://docs.conda.io/projects/conda/en/latest/commands.html

Instructions before running file_select.py: \
Fill 'fastq_R1' with your forward read fastq files and 'fastq_R2' with your reverse read fastq files. 
In the 'Sample_keep.txt' file add all sample ids which will be used to subset your fastq files.
