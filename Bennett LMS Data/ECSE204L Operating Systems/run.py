from os import walk
# import comtypes.client
import os

def PPTtoPDF(inputFileName, outputFileName, formatType=32):
    # powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    # powerpoint.Visible = 1
    # if outputFileName[-3:] != 'pdf':
        # outputFileName = outputFileName + ".pdf"
    # deck = powerpoint.Presentations.Open(inputFileName)
    # deck.SaveAs(outputFileName, formatType)
    # deck.Close()
    print('done')
    # powerpoint.Quit()
    os.system('libreoffice --headless --invisible --convert-to pdf ' + inputFileName)
    # pass

def DOCtoPDF(inputFileName, outputFileName, formatType=17):
    # word = comtypes.client.CreateObject("Word.Application")
    # word.Visible = 1    
    # if outputFileName[-3:] != 'pdf':
        # outputFileName = outputFileName + ".pdf"
    # deck = word.Documents.Open(inputFileName)
    # deck.SaveAs(outputFileName, formatType)
    # deck.Close()
    print('done')
    # word.Quit()
    os.system('libreoffice --headless --invisible --convert-to pdf ' + inputFileName)
    # pass


search_dir = "./"
os.chdir(search_dir)
files = filter(os.path.isfile, os.listdir(search_dir))
files = [os.path.join(search_dir, f) for f in files] 
files.sort(key=lambda x: os.path.getmtime(x))

files.reverse()
print(files)
for file in files:
    try:
        if(file[-4:] == 'pptx'):
            print(file)
            print()
            PPTtoPDF(os.getcwd()+'\\'+file, os.getcwd()+'.\\'+file[:-4]+'pdf')

        if(file[-3:] == 'ppt'):
            print(file)
            print()
            PPTtoPDF(os.getcwd()+'\\'+file, os.getcwd()+'.\\'+file[:-3]+'pdf')

        if(file[-4:] == 'docx'):
            print(file)
            print()
            DOCtoPDF(os.getcwd()+'\\'+file, os.getcwd()+'.\\'+file[:-4]+'pdf')
        
        if(file[-3:] == 'doc'):
            print(file)
            print()
            DOCtoPDF(os.getcwd()+'\\'+file, os.getcwd()+'.\\'+file[:-3]+'pdf')
        
    except Exception as e:
        print(str(e))

        with open('logs.txt','a') as f:
            f.write(str(e)+'\n')