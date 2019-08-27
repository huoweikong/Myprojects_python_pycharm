from Bio import Entrez
Entrez.email = "A.N.Other@example.com"
handle = Entrez.einfo()
record = Entrez.read(handle)
#handle = Entrez.einfo()
#result = handle.read()

#print(result)
print(record)
print(record.keys())
print(record['DbList'])
handle = Entrez.einfo(db="pubmed")
record = Entrez.read(handle)
print(record["DbInfo"]["Description"])
print(record["DbInfo"]["Count"])
print(record["DbInfo"]["LastUpdate"])
for field in record["DbInfo"]["FieldList"]:

    print("%(Name)s, %(FullName)s, %(Description)s" % field)