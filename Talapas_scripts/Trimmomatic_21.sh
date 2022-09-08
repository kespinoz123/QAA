#!/bin/bash
#SBATCH --account=bgmp         ### SLURM account which will be charged for the job
#SBATCH --job-name=Trimmomatic    ### Job Name
#SBATCH --output=Trimmomatic_%j.out         ### File in which to store job output
#SBATCH --error=Trimmomatic-%j.err          ### File in which to store job error messages
#SBATCH --time=0-24:00:00       ### Wall clock time limit in Days-HH:MM:SS
#SBATCH --nodes=1               ### Node count required for the job
#SBATCH --cpus-per-task=4   ### Number of cpus (cores) per task
#SBATCH --partition=bgmp          ### partition to run things

cd /projects/bgmp/kespinoz/bioinfo/Bi623/FASTQC/cutadapt_files
conda activate QAA

trimmomatic PE 21_3G.f.fastq  21_3G.r.fastq 21_Filtered_1P.fq.gz 21_Filtered_1U.fq.gz 21_Filtered_2P.fq.gz 21_Filtered_2U.fq.gz LEADING:3 TRAILING:3 SLIDINGWINDOW:5:15 MINLEN:35

