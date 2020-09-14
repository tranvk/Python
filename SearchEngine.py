import math


"""
Breakdown:
1. create function to take in document to be searched and construct word-count dictionary
2. Vector space
"""

#Vector Space: calculate the distances between two points, infinite planes

class VectorCompare:
    def magnitude(self, concordance): #why first arg self?

        if type(concordance) != dict:
            raise ValueError("Argument needs to be dictionary.")

        total = 0

        for word, count in concordance.iteritems(): #what is iteritems
            total += count ** 2

        return math.sqrt(total)


    def relation(self, concordance1, concordance2):

        if type(concordance1) != dict:
            raise ValueError("Arg needs to be a dictionary.")

        if type(concordance2) != dict:
            raise ValueError("Arg needs to be a dictionary.")

        relevance = 0
        topvalue = 0

        for word, count in concordance1.iteritems():

            if concordance2.has_key(word):
                topvalue += count*concordance2[word]
        if (self.magnitude(concordance1) * self.magnitude(concordance2)) != 0:
            return topvalue/(self.magnitude(concordance1) * self.magnitude(concordance2))
        else:
            return 0

    #Concordance: count of every word that occurs in a document
    def concordance(self, document):

        if type(document) != str:
            raise ValueError("Argument needs to be a string.")

        conc = {}

        for word in document.split(" "):

            if conc.has_key(word):
                conc[word] += 1

            else:
                conc[word] = 1

        return conc

v = VectorCompare()

documents = {
0:"Boy girl apple shirt pants music tree flower school",
1:"actor harry potter NYU pokemon go water bottle microsoft"
}

index = {
0: v.concordance(documents[0].lower()),
1: v.concordance(documents[1].lower())
}

searchterm = raw_input("Enter search term: ")

matches = []

for i in range(len(index)):
    relation = v.relation(v.concordance(searchterm.lower()), index[i])


    if relation != 0:
        matches.append((relation, documents[i][:100]))

matches.sort(reverse = True)

for i in matches: print(i[0], i[1])
