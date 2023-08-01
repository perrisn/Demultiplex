# Assignment the First

## Part 1
1. Be sure to upload your Python script. Provide a link to it here:

| File name | label | Read length | Phred encoding |
|---|---|---|---|
| 1294_S1_L008_R1_001.fastq.gz | read1 | 101 | Phred+33 |
| 1294_S1_L008_R2_001.fastq.gz | index1 | 8 | Phred+33 |
| 1294_S1_L008_R3_001.fastq.gz | index2 | 8 | Phred+33 |
| 1294_S1_L008_R4_001.fastq.gz | read2 | 101 | Phred+33 |

2. Per-base NT distribution
    1. Use markdown to insert your 4 histograms here.
    ![Read 1 Histogram](/projects/bgmp/perrisn/bioinfo/Bi622/Demultiplex/Assignment-the-first/read1_file.png)
    ![Index 1 Histogram](/projects/bgmp/perrisn/bioinfo/Bi622/Demultiplex/Assignment-the-first/index1_file.png)
    ![Index 2 Histogram](/projects/bgmp/perrisn/bioinfo/Bi622/Demultiplex/Assignment-the-first/index2_file.png)
    ![Read 2 Histogram](/projects/bgmp/perrisn/bioinfo/Bi622/Demultiplex/Assignment-the-first/read2_file.png)
    2. **A good quality score cut off for index reads would be 35. This was determined based off of the mean quality score distribution. The lowest score based on the distribution seemed to be around 30. However, because indexes have such short sequences they can be nmore influenced by outliers. Therefore I would set the cutoff to be a little higher than the lowest value we observed. A good quality score cutoff for the read files would be 30. This was determined based off of the mean quality score distribution. In this case, the sequences are not as influcenced by outliers as the index reads. Perhaps a high enough coverage could overcome a large error rate as well. **
    3. **I determined there was 3976613 indexes in Index 1 that had undetermined base calls. I determined there was 3328051 indexes in Index 2 that had undetermined base calls.**
    
## Part 2
1. Define the problem
'''
We have a number of samples which are either matched to our index library, have indexes that have undergone "index-hopping", or are unknown. We need to separate these reads using the indexes provided in R2 and R3. 
'''
2. Describe output
'''
Our ouptut should have separate files for each matched index read, a file for reads that underwent index hopping for each read, and a file for unknown indexes for each read. Further information about output can be found in pseudo_code_output.txt found in this repo. 
'''
3. Upload your [4 input FASTQ files](../TEST-input_FASTQ) and your [>=6 expected output FASTQ files](../TEST-output_FASTQ).
4. Pseudocode
5. High level functions. For each function, be sure to include:
    1. Description/doc string
    2. Function headers (name and parameters)
    3. Test examples for individual functions
    4. Return statement
