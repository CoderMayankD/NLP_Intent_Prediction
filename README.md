# NLP_Intent_Prediction
Task was about creating an nlp model that can predict text intentions as buyer, seller, buyer seller, and nothing intent I have completed the task and now submitting files as:
	### 1. preprocessingNLP.ipynb : Having preprocessing and training.

		I would like to specify here that anyone of you who uses my model can train the model on the basis of one sentence with label or a whole text file filled with sentences with label in both ways my model can be trained it will Encode the sentences And save in csv file which will later be used by the predictive model that I made using python language to decode test sentences and particular intentions as buyer intent, seller intent, buyer seller intent or nothing intent.
I have created my model in such a way that every file having training sentences should be provided with the labels for example one file having all the buyer intense sentences and another file having all the seller intent sentences which can be loaded to this preprocessingNLP.ipynb file and training file will be updated after automatic decoding sentences as per training model.

Prequisites: !pip install re, !pip install pandas,!pip install openpyxl, !pip install tqdm.

	### 2. Model.ipynb : Having predictive model and testing facility.
		
		While using my model I would like to specify few things that a user should know I wish the environments or the libraries that have been used extensively to create the model should be present in the IDE like VS Code, for the model to work.
Required library files are : 

!pip install openpyxl, !pip install scikit-learn, !pip install matplotlib.pyplot,!pip install seaborn, !pip install pandas.
