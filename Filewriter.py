import csv
def Filewriter(list):
    outputFile = open('output.csv', 'a', newline='')
    outputWriter = csv.writer(outputFile)
    for i in range(len(list)):
     outputWriter.writerow(list[i])