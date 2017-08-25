with open("data/asumissanat.txt","r") as f:
    asuminen = f.read().splitlines()

#Vain asua-johdokset
asuminen_strict = ".*asu.*"
