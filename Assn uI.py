#Set is mutable or not
set={1,2,3,4,"Sumeet"}
print(set)

#Update
set.add(5)
print(set)

#Remove
set.remove(4)
print(set)

# Union operation
set1={"A",69}
set2={1,2,3}
set3={"data",1625,"Sumeet"}
set5=set1|(set2)|set3
print(set5)

# Intersection
set1={"Sum","eet"}
set2={69,71,3,"A","Sum","EET"}
print(set1.intersection(set2))
