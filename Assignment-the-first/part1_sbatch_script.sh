#!/bin/bash

#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=compute               #REQUIRED: which partition to use
#SBATCH --mail-user=perrisn@uoregon.edu     #optional: if you'd like email
#SBATCH --mail-type=ALL                   #optional: must set email first, what type of email you want
#SBATCH --cpus-per-task=4                 #optional: number of cpus, default is 1
#SBATCH --mem=16GB                        #optional: amount of memory, default is 4GB

dir1=/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz
dir2=/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz
dir3=/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz
dir4=/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz

#/usr/bin/time -v /projects/bgmp/perrisn/bioinfo/Bi622/Demultiplex/Assignment-the-first/part1_script.py --filename $dir1 -l 101 -o /projects/bgmp/perrisn/bioinfo/Bi622/Demultiplex/Assignment-the-first/read1_file
#/usr/bin/time -v /projects/bgmp/perrisn/bioinfo/Bi622/Demultiplex/Assignment-the-first/part1_script.py --filename $dir2 -l 8 -o /projects/bgmp/perrisn/bioinfo/Bi622/Demultiplex/Assignment-the-first/index1_file
#/usr/bin/time -v /projects/bgmp/perrisn/bioinfo/Bi622/Demultiplex/Assignment-the-first/part1_script.py --filename $dir3 -l 8 -o /projects/bgmp/perrisn/bioinfo/Bi622/Demultiplex/Assignment-the-first/index2_file
/usr/bin/time -v /projects/bgmp/perrisn/bioinfo/Bi622/Demultiplex/Assignment-the-first/part1_script.py --filename $dir4 -l 101 -o /projects/bgmp/perrisn/bioinfo/Bi622/Demultiplex/Assignment-the-first/read2_file