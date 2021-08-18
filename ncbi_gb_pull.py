#For use in downloading protein coding sequence regions from the NCBI nuccore database for a given gene and a given species list.

from Bio import Entrez
from Bio import SeqIO
import os

Entrez.email = "youremail@something.com"
species_list = ["Gallus gallus", "Numida meleagris"]
#Must match name on NCBI taxonomy database.

length = len(species_list)
f = open("geneName.txt", "w")
filename = "geneName.txt"
#Change geneName to your actual gene with each iteration of running this code

for i in range(length):
  species = species_list[i]
  handle = Entrez.esearch(db="nucleotide", term= species + "[Orgn] AND full title of gene from NCBI database", idtype="acc") 
  #Change to fit each gene. Search your gene in the NCBI database and put the description after AND in the above line.
  record = Entrez.read(handle)

  idlist = record["IdList"]
  handle = Entrez.efetch(db="nuccore", id=idlist, rettype="fasta_cds_na", retmode = "text", retmax = 10)
  h = handle.read()
  great = h.count(">")

  print(great)
  if great > 1:
    s = h.split(">")
    for gene in s:
      if "geneName" in gene:
        #Remember to update this with your proper gene name
        h = gene

  if "geneName" in h:
    #Update with correct gene name
    print(species, file =open(filename, "a"))
    print(h,file =open(filename, "a"))


  time.sleep(2)
