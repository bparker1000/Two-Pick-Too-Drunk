from start import DataImporter
import sys

class Main:
    def __init__(self):
        dataImporter = DataImporter()
        dataImporter.saveJson("./hackathon_data")


if __name__ == '__main__':
    #Runs the program
    Main()    
