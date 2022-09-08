Author: Itzel Espinoza :)

>>>>>>>>>>>>>>
Answers are given inside these "greater symbols"
>>>>>>>>>>>>>>

# RNA-seq Quality Assessment Assignment - Bi 622 (Summer 2022)

# Be sure to upload all relevant materials by the deadline and double check to be sure that your off-line repository is up-to-date with your on-line repository. Answers to the questions should be submitted in your final report as a pdf.

* Objectives
The objectives of this assignment are to use existing tools for quality assessment and adaptor trimming, compare the quality assessments to those from your own software, and to demonstrate your ability to summarize other important information about this RNA-Seq data set.

* Data:
Each of you will be working with 2 of the demultiplexed file pairs. For all steps below, process the two libraries separately. Library assignments are here: /projects/bgmp/shared/Bi622/QAA_data_assignments.txt

The demultiplexed, gzipped .fastq files are here: /projects/bgmp/shared/2017_sequencing/demultiplexed/

Do not move, copy, or unzip these data!
______                    _                                                               
|  _  \                  | |                                                              
| | | |___    _ __   ___ | |_   _ __ ___   _____   _____      ___ ___  _ __  _   _        
| | | / _ \  | '_ \ / _ \| __| | '_ ` _ \ / _ \ \ / / _ \    / __/ _ \| '_ \| | | |       
| |/ / (_) | | | | | (_) | |_  | | | | | | (_) \ V /  __/_  | (_| (_) | |_) | |_| |_      
|___/ \___/  |_| |_|\___/ \__| |_| |_| |_|\___/ \_/ \___( )  \___\___/| .__/ \__, ( )     
                                                        |/            | |     __/ |/      
                                                                      |_|    |___/        
                              _         _   _                          _       _        _ 
                             (_)       | | | |                        | |     | |      | |
  ___  _ __   _   _ _ __  _____ _ __   | |_| |__   ___  ___  ___    __| | __ _| |_ __ _| |
 / _ \| '__| | | | | '_ \|_  / | '_ \  | __| '_ \ / _ \/ __|/ _ \  / _` |/ _` | __/ _` | |
