# CHEM283: CAPSTONE
# CREATOR: KOREDE OGUNDELE
# DATE CREATED: APRIL 8, 2024
# LAST MODIFIED: APRIL 19, 2024

import os

# remember to modify directory_path
directory_path = "/global/homes/k/korede/DeepFRI/fasta_work/fasta_txts"

def count_files_in_directory(directory):
    """
    This function counts the number of files in a directory.

    Arguments
    ---------
    directory : str
        path to the directory

    Returns
    -------
    count : int
        number of files in the directory.
    """
    files = os.listdir(directory)
    count = len(files)
    print(count)
    
    return


if __name__ == "__main__":
    file_count = count_files_in_directory(directory_path)
