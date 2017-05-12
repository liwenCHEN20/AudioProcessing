# AudioProcessing

This project is related to audio processing, it has 2 main objectives:

- Single file Classification: Distinguish the audio file which have normal quality of sound and the "broken" audio files (Contents of those audio files don't contain any meaning due to bad recording.) with machine learning methods.
- Audio segmentation: Identifies sub-block of the audio which has different type of content than the part of audio adjacent to that block with time stamps.

# Tool and package used

- Python 2.7 : https://www.python.org/
- pyAudioAnalysis : https://github.com/tyiannak/pyAudioAnalysis

# Single file Classification

The files related to the Single file Classification are inside the 'SFC' folder, the Python script 'trainAndTest.py' is used to train and test audio classifier which handles the classification between "Good" and "Bad" audio files.

Before execute the script, put audio files which used for training and testing in to the folder "SetA" and "SetB", be default, folder "SetA" contains the audio files for training and "SetB" contains the audio files for testing, one can rename the folders in an opposite way to swap the testing and training set.

There are four dummy blank text files in the folders which contains the testing and training sets, these files are only created to display the correct path user should put the audio files in. (Otherwise git won't contain the empty folders after the this project been cloned from the web.)

To execute the script after the training and testing files are placed, type the following line in the terminal:

- python trainAndTest.py <modelName> <midtermWindow> <midtermStep>

modelName is the name of the machine learning method which can only be the following:

- knn : k-nearest neighbors algorithm
- svm : Support vector machine
- randomforest : Random forest
- extratrees : Extra Trees
- gradientboosting : Gradient boosting

midtermWindow and midtermStep are the mid-term block size and step used while training the classifier from the samples. (In seconds)

The classifier generated after training and testing as well as some related files will be created in folder "Models", if a the classifier with the same type of learning model already exists, the old classifier will be replaced by the new one.

To test a already generated classifier, comment out the line 11 to 19 in trainAndTest.py and run the script again with the same modelName as the first command line argument.

# License

Copyright 2017 Xuping Fang

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
