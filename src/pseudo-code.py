import pandas as pd
import numpy as np

# create a small example dataset

df = pd.DataFrame({
    "num_feat1": [1, 2, 3, 4],
    "num_feat2": [5, 6, 7, 8],
    "cat_feat": ["a", "b", "c", "d"]
})

# factorize categorical feature
df["cat_feat"] = pd.factorize(df["cat_feat"])[0]

# # add noise to categorical feature
# def add_noise_categorical(feature, sample_pct, noise_scale):
#     """
#     Add Gaussian noise to a categorical feature.
#     """
#     n_samples = int(len(feature) * sample_pct / 100)
#     samples = np.random.choice(feature, size=n_samples, replace=True)
#     noise = np.random.normal(scale=noise_scale, size=len(samples))
#     new_samples = np.clip(samples + noise, np.min(feature), np.max(feature))
#     new_feature = feature.copy()
#     new_feature[np.isin(feature, samples)] = new_samples
#     return new_feature
def add_noise_categorical(feature, sample_pct, noise_scale):
    """Add noise to categorical feature."""
    samples = feature.sample(frac=sample_pct / 100.0)
    noise = np.random.normal(0, noise_scale, len(samples))
    new_samples = np.clip(samples + noise, np.min(feature), np.max(feature))
    bool_mask = feature.isin(samples)
    feature[bool_mask] = new_samples
    return feature


X_categorical = df["cat_feat"].values
try:
    X_noisy_categorical = add_noise_categorical(X_categorical, 50, 0.1)
except:
    X_noisy_categorical = add_noise_categorical(X_categorical, 50, 0.1)


# # add noise to numerical features
# def add_noise_numerical(X, sample_pct, noise_scale):
#     """
#     Add Gaussian noise to numerical features in a dataset.
#     """
#     X_noisy = X.copy()
#     numerical_cols = [0, 1]  # column indices for numerical columns
#     for col in numerical_cols:
#         feature = X[:, col]
#         n_samples = int(len(feature) * sample_pct / 100)
#         samples = np.random.choice(feature, size=n_samples, replace=True)
#         noise = np.random.normal(scale=noise_scale, size=len(samples))
#         new_samples = np.clip(samples + noise, np.min(feature), np.max(feature))
#         X_noisy[:, col][np.isin(feature, samples)] = new_samples
#     return X_noisy

# add noise to numerical features
def add_noise_numerical(X, sample_pct, noise_scale):
    """
    Add Gaussian noise to numerical features in a dataset.
    """
    X_noisy = X.copy()
    numerical_cols = [0, 1]  # column indices for numerical columns
    for col in numerical_cols:
        feature = X[:, col]
        n_samples = int(len(feature) * sample_pct / 100)
        samples = np.random.choice(feature, size=n_samples, replace=True)
        noise = np.random.normal(scale=noise_scale, size=len(samples))
        new_samples = np.clip(samples + noise, np.min(X[:, col]), np.max(X[:, col]))
        X_noisy[:, col][np.isin(feature, samples)] = new_samples
    return X_noisy


numerical_cols = ["num_feat1", "num_feat2"]
X_numerical = df[numerical_cols].values

try:
    X_noisy_numerical = add_noise_numerical(X_numerical, 50, 0.1)
except:
    X_noisy_numerical = add_noise_numerical(X_numerical, 50, 0.1)

# combine noisy features with original features
df_noisy = pd.DataFrame(X_noisy_categorical, columns=["cat_feat"])
df_noisy[numerical_cols] = X_noisy_numerical

print(df.head())
print(df_noisy.head())

# check if the shapes are the same
print(df.shape)
print(df_noisy.shape)


'''
> df
   num_feat1  num_feat2  cat_feat
0          1          5         0
1          2          6         1
2          3          7         2
3          4          8         3
> df_noisy
   cat_feat  num_feat1  num_feat2
0         0          1          5
1         2          2          6
2         1          3          7
3         3          4          8
'''

# split into train and test sets for df 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.drop("cat_feat", axis=1), df["cat_feat"], test_size=0.2, random_state=42)
# split into train and test sets for df_noisy
X_train_noisy, X_test_noisy, y_train_noisy, y_test_noisy = train_test_split(df_noisy.drop("cat_feat", axis=1), df_noisy["cat_feat"], test_size=0.2, random_state=42)

# train a model on df
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
print(rf.score(X_test, y_test))

# train a model on df_noisy
rf_noisy = RandomForestClassifier(random_state=42)
rf_noisy.fit(X_train_noisy, y_train_noisy)
print(rf_noisy.score(X_test_noisy, y_test_noisy))

