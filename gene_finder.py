# -*- coding: utf-8 -*-
"""
Gene Finder Project main file
Software Design Spring 2020

@author: Lilo Heinrich

"""

import random
from amino_acids import aa, codons, aa_table   # you may find these useful
from load import load_seq

def shuffle_string(s):
    """Shuffles the characters in the input string
        NOTE: this is a helper function, you do not
        have to modify this in any way """
    return ''.join(random.sample(s, len(s)))

# YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###

def get_complement(nucleotide):
    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
    >>> get_complement('A')
    'T'
    >>> get_complement('C')
    'G'
    """

    pairs = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    return pairs[nucleotide]
    pass

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence

        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    >>> get_reverse_complement("ATGCCCGCTTT")
    'AAAGCGGGCAT'
    >>> get_reverse_complement("CCGCGTTCA")
    'TGAACGCGG'
    """

    rev_dna = ''
    for i in dna:
        rev_dna = get_complement(i) + rev_dna
    return rev_dna
    pass

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start
        codon and returns the sequence up to but not including the
        first in frame stop codon.  If there is no in frame stop codon,
        returns the whole string.

        dna: a DNA sequence
        returns: the open reading frame represented as a string
    >>> rest_of_ORF("ATGTGAA")
    'ATG'
    >>> rest_of_ORF("ATGAGATAGG")
    'ATGAGA'
    >>> rest_of_ORF("ATGTGCCC")
    'ATGTGCCC'
    >>> rest_of_ORF("ATGCATGAATGTAGATAG")
    'ATGCATGAATGTAGA'
    """

    end_codons = ['TAG', 'TGA', 'TAA']
    index = len(dna)
    i = 0
    while index == len(dna) and i < 3*(len(dna)+2):
        for c in end_codons:
            n =  dna.find(c, 3*(i+1), 3*(i+2))
            if n != -1 and (n < index or index == len(dna)):
                index = n
        i += 1
    return dna[0:index]
    pass

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA
        sequence and returns them as a list.  This function should
        only find ORFs that are in the default frame of the sequence
        (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """

    orfs = []
    start_codon = 'ATG'
    for n in range(len(dna)//3): # go through each codon
        i = dna.find(start_codon,n*3,(n+1)*3)
        if i != -1:
            orf = rest_of_ORF(dna[i:])
            dna = dna[len(orf)+i:]
            orfs.append(orf)
    return orfs
    pass

def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in
        all 3 possible frames and returns them as a list.  By non-nested we
        mean that if an ORF occurs entirely within another ORF and they are
        both in the same frame, it should not be included in the returned list
        of ORFs.

        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """

    orfs = []
    start_codon = 'ATG'
    for n in range(len(dna)): # go through each letter
        i = dna.find(start_codon,n,n+3)
        if i != -1:
            for orf in find_all_ORFs_oneframe(dna[i:]):
                orfs.append(orf)
    return orfs
    pass

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on
        both strands.

        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """

    orfs = []
    orfs += find_all_ORFs(dna)
    orfs += find_all_ORFs(get_reverse_complement(dna))
    return orfs
    pass

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns
        it as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """

    orf = []
    for n in find_all_ORFs_both_strands(dna):
        if len(n) > len(orf):
            orf = n
    return orf
    pass

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence

        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    max = 0
    for i in range(num_trials):
        shuffle = shuffle_string(dna)
        n = len(longest_ORF(shuffle))
        if n > max:
            max = n
    return max
    pass

def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).

        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """

    protein = ''
    for n in range(len(dna)//3): # go through each codon
        protein += aa_table[dna[3*n:3*(n+1)]]
    return protein
    pass

def gene_finder(dna):
    """ Returns amino acid sequences that are likely coded by the specified dna

        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    >>> gene_finder(load_seq("./data/X73525.fa"))
    ' '
    """

    threshold = longest_ORF_noncoding(dna, 1500)
    orfs = find_all_ORFs_both_strands(dna)
    proteins = []
    for orf in orfs:
        if len(orf) <= threshold:
            proteins.append(coding_strand_to_AA(orf))
    return proteins
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # dna = load_seq("./data/X73525.fa")
