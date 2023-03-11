# data = pd.read_csv('../data/dataset.csv')
# # features to randomize
# features_to_randomize = ['Customer Lifetime Value', 'Education', 'Gender', 'Income', 'Location Code','Marital Status', 'Months Since Last Claim', 'Months Since Policy Inception','Number of Open Complaints', 'Number of Policies', 'Sales Channel']
# num_vars = ['Customer Lifetime Value', 'Income', 'Months Since Last Claim', 'Months Since Policy Inception', 'Number of Open Complaints', 'Number of Policies']
# cat_vars = ['Education', 'Gender', 'Location Code', 'Marital Status', 'Sales Channel']

# # convert 'Response' feature to binary output
# data['Engaged'] = data['Response'].apply(lambda x: 1 if x=='Yes' else 0)
# data.drop('Response', axis=1, inplace=True)
# # factorize categorical variables
# cat_vars = ['Education', 'Gender', 'Location Code', 'Marital Status', 'Sales Channel']
# for var in cat_vars:
#     le = LabelEncoder()
#     data[var] = le.fit_transform(data[var].astype(str))

# print(data.head())
# import train_test_split
from sklearn.model_selection import train_test_split


# train split data for df
X_train, X_test, y_train, y_test = train_test_split(df.drop('Engaged', axis=1), df['Engaged'], test_size=0.2, random_state=42)
# train split data for df_noisy
X_train_noisy, X_test_noisy, y_train_noisy, y_test_noisy = train_test_split(df_noisy, df_noisy['Engaged'], test_size=0.2, random_state=42)

# calculate the accuracy for df
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print('Accuracy for df: {:.2f}'.format(accuracy_score(y_test, y_pred)))

# calculate the accuracy for df_noisy
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train_noisy, y_train_noisy)
y_pred = rf.predict(X_test_noisy)
print('Accuracy for df_noisy: {:.2f}'.format(accuracy_score(y_test_noisy, y_pred)))
