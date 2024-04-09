# Work for Pivotal Life Sciences
## January - May 2024

During my internship at Pivotal Life Sciences, I worked on enhancing DeepFRI, a deep learning model that combines long short-term memory (LSTM) networks with graph convolutional networks (GCN) to predict protein functions. My role involved data cleaning, feature selection, and in-depth analysis using Python libraries like TensorFlow and Biopython. Ultimately, I modified DeepFRI and develop complementary functions that increased its utility for Pivotal Life Sciences' investment team. At the end of my internship, I presented my findings to both UC Berkeley faculty and peers, as well as the Pivotal Life Sciences team. 

Files included in this repository are:
- bio_python exploration.ipynb : this notebook introduces the SeqIO function from the Biopython package and demonstrates simple function uses. The function used in extract_fasta.py can also be found here.
- count_files.py : this script contains a script that counts the number of files in a directory. I use this to make sure that all (80k+) protein fasta files are present, all txt files have been moved, etc. Remember to modify directory path before use.
- move_txt.py : this script moves all .txt files from one directory (origin) to another (destination).
- nacht.fasta : fasta sequences for NACHT.
- output.fasta : fasta sequence for one isoform of NACHT, filtered from nacht.fasta.
- uniprot_go_ec.ipynb : this notebook accesses UniProt's API
- uniprotkb_proteome_human.fasta : the fasta file downloaded from UniProtKB, which contains all fasta sequences (canonical and isoform) of human proteins. Not pushed to this repo due to size.
- biopython-fasta-work/individual_fastas/ : this directory contains individually parsed fasta files for human proteins. It was not pushed to this repo, but uploaded to Perlmutter (the supercomputer used for this project) instead. Not pushed to this repo due to size.
