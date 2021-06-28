#For use in downloading protein coding sequence regions from the NCBI nuccore database for a given gene and a given species list.

from Bio import Entrez
from Bio import SeqIO
import os

Entrez.email = "youremail@something.com"
species_list = ["Gallus gallus", "Numida meleagris"]
#Must match name on NCBI taxonomy database.

length = len(species_list)
gID = "gene string"
filename = "yourfile.txt"
#Ex fox3

for i in range(length):
  species = species_list[i]
  handle = Entrez.esearch(db="nucleotide", term= species + "[Orgn] AND " + gID + "[Gene]", idtype="acc")
  record = Entrez.read(handle)

  idlist = record["IdList"]
  handle = Entrez.efetch(db="nuccore", id=idlist, rettype="fasta_cds_na", retmax = 3, retmode = "text")
  print(species, file =open(filename, "a"))
  print(handle.read(),file =open(filename, "a"))
