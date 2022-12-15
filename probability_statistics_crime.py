import csv

class CrimeStatistics():
    crime_statistics_list = []
    #Relevant data should be in the list above, so sector, community name, category, crime count and year from the provided csv file
    def readFile(self):
        with open("Community_Crime_Statistics.csv") as csvfile:
            csvRead = csv.reader(csvfile)
            row_data = []
            for element in csvRead:
                row_data += [[element[0], element[1], element[2], element[3], element[6]]]
                print(row_data)
    pass

class CrimeProbability():

        def __init__(self):
            pass

        def yearly_trend(year):
            pass            

x = CrimeStatistics()

x.readFile()