import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from pprint import pprint
import random
import warnings


warnings.filterwarnings("ignore")
# load iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# set random seed for reproducibility
np.random.seed(42)

# function to add Gaussian noise to a feature
def add_noise(X, feature_idx, noise_factor):
    X_noisy = X.copy()
    noise = np.random.normal(scale=noise_factor, size=X.shape[0])
    X_noisy[:, feature_idx] += noise
    return X_noisy
def add_categorical_noise(X, feature_idx, noise_factor):
    feature_values = np.unique(X[:, feature_idx])
    num_values = feature_values.shape[0]
    max_new_values = min(num_values, int(num_values * noise_factor))
    new_value = np.random.randint(num_values, num_values + max_new_values)
    X_noisy = X.copy()
    noisy_indices = np.random.rand(X.shape[0]) < noise_factor
    num_noisy_indices = np.sum(noisy_indices)
    if num_noisy_indices > 0:
        noisy_values = np.random.choice(feature_values, size=num_noisy_indices)
        X_noisy[noisy_indices, feature_idx] = noisy_values
    return X_noisy

# function to add noise to a random feature using add_noise() or add_categorical_noise()
def add_random_noise(X, noise_factor):
    X_noisy = X.copy()
    feature_idx = np.random.randint(X.shape[1])
    if np.unique(X[:, feature_idx]).shape[0] > 2:
        X_noisy = add_categorical_noise(X, feature_idx, noise_factor)
    else:
        X_noisy = add_noise(X, feature_idx, noise_factor)
    return X_noisy

# function to add noise to all features using add_random_noise()
def add_all_noise(X, noise_factor):
    X_noisy = X.copy()
    for feature_idx in range(X.shape[1]):
        X_noisy = add_random_noise(X_noisy, noise_factor)
    return X_noisy
import numpy as np

def calculate_pearson_correlation(X, y):
    # Calculate Pearson correlation coefficient between each feature and target variable
    for i in range(X.shape[1]):
        x_i = X[:, i]
        y_i = y
        n = len(x_i)
        x_bar = np.mean(x_i)
        y_bar = np.mean(y_i)
        numerator = np.sum((x_i - x_bar) * (y_i - y_bar))
        denominator = np.sqrt(np.sum((x_i - x_bar)**2) * np.sum((y_i - y_bar)**2))
        r_xy = numerator / denominator
        print(f"Pearson correlation coefficient between feature {i} and target variable: {r_xy}")


# function to run classification algorithm on original and noisy datasets
def run_classifier(X, y, clf):
    clf.fit(X, y)
    y_pred = clf.predict(X)
    acc = accuracy_score(y, y_pred)
    return acc

noise_dict = {}

# get random noise factor
for i in range(1000):
    noise = random.choice([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
    # add noise to all features 
    X_noisy = add_all_noise(X, noise)
    # run classification algorithms on original and noisy datasets
    clf1 = LogisticRegression(random_state=42)
    acc_noisy1 = run_classifier(X_noisy, y, clf1)
    noise_dict[noise] = acc_noisy1
pprint(noise_dict)