import os

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


# run the function. idk how to do it from terminal
if __name__ == "__main__":
    # remember to modify file path
    directory_path = "/global/homes/k/korede/DeepFRI/fasta_work/individual_fastas"
    file_count = count_files_in_directory(directory_path)