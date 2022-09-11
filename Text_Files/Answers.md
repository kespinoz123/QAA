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

# Part 2 – Adaptor trimming comparison

Create a new conda environment called QAA and install cutadapt and Trimmomatic. Google around if you need a refresher on how to create conda environments. Recommend doing this in an interactive session, not the login node! Make sure you check your installations with:

* cutadapt --version (should be 4.1)
* trimmomatic -version (should be 0.39)
Using cutadapt, properly trim adapter sequences from your assigned files. Be sure to read how to use cutadapt. Use default settings. 


# Try to determine what the adapters are on your own. If you cannot (or if you do, and want to confirm), click here to see the actual adapter sequences used.Sanity check: Use your Unix skills to search for the adapter sequences in your datasets and confirm the expected sequence orientations. 

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

==================== Command used Command ====================
 $ ./QAA_ParsingSAM.py -f aligned_34_Mus_musculus.GRCm39.dnaAligned.out.sam 

>>>>>>>>>>>>>>

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

-------- Below is supporting information on how I was able to answer this question --------
* ******** Example of commands run for each file (repeated for all 4): FWD and RVS * ******** 
$ cat 21_3G_htseq_Forward_strand.txt | grep -v "^_" | awk '{sum+=$2} END {print sum}
$ cat 21_3G_htseq_reverse_strand.txt | grep -v "^_" | awk '{sum+=$2} END {print sum}'

* ******** Example of commands run for each file (repeated for all 4): Total Reads * ******** 
$ cat 21_3G_htseq_Forward_strand.txt | awk '{sum+=$2} END {print sum}'
$ cat 34_4H_htseq_Forward_strand.txt | awk '{sum+=$2} END {print sum}'

>>>>>>>>>>>>>>

