import pandas as pd
# Load dataset
cc_apps = pd.read_csv('datasets/cc_approvals.data',header=None)
cc_apps_description = cc_apps.describe()
print(cc_apps_description)

# Print DataFrame information
cc_apps_info = cc_apps.info()
from sklearn.model_selection import train_test_split
# Drop the features 11 and 13
cc_apps = cc_apps.drop([11,13],axis=1)

# Split into train and test sets
cc_apps_train, cc_apps_test = train_test_split(cc_apps, test_size=0.33, random_state=42)
import numpy as np
# Replace the '?'s with NaN in the train and test sets
cc_apps_train = cc_apps_train.replace('?','NaN')
cc_apps_test = cc_apps_test.replace('?','NaN')
# Impute the missing values with mean imputation
cc_apps_train.fillna(cc_apps_train.mean(), inplace=True)
cc_apps_test.fillna(cc_apps_train.mean(), inplace=True)

# Count the number of NaNs in the datasets and print the counts to verify
print(cc_apps_train.isnull().sum())
print(cc_apps_test.isnull().sum())
for col in cc_apps_train.columns:
    # Check if the column is of object type
    if cc_apps_train[col].dtypes == 'object':
        # Impute with the most frequent value
        cc_apps_train = cc_apps_train.fillna(cc_apps_test[col].value_counts().index[0])
        cc_apps_test = cc_apps_test.fillna(cc_apps_test[col].value_counts().index[0])

# Count the number of NaNs in the dataset and print the counts to verify
# ... YOUR CODE FOR TASK 6 ...
print(cc_apps_test.isna().sum())
print(cc_apps_test.isna().sum())