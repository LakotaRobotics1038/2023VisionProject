import os


dirt = '/home/team1038/workspace/2023VisionProject/mk1/aprilTagsLabeled'

for aprilTagsLabeled in os.listdir(dirt):

    file = os.path.join(dirt, aprilTagsLabeled)

    #checking if its a file

    if os.path.isfile(file) and file.find('.txt')!=-1:
        savePoint = open(file)
        lines = savePoint.readlines()
        newLines = []
       
        for line in lines:
            ID = line[0]
            numId = int(ID)
            newId = numId + 2
            newLine = str(newId) + line[1:]
            newLines.append(newLine)
        
        newFile = open(file, mode = 'w')

        for line in newLines:
            print(line,file = newFile)
