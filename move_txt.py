import os
import shutil

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

    os.makedirs(destination_directory)

    for file in os.listdir(origin_directory):
        # check file ending
        if file.endswith('.txt'):
            # get full file paths
            origin_file = os.path.join(origin_directory, file)
            destination_file = os.path.join(destination_directory, file)
            # move file to destination directory
            shutil.move(origin_file, destination_file)
            print(f"{file} moved to {destination_directory}")

            return

# python move_txt.py /global/homes/k/korede/DeepFRI/fasta_work/individual_fastas /global/homes/k/korede/DeepFRI/fasta_work/fasta_txts