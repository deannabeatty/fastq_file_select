# file_select

This repository contains a python script to select fastq files with a user supplied text file of sample 
identifiers found in the fastq file names. Files are moved to a new directory called 'keep' and a csv file is 
written with rows for sample identifiers and their forward and reverse read filepaths, respectively. The output 
csv file and directory of fastq files can be used uploading fastq files to NCBI.

Language:
Python version 3.10.0 

Package manager:
Miniconda, installation instructions can be found here: https://docs.conda.io/en/latest/miniconda.html

Create a conda environment with: 'conda create --name $ENVIRONMENT_NAME'
Activate your conda environment with: 'conda activate $ENVIRONMENT_NAME'
Install dependencies (pandas) for using file_select.py within your conda environment:
'conda install $pandas'
See documentation for other commands:
https://docs.conda.io/projects/conda/en/latest/commands.html

Instructions before running file_select.py:
create a directory that contains fastq files within subdirectories 
'fastq_path_R1' (forward reads) or 'fastq_path_R2' (reverse reads), an empty subdirectory called
'keep', and a tab deliminated text file of sample identifiers found in the fastq file names.
