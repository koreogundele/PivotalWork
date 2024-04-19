# CHEM283: CAPSTONE
# CREATOR: KOREDE OGUNDELE
# DATE CREATED: MARCH 4, 2024
# LAST MODIFIED: APRIL 19, 2024

import os
from Bio import SeqIO

# file path for FASTA file with all sequences.
input_filename = "uniprotkb_proteome_human.fasta"


def filter_sequences(input_filename, desired_proteins):
    """
    This function iterates through a list (or set) of proteins, write FASTA sequences
    for each protein (selected from a file) to individual files.

    Arguments
    ---------
    input_filename : str
        name of the input FASTA file.
    desired_proteins : list or set
        list of proteins to keep and write to output file

    Returns
    -------
    *.fasta : fasta file
        fasta file containing sequences for the desired proteins. Each file will bear the name of the corresponding protein.
    """
    instances = []
    
    output_filename = f"individual_fastas/{desired_proteins}"
    
    if os.path.exists(output_filename):
        print(f"Output file '{output_filename}' already exists. Skipping '{desired_proteins}'")
        return

    for record in SeqIO.parse(input_filename, "fasta"):
        if desired_proteins == record.name.split("|")[2]:
            instances.append(record)
    
    with open(output_filename, "w") as output_file:
        SeqIO.write(instances, output_file, "fasta")
        print(f"Generated new fasta file for {desired_proteins}")
        
    return


if __name__ == "__main__":
    protein_set = set()
    # remember to change 'input_filename' variable
    for protein in SeqIO.parse(input_filename, "fasta"):
        protein_set.add(protein.name.split("|")[2])

    for protein in protein_set:
        protein_to_select = protein
        filter_sequences(input_filename, protein_to_select)
