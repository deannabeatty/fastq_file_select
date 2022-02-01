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


# subset_fastq_files function
def subset_fastq_files(fastq_source_dir, fastq_keep_dir, sample_id_keep_list, fastq_subset_file_list):
    '''
    Function to subset source directory of fastq files based on user provided valid sample IDs.

    Sample IDs provided in 'sample_id_keep_list' will be used to select fastq files using the following criteria:
        * First item (before '_') in fastq file name == 'sample_id'
    
    Example:
        - Files in fastq_source_dir:
            '1_S1_L001_R1_001.fastq',
            '2_S13_L001_R1_001.fastq',
            '5_S49_L001_R1_001.fastq'

        - sample_id_keep_list: [ 1, 5 ]

        - fastq_subset_file_list: [
            [ '1', '1_S1_L001_R1_001.fastq'  ],
            [ '5', '5_S49_L001_R1_001.fastq' ]
        ]
    
        - New directory containing selected files will be create at 'fastq_keep_dir':
            '1_S1_L001_R1_001.fastq',
            '5_S49_L001_R1_001.fastq'

    Parameters 
    ----------
    fastq_source_dir: Directory containing fastq files (forward or reverse).

    fastq_keep_dir: Copy fastq files to this path if they meet 'keep' criteria.

    sample_id_keep_list: List of user provided sample ids to define 'keep' criteria.

    fastq_subset_file_list: For files that meet 'keep' criteria, append sample id and file name to this list.
    '''

    for file in fastq_source_dir.glob('*'):
        if file.name.split('_')[0] in sample_id_keep_list:
            copy2(file, str(fastq_keep_dir) + f'/{file.name}')
            SampleID = file.name.split('_')[0]
            file_name = file.name
            fastq_subset_file_list.append([ str(SampleID), str(file_name) ])

# main
def main():
    # open sample_keep file to get list of sample identifiers to keep
    keep_sample_ids = []
    with open('Sample_keep.txt', 'r') as keep_nums:
        keep_sample_ids = keep_nums.read().splitlines()

    # create path variables
    fastq_path_R1 = Path('./fastq_R1')
    fastq_path_R2 = Path('./fastq_R2')
    keep_path = Path('./keep')

    # use lists (indexed and ordered) within each for loop for forward (R1) and reverse (R2) reads

    # Create fastq subset for forward reads (R1). Create a dataframe from this subset.
    R1_list = [] # Create empty list for forward reads to be kept. Rows will be appended for forward reads that match 'keep' criteria.
    R1_cols = ['SampleID', 'filename'] # Define column headers
    subset_fastq_files(fastq_path_R1, keep_path, keep_sample_ids, R1_list)       
    df_forward_read_subset = DataFrame(R1_list, columns = R1_cols)

    # Create fastq subset for reverse reads (R2). Create a dataframe from this subset.
    R2_list = [] # Create empty list for reverse reads to be kept. Rows will be appended for reverse reads that match 'keep' criteria.
    R2_cols = ['SampleID', 'filename2'] # Define column headers
    subset_fastq_files(fastq_path_R2, keep_path, keep_sample_ids, R2_list)       
    df_reverse_read_subset = DataFrame(R2_list, columns = R2_cols)

    # Leftjoin forward & reverse read subset dataframes on common column SampleID
    df_output_csv = df_forward_read_subset.merge(df_reverse_read_subset, on=[ "SampleID" ], how='left')

    # write csv of df_output_csv (three columns: SampleID, FileNameR1, FileNameR2)
    df_output_csv.to_csv("SampleID_fastq.csv", header = True, index = False)

# Main entrypoint
if __name__ == '__main__':
    main()
