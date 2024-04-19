# CHEM283: CAPSTONE
# CREATOR: KOREDE OGUNDELE
# DATE CREATED: APRIL 8, 2024
# LAST MODIFIED: APRIL 19, 2024

import os
import shutil

# modify to fit your desird origin and destination directories
origin_filepath = "/global/homes/k/korede/DeepFRI/fasta_work/individual_fastas"
destination_filepath = "/global/homes/k/korede/DeepFRI/fasta_work/fasta_txts"

def move_txt_files(origin_directory, destination_directory):
    """
    This function takes all txt files from one directory (origin), makes a new directory (destination) and moves them all there.

    Arguments
    ---------
    origin_directory : str
        directory files are currently in
    target_directory : str
        directory files will be moved to

    Returns
    -------
    None.
    """
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
        
    file_list = os.listdir(origin_directory)

    for file in file_list:
        if file.endswith('.txt'):
            origin_file = os.path.join(origin_directory, file)
            destination_file = os.path.join(destination_directory, file)

            shutil.move(origin_file, destination_file)
            print(f"{file} moved to {destination_directory}")

if __name__ == "__main__":
    move_txt_files(origin_filepath, destination_filepath)
