from pyAudioAnalysis import audioTrainTest as aT
from pyAudioAnalysis import audioSegmentation as aS
from os import path

import os
import sys

modelName = sys.argv[1]     # Command line argument 1 is the name of the training model.


mtw = float(sys.argv[2])      # Command line argument 2 is the mid-term window.
mts = float(sys.argv[3])      # Command line argument 3 is the mid-term step.


aT.featureAndTrain(["SetA/Good/",
                    "SetA/Bad/"], 
                   mtw, mts, aT.shortTermWindow, aT.shortTermStep, modelName, "Models/"+modelName)


for fileName in [f for f in os.listdir("SetB/Good/") if path.isfile(path.join("SetB/Good/",f))]:
    print "Good: "+fileName
    print aT.fileClassification("SetB/Good/"+fileName, "Models/"+modelName, modelName)

for fileName in [f for f in os.listdir("SetB/Bad/") if path.isfile(path.join("SetB/Bad/",f))]:
    print "Bad: "+fileName
    print aT.fileClassification("SetB/Bad/"+fileName, "Models/"+modelName, modelName)