| (_) | |    | |_| | | | |/ /| | |_) | | |_| | | |  __/\__ \  __/ | (_| | (_| | || (_| |_|
 \___/|_|     \__,_|_| |_/___|_| .__/   \__|_| |_|\___||___/\___|  \__,_|\__,_|\__\__,_(_)
                               | |                                                        
                               |_|                                                        
Do not move, copy, or unzip these data!

# Part 1 – Read quality score distributions
Q: Using FastQC via the command line on Talapas, produce plots of quality score distributions for R1 and R2 reads. Also, produce plots of the per-base N content, and comment on whether or not they are consistent with the quality score plots.

>>>>>>>>>>>>>>
----- Figures to Refer to: Folder in "Origninal FASTQC 21_3G Plots" ----- 
Fig.1 21_3G Forward R1 
fig 2. 21_3G Forward R1 N base
fig 3. 21_3G Reverse R2 
fig 4. 21_3G Reverse R2 N base

Figure 1 demonstrates an a high mean quality score scorss all base positions. All quality scores are at least greater than a value of 30. As expected, the quality scores values are lower at the begining (lowest QS of 32 from bp 0-4) of the sequence as well as at the end (QS of 30 from bp 98-101). The quality of reads degrade overtime, so it is normal to see a drop in quality scores at the end of the read. The per N base content plot for this plot does match the overall high quality score trend seend in figure 1. As expected, a small peak appears between basepair 0-1, but remains at a value of zero for the remaining of the sequence. Sequencers input an N base when not being able to recal a base with high confidence, therefore an overall trend of N values being zero means good quality data. The per N base plots matches what is seen in the per base seuqnece plot as the higher the quality score, the better the base call.  

Now for figure 3, I can observe an overall slightly lower quality score mean across all base reads. Unlike the forward fastq file, I can observe more of the yellow whisker plot boxes (indicate inter quartile) and wider ranges (lower-10% and upper quartile-90%). These differences indicate that there is higher variability of quality scores across base reads in the reverse fastq file compared to the forward fastq file. 


 This trend is also seen with the second demultiplexed file of 34_4H forward and reverse (Refer to figures 5-8). It is also important to note that unlike figure 3, figure 7 shows higher variability with more yellow whisker plots. 

 ----- Figures to Refer to: Folder in "Origninal FASTQC 34_4H Plots" ----- 
Fig.5 34_4H Forward R1 
fig 6. 34_4H Forward R1 N base
fig 7. 34_4H Reverse R2 
fig 8. 34_4H Reverse R2 N base

>>>>>>>>>>>>>>


Q: Run your quality score plotting script from your Demultiplexing assignment. (Make sure you're using the "running sum" strategy!!) Describe how the FastQC quality score distribution plots compare to your own. If different, propose an explanation. Also, does the runtime differ? If so, why? Comment on the overall data quality of your two libraries.

>>>>>>>>>>>>>>              

Overall, the plots generated in my demultiplexed script showed a similar mean quality score as seen in fastqc. It is important to note that in my demultiplexed script I decided to give it a quality score of 30. However, the fastqc software must have a different quality score threshold since the lowest quality score I observe was 25 for the reverse 34_4H.fastq.gz. and 22 for reverse 21_3G.fastq.gz. Fastqc also outputs more information compared to my manual script (super cool!) by proving information rergarding the upper and lower quartiles of quality scores for each base read. This information provides further insight as to how the quality scores varies per base (as seen in both reverse fastq.gz files for 21_3G and 34-4H). Fastqc also runs at a much faster speed by generating all the plots in less than 2 minutes and has already included warning and failure thresholds. According to its documentation, I found that a warning will be given if the lower wquartile of a base is less than a quality score value of 10. As well, is any position has an N value higher than 5% and an error message if the N value is higher than 20%. 

Online Documentation for fastqc: https://dnacore.missouri.edu/PDF/FastQC_Manual.pdf

>>>>>>>>>>>>>>

# Part 2 – Adaptor trimming comparison

Create a new conda environment called QAA and install cutadapt and Trimmomatic. Google around if you need a refresher on how to create conda environments. Recommend doing this in an interactive session, not the login node! Make sure you check your installations with:

* cutadapt --version (should be 4.1)
* trimmomatic -version (should be 0.39)
Using cutadapt, properly trim adapter sequences from your assigned files. Be sure to read how to use cutadapt. Use default settings. 

Q: What proportion of reads (both R1 and R2) were trimmed?

>>>>>>>>>>>>>>
For 21_3G.fastq.gz file, the  forward reads had a total of 6.6% of reads trimmed, in comparison to
7.4% trimmed reads in the reverse file (Refer to summary table 1). While for 34_4H.fastq.gz, the forward file had 9.1% of its read trimmed, with 9.8% reads trimmed from the reverse file (Refer to summary table 2). 


================  Summary Table 1: Proportion of Trimmed Reads-21_3G.fastq.gz ================
Total read pairs processed:          9,237,299  
  Read 1 with adapter:                 613,874 (6.6%)  
  Read 2 with adapter:                 679,275 (7.4%)
How they did it: (613874 times/9,237,299)*100 = 6.6%


================  Summary Table 2: Proportion of Trimmed Reads-34_4H.fastq.gz  ====================

Total read pairs processed:          9,040,597
  Read 1 with adapter:                 819,166 (9.1%)
  Read 2 with adapter:                 886,595 (9.8%)

>>>>>>>>>>>>>>

# Try to determine what the adapters are on your own. If you cannot (or if you do, and want to confirm), click here to see the actual adapter sequences used.

# Sanity check: Use your Unix skills to search for the adapter sequences in your datasets and confirm the expected sequence orientations. 

Q: Report the commands you used, the reasoning behind them, and how you confirmed the adapter sequences.

>>>>>>>>>>>>>>

I included the command I used to look up the adaptor sequences in both of my RNA datasets. This command above was used for all files listed below. I first listed the overall format of the command and then defined each segment, as well as listed all the files I analyzed (only paired for time effciency). Using fastqc overrepresented sequences plot, I used that sequence and inserted it for the adapater sequence in my command. Refering to the online resource listed below, I then used this over-represented sequence and used the awk command to search and print the index pattern given in my list of files. Since the adaptor sequence was then provided, I double checked my command by running the known adaptor sequence instead. The output from running this command is a list of where the adaptor sequence starts in the read length (what base the adator first appears in my raw file). 

================== Commands used ================== 
$ zcat <fastq path> |  awk '/adapter sequence/ {print index($0, <adapter sequence> )}' | head -10

* Example of how I used the command for one of my files * 
$ zcat projects/bgmp/shared/2017_sequencing/demultiplexed/21_3G_both_S15_L008_R1_001.fastq.gz |  awk '/AGATCGGAAGAGCACACGTCTGAACTCCAGTCA/ {print index($0, AGATCGGAAGAGCACACGTCTGAACTCCAGTCA )}' | head -10

<Known Adaptor sequences> 
R1: AGATCGGAAGAGCACACGTCTGAACTCCAGTCA
R2: AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT

<fastq path> =  /projects/bgmp/kespinoz/bioinfo/Bi623/FASTQC/trimmed_reads

====== List of Assigned Demultiplexed FASTQ Files (containing adaptors) ====== 
* 21_3G_both_S15_L008_R1_001.fastq.gz   
* 21_3G_both_S15_L008_R2_001.fastq.gz   
* 34_4H_both_S24_L008_R1_001.fastq.gz
* 34_4H_both_S24_L008_R2_001.fastq.gz 

Online Reference: 
https://stackoverflow.com/questions/53180311/using-awk-to-print-index-of-a-pattern-in-a-file


>>>>>>>>>>>>>>

# Use Trimmomatic to quality trim your reads. Specify the following, in this order:

* LEADING: quality of 3
* TRAILING: quality of 3
* SLIDING WINDOW: window size of 5 and required quality of 15
* MINLENGTH: 35 bases
Be sure to output compressed files and clear out any intermediate files.

# Plot the trimmed read length distributions for both R1 and R2 reads (on the same plot). You can produce 2 different plots for your 2 different RNA-seq samples. There are a number of ways you could possibly do this. One useful thing your plot should show, for example, is whether R1s are trimmed more extensively than R2s, or vice versa. 

>>>>>>>>>>>>>>

Plots generated from Excel showing trimmed read length distribution are found in "Distribution Plot Folder". 

Figure 1 shows trimmed read length distribtion of 21_3G.fastq.gz R1 overlayed with R2. Overall, R1 Forward paired file has higher reads with length 99-101 when compared to R1 Reverse Paired file. This further supports that R2 was trimmed at a higher extent than R1, given that difference at read length 99-101 (Refer to figure 1). 

Figure 2 shows trimmed read length distribution of 34_4H.fastq.gz R1 overlayed with R2. Overall, R1 Forward paired file has higher reads with length 99-101 when compared to R1 Reverse Paired file. This further supports that R2 was trimmed at a higher extent than R1, given that difference at read length 99-101 (Refer to figure 1). However, the R1 and R2 for 34_4H.fastq.gz file show a lower trimmed difference between the two when compared to the R1 and R2 file from 21_3G.fastq.gz. 
This is also supported as R2 was trimmed 0.8% more than R1 in 21_3G.fastq.gz (Summary Table 1). While R2 was trimmed 0.7% more than R1 in 34_4H.fastq.gz (Summary table 2). 

>>>>>>>>>>>>>>
Q: Comment on whether you expect R1s and R2s to be adapter-trimmed at different rates.

 ----- Figures to Refer to: Folder in "Trimmed FASTQC 21_3G Plots" ----- 
Fig.17 21_3G Forward R1 
fig.18 21_3G  Forward R1 N base
fig.19 21_3G  Reverse R2 
fig.20 21_3G  Reverse R2 N base

 ----- Figures to Refer to: Folder in "Trimmed FASTQC 34_4H Plots" ----- 
Fig.21 34_4H Forward R1 
Fig.22 34_4H Forward R1 N Base
Fig.23 34_4H Reverse R1 
Fig.24 34_4H Reverse R1 N base

>>>>>>>>>>>>>>

R1s and R2s should be trimemd at different rates. When running fastqc on the raw reads, the R2 file showed lower quality scores scross base reads than the forward or R1 file. For this reason, cuatadpt and trimmomatic will remove more of those flagged poor quality reads from the R2 file than the R1 file. This is supportd by the proportions of trimmed reads reported in summary table 1 and summary table 2. For example in 21_3G.fastq.gz, the R1 file had a 6.6% trimmed value while R2 had a 7.4% trimmed value, with a difference of 0.8% (Figs. 9-12). For 34_4H.fastq.gz, the R1 file had a trimmed value of 9.1%, compared to 98% for R2, with a difference of 0.7% (Figs. 13-16). As observed in fastqc raw files, the 43_4H.fastq.gz showed lower quality values and higher variability, which is why it has a higher trimmed percentage when compared to 21_3G.fastq.gz.  

>>>>>>>>>>>>>>

# Part 3 – Alignment and strand-specificity
Install sofware. In your QAA environment, use conda to install:

* star
* numpy
* pysam
* matplotlib
* htseq

# Find publicly available mouse genome fasta files (Ensemble release 107) and generate an alignment database from them. Align the reads to your mouse genomic database using a splice-aware aligner. Use the settings specified in PS8 from Bi621.

Hint - you will need to use gene models to perform splice-aware alignment, see PS8 from Bi621.

Using your script from PS8 in Bi621, report the number of mapped and unmapped reads from each of your 2 sam files. Make sure that your script is looking at the bitwise flag to determine if reads are primary or secondary mapping (update/fix your script if necessary).

>>>>>>>>>>>>>>

The number of mapped, unmapped and total number of reads for each sam file from 21_3G.fastq.gz and 34_4H.fastq.gz are reported in summary table 3. File aligned_21_Mus_musculus.GRCm39.dnaAligned.out.sam had a 17061173 number of reads mapped from 18586906 reads total, 91.8%. While aligned_34_Mus_musculus.GRCm39.dnaAligned.out.sam had 16822704 number of reads mapped from 18158914 reads total, 92.6%. 


==================== Command used Command ====================
 $ ./QAA_ParsingSAM.py -f aligned_34_Mus_musculus.GRCm39.dnaAligned.out.sam 

====================  Summary Table 3: Mapped vs Unmapped Reads ====================
   1.  aligned_21_Mus_musculus.GRCm39.dnaAligned.out.sam 
        Number mapped:  17061173
        Number unmapped:  645451
        Number of reads:  18586906

   2.  aligned_34_Mus_musculus.GRCm39.dnaAligned.out.sam 
        Number mapped:  16822704
        Number unmapped:  483578
        Number of reads:  18158914


# Count reads that map to features using htseq-count. You should run htseq-count twice: once with --stranded=yes and again with --stranded=reverse. Use default parameters otherwise. 

-------- Below is supporting information on how I was able to use hseq-count --------
>>>>>>>> Commands used for when running hseq for all 4 files:
$ htseq-count --format sam --stranded=yes  aligned_21_Mus_musculus.GRCm39.dnaAligned.out.sam Mus_musculus.GRCm39.107.gtf > 21_3G_htseq_Forward_strand.txt

$ htseq-count --format sam --stranded=reverse  aligned_21_Mus_musculus.GRCm39.dnaAligned.out.sam /Mus_musculus.GRCm39.107.gtf > 21_3G_htseq_reverse_strand.txt

Example of output Files (4 in total)
  1. 21_3G_htseq_Forward_strand.txt
  2. 21_3G_htseq_reverse_strand.txt

>>>>>>>> 


# Demonstrate convincingly whether or not the data are from “strand-specific” RNA-Seq libraries. Include any comands/scripts used. Briefly describe your evidence, using quantitative statements (e.g. "I propose that these data are/are not strand-specific, because X% of the reads are y, as opposed to z."). Hint - recall ICA4 from Bi621.

>>>>>>>>>>>>>>

I know that my data is stranded specific because more than half of my sequences are reading in one direction and the other half reads in the other direction. Using the information reported below, for 21_3G.fastq.gz, 3.8% were mapped in the forward direction and 81.2% in the reverse direction. For 34_4H.fastq.gz, 5.6% were mapped in the forward direction while 83.4% in the reverse direction. These reported values support the idea that more than 50% of reads for a given value are being read in one direction over the other, thus indicating stranded specific RNA libraries. 

>>>>>>>>>>>>>>

-------- Below is supporting information on how I was able to answer this question --------
* ******** Example of commands run for each file (repeated for all 4): FWD and RVS * ******** 
$ cat 21_3G_htseq_Forward_strand.txt | grep -v "^_" | awk '{sum+=$2} END {print sum}
$ cat 21_3G_htseq_reverse_strand.txt | grep -v "^_" | awk '{sum+=$2} END {print sum}'

* ******** Example of commands run for each file (repeated for all 4): Total Reads * ******** 
$ cat 21_3G_htseq_Forward_strand.txt | awk '{sum+=$2} END {print sum}'
$ cat 34_4H_htseq_Forward_strand.txt | awk '{sum+=$2} END {print sum}'

====================  Summary Table 4: Strand Specific RNA Libraries ====================
-- Reads in FWD and RVS --         -- Percent of reads mapped -- 
    Sum 21 forward: 340380          (340380/8853312)*100 = 3.8%
    sum 21 reverse: 7181307         (7181307/8853312)*100 = 81.2%

    Sum 34 forward: 482525          (482525/8653141)*100 = 5.6%
    sum 34 reverse: 7214830         (7214830/8653141)*100 = 83.4%

-----  Total Number of reads----- 
    21_3G.fastq.gz: 8853312
    34_4H.fastq.gz: 8653141





