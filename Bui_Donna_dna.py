# Trees and Dictionaries: Part 2 (Dictionaries/DNA Sequences) - Donna Bui - 3/25/2023 - Professor Henry Estrada's COMSC 078
# This program will prompt the user to input a valid DNA sequence and then output the corresponding amino acid from a dictionary.

import re

dictionary = {
'TTT':'Phe',   'TCT':'Ser',  'TGT':'Cys',  'TAT':'Tyr',
'TTC':'Phe',   'TCC':'Ser',  'TGC':'Cys',  'TAC':'Tyr',
'TTG':'Leu',   'TCG':'Ser',  'TGG':'Trp',  'TAG':'***',
'TTA':'Leu',   'TCA':'Ser',  'TGA':'***',  'TAA':'***',

'CTT':'Leu',   'CCT':'Pro',  'CGT':'Arg',  'CAT':'His',
'CTC':'Leu',   'CCC':'Pro',  'CGC':'Arg',  'CAC':'His',
'CTG':'Leu',   'CCG':'Pro',  'CGG':'Arg',  'CAG':'Gln',
'CTA':'Leu',   'CCA':'Pro',  'CGA':'Arg',  'CAA':'Gln',

'GTT':'Val',   'GCT':'Ala',  'GGT':'Gly',  'GAT':'Asp',
'GTC':'Val',   'GCC':'Ala',  'GGC':'Gly',  'GAC':'Asp',
'GTG':'Val',   'GCG':'Ala',  'GGG':'Gly',  'GAG':'Glu',
'GTA':'Val',   'GCA':'Ala',  'GGA':'Gly',  'GAA':'Glu',

'ATT':'Ile',   'ACT':'Thr',  'AGT':'Ser',  'AAT':'Asn',
'ATC':'Ile',   'ACC':'Thr',  'AGC':'Ser',  'AAC':'Asn',
'ATG':'Met',   'ACG':'Thr',  'AGG':'Arg',  'AAG':'Lys',
'ATA':'Ile',   'ACA':'Thr',  'AGA':'Arg',  'AAA':'Lys',
}

def getAminoAcid(s):
    string = re.sub("[^a-zA-Z]+", '', s.upper()) # Similar to Java's string.replaceAll() / regex. This automatically makes the string uppercase and removes all non-alphabetical characters, including spaces.
    if not len(string) % 3 == 0: # Will not evaluate the string if it's not a complete triple
        print("Error: The sequence", string[-len(string):], "is not a complete triple.")
    else:
        sequences = [(string[i:i+3]) for i in range(0, len(string), 3)] # Similar to a regular for loop; automatically appends every 3 characters to the list
        for seq in sequences: # Iterate through the list of sequences
            if not all(char in 'TGCA' for char in seq): # Check if the sequence is valid. If it contains a non T/G/C/A character, print "invalid sequence"
                print(seq, "invalid sequence") # This works assuming that the dictionary contains all possible 3-character combinations of T, G, C, and A.
            else: 
                for nucleotide, aminoAcid in dictionary.items(): # Iterate through the dictionary for a nucleotide matching the sequence
                    if nucleotide == seq:
                        print(nucleotide, aminoAcid)

        
while True:
    userInput = input("Enter a nucleotide sequence or press ENTER to quit: ")
    if userInput == "": 
        print("Program stopped. To resume using, simply restart the program.")
        break
    else:
        getAminoAcid(userInput)