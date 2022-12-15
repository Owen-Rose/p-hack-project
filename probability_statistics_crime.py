import csv
import statistics

class CrimeStatistics():
    crime_statistics_list = []
    #Relevant data should be in the list above, so sector, community name, category, crime count and year from the provided csv file
    def readFile(self):
        with open("Community_Crime_Statistics.csv") as csvfile:
            csvRead = csv.reader(csvfile)
            row_data = []
            for element in csvRead:
                row_data += [[element[0], element[1], element[2], element[3], element[6]]]
            self.crime_statistics_list = row_data
    def getCrimeStatistics_List(self):
        print(self.crime_statistics_list)

    def getCrimeCountMean(self):
        for sublist in self.crime_statistics_list:
            print(sublist[3])

class CrimeProbability():

        def __init__(self):
            pass

        def yearly_trend(year):
            pass            

x = CrimeStatistics()

x.readFile()
x.getOverallCrimeCountMean()