import os
import copy
import time
from kkloader import KoikatuCharaData
import datetime

def main():
    PNGNum = 0
    CCNum = 0
    ChangedNum = 0
    root = "."
    InitTime = time.perf_counter()
    LastTime = InitTime
    ChangeList = ""
    
    for dirpath, dirnames, filenames in os.walk(root):
        for filepath in filenames:
            if filepath.endswith('.png'):
                PNGNum += 1
                TotalFilePath = os.path.join(dirpath, filepath)
                try:
                    kc = KoikatuCharaData.load(TotalFilePath)
                    if (not hasattr(kc, "Custom")):
                        continue
                    
                    bChanged = False
                    '''
                    It takes me half a day to solve the problem caused by the existence of 2 Parameter.version 
                    '''
                    if (kc["Parameter"]["version"] == "0.0.6") :
                        kc["Parameter"]["version"] = "0.0.5"
                        bChanged = True
                        
                    if (kc.Parameter.version == "0.0.6"):
                        kc.Parameter.version = "0.0.5"
                        bChanged = True
                        
                    if (bChanged == True):
                        ChangeList += TotalFilePath + "\n"
                        kc.save(TotalFilePath)
                        ChangedNum += 1
                    CCNum += 1
                    
                except Exception as e:
                    pass
        if time.perf_counter() - LastTime > 10 :
            LastTime = time.perf_counter()
            print("Run " + str(LastTime - InitTime) + " seconds:")
            print("PNGNum: " + str(PNGNum))
            print("CCNum: " + str(CCNum))
            print("ChangedNum: " + str(ChangedNum))
            print("")
            
    print("Runs " + str(time.perf_counter() - InitTime) + " seconds:")
    print("PNGNum: " + str(PNGNum))
    print("CCNum: " + str(CCNum))
    print("ChangedNum: " + str(ChangedNum))
    print("")
    
    ChangedListFile = os.open("ChangedList" + str(datetime.datetime.now()).replace(":", "-") + ".txt", os.O_WRONLY | os.O_CREAT)
    os.write(ChangedListFile, ChangeList.encode("utf-8"))
    os.close(ChangedListFile)
    os.system('pause')

if __name__ == '__main__':
    main()