#!/usr/bin/env python3

# This script will open and read a GFF file. Good luck!
file_name = 'covid.gff3'

def parseGFF3(file_name):
  with open(file_name, 'r') as file:
      for line in file:
        columns = line.strip().split('\t')
        if len(columns) > 4:
            start_position = int(columns[3])
            end_position = int(columns[4])
            feature_length = end_position - start_position + 1 
            print('\t'.join(columns) + f"\tFeature Length: {feature_length}")
        else:
            print('\t'.join(columns))

def main():
    gff_file_name = input("Hey my friend enter the ggf file name: ")
    fasta_file_name = input("Hey my friend enter the Fasta file name: ")

    parseGFF3(gff_file_name)
    print(f"Received FASTA file: {fasta_file_name} (processing not implemented)")


if __name__ == "__main__":
    main() 
