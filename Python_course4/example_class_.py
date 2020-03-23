# cityNames = ["Detroit","Ann arbor","Shanghai","Beijing"]
# populations = [342434,23213,22212,1546]
# states = ["MI","MI","CN","CN"]
#
# city_tuples = zip(cityNames,populations,states)
#
# class City:
#     def __init__(self,n,p,s):
#         self.name = n
#         self.populations = p
#         self.state = s
#     def __str__(self):
#         return "{},{}(Pop:{})".format(self.name,self.state,self.populations)
# for city_tuple in city_tuples:
#     name,pop,state = city_tuple
#     city = City(name,pop,state)
#     print(city)


class Cereal:
    def __init__(self,str1,str2,num):
        self.name = str1
        self.brand = str2
        self.fiber = num
    def __str__(self):
        return "{} cereal is produced by {} and has {} grams of fiber in every serving!".format(self.name,self.brand,self.fiber)


c1 = Cereal("Corn Flakes","Kellogg's",2)
c2 = Cereal("Honey Nut Cheerios","General Mills",3)
print(c1)
print(c2)
