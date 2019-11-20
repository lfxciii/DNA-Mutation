## Introduction to Programming, Task 25
## Ruben Louw, [2019-05-04]
## Input DNA string and output amino acid sequence

## lookup table for SLCs and a list DNA codons
#slc = {"ATT": "I",
#        "ATC": "I",
#        "ATA": "I",

#        "CTT": "L",
#        "CTC": "L",
#        "CTA": "L",
#        "CTG": "L",
#        "TTA": "L",
#        "TTG": "L",

#        "GTT": "V",
#        "GTC": "V",
#        "GTA": "V",
#        "GTG": "V",    
   
#        "TTT": "F",
#        "TTC": "F",

#        "ATG": "M"}

## Write a function called ‘translate’ that, when given a DNA sequence of
## arbitrary length,
## the program identifies and returns the amino acid sequence of the DNA using
## the
## amino acid SLC code found in that table.
## E.g DNA Input: ATTATTATT
## Output: ​III​ (representing: Isoleucine, Isoleucine, Isoleucine ​)
#def translate(dna_sequence):
    
#    # amino acid sequence
#    a_a_s = ""

#    # convert input to codon list for iteration.
#    dna_sequence = [dna_sequence[i:i + 3] for i in range(0, len(dna_sequence), 3)]    
    
#    # foreach codon, determine slc value
#    for codon in dna_sequence:
        
#        if codon in slc.keys():
#            a_a_s += slc[codon] 
#        else:
#            a_a_s += "X"        
        
#    return a_a_s


#def mutate():       

#    # read the contents of the text file named 'DNA.txt'. 
#    dna_file = open("DNA.txt", "r")

#    #comment out to test against task1 sequence
#    #dna_file = open("Test.txt", "r") 

#    dna_file = [x.rstrip() for x in dna_file.readlines()] 
#    dna_file = str("".join(dna_file))

#    #You must then write two new text files, one named normalDNA.txt and the other named mutatedDNA.txt.     
#    #The file normalDNA.txt must have the same DNA sequence as DNA.txt with the 'a' changed to an 'A'.     
#    normal_dna = open("normalDNA.txt", "w")
#    normal_dna.write(dna_file.replace('a', 'A'))
#    normal_dna.close()

#    #The file mutatedDNA.txt must have the same DNA sequence as DNA.txt with the 'a' changed to a 'T'.     
#    mutated_dna = open( "mutatedDNA.txt", "w")
#    mutated_dna.write(dna_file.replace('a', 'T'))
#    mutated_dna.close()

##call the translate function that you wrote in Task 1, to take in text file input. 
#def txtTranslate(sequence_file):    
#    return translate(sequence_file)               

### input dna sequence
##dna_sequence = input("DNA Input: ")

### do input translation
##print(translate(dna_sequence))

## do mutation
#mutate()

## do file translation
#normal_sequence = open("normalDNA.txt", "r")  
#print("Normal Amino Acid sequence " + txtTranslate(normal_sequence.read()))

#mutated_sequence = open("mutatedDNA.txt", "r")
#print("Mutated Amino Acid sequence " + txtTranslate(mutated_sequence.read()))

