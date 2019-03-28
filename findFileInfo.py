import os
from searchData import seperateJSONData,readJSONData

##Remove the file
def removefile(filename):
    if (os.path.exists(filename)):
        os.remove(filename)

##Wrtie data in the file
def writeFile(label,fileName,String):
        with open(label, 'a') as fp:
            fp.write(fileName + "," + String)
            fp.write("\n")
        fp.close()

##Read all the files from the folder and write the result to another file
def loopFiles(label,training_dir):
    files = [os.path.join(training_dir,fi) for fi in os.listdir(training_dir)]
    for file in files:
        filename = file.split(os.sep)[1]
        b,w=seperateJSONData(readJSONData(file))
        writeFile(label,filename, b + "," + w)
    print("Finish the collection !")   
     
def main():
    filename="FileTrain.label"
    filename_test="FileTest.label"
    ##TRAINING :
    removefile(filename)
    training_dir ="TRAINING"
    loopFiles(filename,training_dir)
    ##TESTING:
    removefile(filename_test)
    training_dir ="TESTING"
    loopFiles(filename_test,training_dir)
main()