The overall counts for matched, hopped, and unknown data are shown in the following table:

type of data|count|percent of total
------------|-----|---------------
hopped|707740|0.19483726398807136%
matched|331755033|91.33049275721639%
unknown|30783962|8.474669978795541%

This table was compiled from the data found in [overall_data.tsv](https://github.com/perrisn/Demultiplex/blob/7bc834305a128b01a5af2e948477c0ae66f3baaf/Assignment-the-third/overall_data.tsv)

The highest percentage of data was matched data. This was expected because we used dual-matched index pairs, so theoretically they should be the same on each side. The index hopped and unknown barcodes are likely from sequencing errors. 

The data including the number of matches per index and percent of matched indexes (per sample and in total) is included in this file: [matched_data.tsv](https://github.com/perrisn/Demultiplex/blob/a470fd86c8986f2a90453ee6d7e9566bd58dd493/Assignment-the-third/matched_data.tsv)

The data including the number of index hops and percentage (of total) is included in this file: [hopped_data.tsv](https://github.com/perrisn/Demultiplex/blob/a470fd86c8986f2a90453ee6d7e9566bd58dd493/Assignment-the-third/hopped_data.tsv)

Quality score filtering was not included. This is because by filtering for unknowns (both N and not included in our index list) we are inherently doing quality filtering. Reads of low quality would likely have an N as the base was not able to be definitively called. 



