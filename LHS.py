# Para utilizar, crie um arquivo na mesma pasta chamado 'vectors.csv', e defina o tamanho da amostra pelo sampleSize

import csv
from pyDOE import lhs

sampleSize = 10
vectors = 'vectors.csv'

def csvToHash(vectors):
	# Reads the vectors file, and returns a dictionary with the values
	# of each vector, and the header

	firstTime = True
	i = 0
	possibleValues = {}
	csvFile = open(vectors, 'r')
	csvReader = csv.reader(csvFile, delimiter=',', quotechar='|')

	for row in csvReader:
		while i < len(row):
			if not firstTime:
				if row[i] not in possibleValues[i] and row[i] != "":
					possibleValues[i].append(row[i])
			else:
				headerCsv = row
				possibleValues[i] = []
			i += 1

		firstTime = False
		i = 0

	return (possibleValues,headerCsv)
	
def lhsValues(possibleValues, sampleSize):
	lhd = lhs(len(possibleValues), samples=sampleSize)

	return lhd

##
## @brief      This method map a continuous value to a discrete one.
##             We apply this method to every value in our dictionary that
##             contains all possible values supplied by the user. This allow
##             to have a consistent sample.
##
## @param      value         The continous value that will use as baseline.
## @param      discrete      The discrete value that we want to map.
##
## @return    Returns the next discrete value.
##
def discrete(value, discrete):
	diff = 1/discrete
	total=diff
	i=1
	while (total<value):
		i+=1
		total+=diff
	return i

##
## @brief      This method creates a list of lists which number of lists
##             is equal to "sampleSize". Each list has a value for each
##             variable, creating a possibility, among all. For do this
##             we take the values created from the "lhs" method and map
##             the values to our values taken from CSV using the "discrete"
##             function (see its documentation for more info). Each list
##             has a size equal to the number of variable in each item
##             of this list has a value from the csv that represents that
##             column.
##
## @param      self            Non static method.
## @param      lhd             Matrix samplesSize x len(possibleValues)
##                             with values from the "lhs" method. See its
##                             documentation for more info.
##
## @param      possibleValues  A dictionary (Hash Table) with the number
##                             of entries equals to the number of variables
##                             which maps to a list with all possible
##                             values of that variable.
##
## @param      sampleSize      Number of possibilities that the user wants.
##
## @return     A list of lists containing the continous values mapped
##             to values of variable which came from the csv informed
##             by the user.
##
def mapValues(lhd, possibleValues, headerCsv, sampleSize):
	mappedValues = []
	for i in range(0, sampleSize):
		chosenValues = []
		for j in range(0, len(possibleValues)):
			if headerCsv[j][:2] == '@#':
				value = float(min(possibleValues[j]))+(float(max(possibleValues[j]))-float(min(possibleValues[j])))*lhd[i][j]
				# print(headerCsv[j])
				# print('max',float(max(possibleValues[j])))
				# print('min',float(min(possibleValues[j])))
				# print('dif',float(max(possibleValues))-float(min(possibleValues)))
				#print(lhd[i][j])
				#print(value)
			else:
				value_position = int(discrete(lhd[i][j],len(possibleValues[j])))-1
				value = str(possibleValues[j][value_position])
			chosenValues.append(value)
		mappedValues.append(chosenValues)

	return mappedValues

def writeMappedValues(mappedValues):
	newFile = open("sample.csv", 'w', newline="")
	csvWriter = csv.writer(newFile, delimiter=',', quotechar='|')

	csvWriter.writerow(headerCsv)

	for values in mappedValues:
		csvWriter.writerow(values)

ReadCSV = csvToHash(vectors)

possibleValues = ReadCSV[0]
headerCsv = ReadCSV[1]

lhd = lhsValues(possibleValues, sampleSize)

mappedValues = mapValues(lhd, possibleValues, headerCsv, sampleSize)

writeMappedValues(mappedValues)
