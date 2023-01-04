people = [{"name" : "harry", "house" : "gryffindor"},{"name" : "ram" , "house" : "ayodha"}, {"name":"shyam","house":"brindavan"}]

people.sort(key= lambda person : person ["house"])
print(people)
