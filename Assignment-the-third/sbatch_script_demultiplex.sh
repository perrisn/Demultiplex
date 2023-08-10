#!/bin/bash

#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=compute               #REQUIRED: which partition to use
#SBATCH --mail-user=perrisn@uoregon.edu     #optional: if you'd like email
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email you want
#SBATCH --cpus-per-task=1                 #optional: number of cpus, default is 1
#SBATCH --mem=8GB                        #optional: amount of memory, default is 4GB
conda activate base

/usr/bin/time -v ./demultiplex_script.py -i /projects/bgmp/shared/2017_sequencing/indexes.txt \
    -f1 /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz \
    -f2 /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz \
    -f3 /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz \
    -f4 /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz 