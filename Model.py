
import pandas as pd
import numpy as np
import plotly.express as px 
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

file="dataset_trained.xlsx.xlsx"
df=pd.read_excel(file)
df.describe(include="all")

# %%
px.histogram(df,"label", "buyer","buyer")

# %%
px.histogram(df,"label", "seller","seller")

# %%
px.histogram(df,"label", "buyer_verb","buyer_verb")

# %%
px.histogram(df,"label", "seller_verb","seller_verb")

# %%
px.histogram(df,"label", "products","products")

# %%
px.histogram(df,"label", "ad_campaign","ad_campaign")

# %%
px.histogram(df,"label", "intent_sufixes","intent_sufixes")

# %%
px.histogram(df,"label", "negations","negations")

# %%
# Import necessary libraries
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import cross_val_score, train_test_split

# Load your dataset (replace 'data.csv' with your dataset file)
data = df

# Assuming 'X' contains your feature columns and 'y' contains your target variable
X = data.drop('label', axis=1)
y = data['label']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Logistic Regression model
model = LogisticRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("---------------------------------------------")
print("Confusion Matrix:\n", confusion_mat)
print("---------------------------------------------")
print("Classification Report:\n", classification_rep)


# %%
plt.figure(figsize=(8, 2))
sns.set(font_scale=.8)  # Adjust font size for clarity
sns.heatmap(confusion_mat, annot=True, fmt="d", cmap="Blues",
            xticklabels=["N","BS","B","S"], yticklabels=["N","BS","B","S"])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

# %%
# Initialize your Logistic Regression model
LRmodel = LogisticRegression()

# Specify the number of folds for k-fold cross-validation
k = 10

# Perform k-fold cross-validation on the training data
accuracy_scores = cross_val_score(LRmodel, X_train, y_train, cv=k, scoring='accuracy')

# Print the accuracy scores for each fold
for fold, accuracy in enumerate(accuracy_scores, start=1):
    print(f"Fold {fold}: Accuracy = {accuracy*100:.2f}")

# Calculate the mean and standard deviation of accuracy scores
mean_accuracy = np.mean(accuracy_scores)*100
std_accuracy = np.std(accuracy_scores)

print(f"\nMean Accuracy: {mean_accuracy:.2f}")
print(f"Standard Deviation of Accuracy: {std_accuracy:.2f}")

# Now, you can train your model on the entire training dataset and evaluate on the test dataset
LRmodel.fit(X_train, y_train)
test_accuracy = LRmodel.score(X_test, y_test)*100
print(f"\nTest Accuracy: {test_accuracy:.2f}")


# %% [markdown]
# Enabling User Testing here: 

# %%
def predict_intent(testcase):
    import re # regular expression for pattern detection
    import openpyxl as op # For using tabular data.

    # Importing Buyers and Sellers data for training
    wb=op.load_workbook(r"training_intent_samples.xlsx")
    ws=wb.active

    buyers= []
    buyer_verbs=[]
    products=[]
    sellers = []
    seller_verbs=[]
    ad_camp=[]
    negations=[]
    intent_suffixes=[]

    # Extracting buyers and seller lists of WORD BANK to predict the intents
    for row in ws.iter_rows():
        if row[0].value is not None:
            buyers.append(str(row[0].value))
        if row[1].value is not None:
            buyer_verbs.append(str(row[1].value))
        if row[2].value is not None:
            products.append(str(row[2].value))
        if row[3].value is not None:
            sellers.append(str(row[3].value))
        if row[4].value is not None:
            seller_verbs.append(str(row[4].value))
        if row[5].value is not None:
            ad_camp.append(str(row[5].value))
        if row[6].value is not None:
            negations.append(str(row[6].value))
        if row[7].value is not None:
            intent_suffixes.append(str(row[7].value))

    # Creating patterns for regular expression for buyer and seller intents
    buyer_pattern = r'\b(?:' + '|'.join(map(re.escape, buyers)) + r')\b'
    buyer_verbs_pattern = r'\b(?:' + '|'.join(map(re.escape, buyer_verbs)) + r')\b'
    products_pattern = r'\b(?:' + '|'.join(map(re.escape, products)) + r')'
    sellers_pattern = r'\b(?:' + '|'.join(map(re.escape, sellers)) + r')\b'
    seller_verbs_pattern = r'\b(?:' + '|'.join(map(re.escape, seller_verbs)) + r')\b'
    ad_camp_pattern = r'\b(?:' + '|'.join(map(re.escape, ad_camp)) + r')\b'
    negations_pattern = r'\b(?:' + '|'.join(map(re.escape, negations)) + r')\b' 
    intent_suffixes_pattern = r'\b(?:' + '|'.join(map(re.escape, intent_suffixes)) + r')' 

    wb.close()


    # Finding all occurrences using the re module for patterns
    text=testcase

    buyer_match = re.findall(buyer_pattern, text, flags=re.IGNORECASE)
    buyer_verbs_match = re.findall(buyer_verbs_pattern, text, flags=re.IGNORECASE)
    products_match = re.findall(products_pattern, text, flags=re.IGNORECASE)
    seller_match = re.findall(sellers_pattern, text, flags=re.IGNORECASE)
    seller_verbs_match = re.findall(seller_verbs_pattern, text, flags=re.IGNORECASE)
    ad_camp_match = re.findall(ad_camp_pattern, text, flags=re.IGNORECASE)
    negations_match = re.findall(negations_pattern, text, flags=re.IGNORECASE)
    intent_suffixes_match= re.findall(intent_suffixes_pattern, text, flags=re.IGNORECASE)


    B=len(buyer_match)
    S=len(seller_match)
    SV=len(seller_verbs_match)
    BV=len(buyer_verbs_match)
    P=len(products_match)
    Ad=len(ad_camp_match)
    IS=len(intent_suffixes_match)
    PN=len(negations_match)


    # prediction: 
    pred=model.predict(np.array([B,S,SV,BV,P,Ad,IS,PN]).reshape(1, -1))
    pred=str(pred[0])
    
    if pred=='BS': return "Buyer Seller Intent"
    elif pred=='B': return "Buyer Intent"
    elif pred=='S': return "Seller Intent"
    elif pred=='N': return "Nothing"



# %%
testcase=input("Enter Your Sentence to be tested here: ")
print(predict_intent(testcase).upper(),"\n")


