# CHEM283: CAPSTONE
# CREATOR: KOREDE OGUNDELE
# DATE CREATED: APRIL 12, 2024
# LAST MODIFIED: APRIL 16, 2024

import os

# directory with all prediction .txt files
directory = "./fasta_txts/"


def select_positives(filename):
    """"
    This function iterates through files that contain DeepFRI predictions, selects positive predictions (score > 0.5),
    and writes them to a new file.

    Arguments
    ---------
    filename : str
        name of file with predictions

    Returns
    -------
    None.
    """
    protein_name = os.path.splitext(os.path.basename(filename))[0]
    
    if not os.path.exists(filename):
        print(f"File {filename} does not exist. Run DeepFRI on the FASTA to obtain an output file.")
        return

    with open(filename, 'r') as file:
        # skip first line (contains column titles)
        next(file)
        
        for line in file:
            score = float(line.split(",")[2])
            
            if score > 0.5:
                new_filename = f"positives/{protein_name}.txt"

                if not os.path.exists("positives/"):
                    os.makedirs("positives/")
                    
                # You might have the run this script more than once. In that case, you would want
                # to skip files that already exist or you'll write the same predictions multiple times.
                if not os.path.exists(new_filename):
                    with open(new_filename, 'a') as positive_file:
                        positive_file.write(line)
                else:
                    print(f"Positive predictions have already been written for {new_filename}.")
                    

if __name__ == "__main__":
    file_list = os.listdir(directory)

    for file in file_list:
        full_path = os.path.join(directory, file)
        # Printing the full path before running select_positives increases runtime makes debugging significantly easier.
        # Sometimes the loop gets interrupted by a hidden file (such as .DS_Store or a weirdly formatted file)
        print(full_path)
        select_positives(full_path)