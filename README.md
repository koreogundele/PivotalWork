# Work for Pivotal Life Sciences
## January - May 2024


### NOTE::Much of the code I wrote for this project has been left out due to being covered by a non-disclosure agreement
During my internship at Pivotal Life Sciences, I worked on enhancing DeepFRI, a deep learning model that combines long short-term memory (LSTM) networks with graph convolutional networks (GCN) to predict protein functions. My role involved data cleaning, feature selection, and in-depth analysis using Python libraries like TensorFlow and Biopython. Ultimately, I modified DeepFRI and develop complementary functions that increased its utility for Pivotal Life Sciences' investment team. At the end of my internship, I presented my findings to both UC Berkeley faculty and peers, as well as the Pivotal Life Sciences team. 

Files included in this repository are:
- count_files.py : this script contains a function that counts the number of files in a directory. I use this to make sure that all (80k+) protein FASTA files are present, all txt files have been moved, etc. Remember to modify directory path before use.
- extract_fasta.py: this script contains a function that extracts the FASTA sequences of the desired protein(s) and writes them to separate output files for each protein.
- move_txt.py : this script moves all .txt files from one directory (origin) to another (destination).
- select_DeepFRI_positives.py : this script contains a function that iterates thorugh saved DeepFRI predictions and creates a new folder that contains only positive predictions (DeepFRI score >0.5)
