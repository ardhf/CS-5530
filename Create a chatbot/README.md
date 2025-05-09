# This is our Group Project for CS-5530 (Create a chatbot)

## Two ChatbotFromScratch notebooks
Both of the ChatbotFromScratch notebooks are the same, except ```ChatbotFromScratch_Final.ipynb``` can be viewed in the github preview and the ```ChatbotFromScratch_Final_with_Outputs.ipynb``` cannot due to an issue with the cell outputs. The code is the same for both files, but the only change is that ```ChatbotFromScratch_Final.ipynb``` doesn't have any cell outputs.

## Model Files
The .pth files can be found in the google drive link below:<br>
https://drive.google.com/drive/folders/1At7fosDvUSospZ7MK5XEM2pbVlq2v22x?usp=drive_link

## Running the Final Model
To run the final model you need the ```fine_tuned_model.pth``` file from the Google Drive link. Put this file in your Google Colab file storage and run the final cell in the notebook (Labeled with ```Inference on Model```). This will run the model without the classifier. If you wish to use the classifier you need to change ```enable_classifier``` to True in the ```Inference on Model``` cell, and then run all of the cells under the ```Classifier``` heading in the notebook. Then you will be able to run the ```Inference on Model``` cell and get output with the classifier.

## Files and Authors
Chatbot with Transformer - Rohan<br>
Chatterbot - Jim<br>
data_generation - Daniel<br>
ChatbotFromScratch_Final - Alex<br>
data folder - data for the final model
