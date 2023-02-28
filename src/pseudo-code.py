import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def gaussian_noise(data, epsilon):
    # Add Laplacian mechanism to data using Gaussian noise.
    sensitivity = 1 / epsilon
    shape = data.shape
    noise = np.random.normal(scale=sensitivity, size=shape)
    return data + noise

def add_noise_categorical(data, sample_percentage):
    # Add noise to categorical data by introducing a new random value based on data.
    new_data = []
    for feature in data.T:
        if np.all(np.isnan(feature)):
            new_data.append(feature)
            continue
        if np.all(feature == feature[0]):
            new_data.append(feature)
            continue
        if np.any(np.isnan(feature)):
            feature = np.nan_to_num(feature, nan=np.nanmean(feature))
        values, counts = np.unique(feature, return_counts=True)
        if len(values) >= 50:
            new_data.append(feature)
            continue
        for i in range(len(feature)):
            if np.random.rand() < sample_percentage:
                value_counts = list(zip(values, counts))
                value_counts.sort(key=lambda x: x[1])
                value_counts = value_counts[-5:]
                value = np.random.choice([vc[0] for vc in value_counts])
                feature[i] = value
        new_data.append(feature)
    return np.array(new_data).T

def add_noise_numerical(data, sample_percentage, model='logistic_regression'):
    # Add noise to numerical data using Laplacian mechanism and Gaussian noise.    
    new_data = []
    for feature in data.T:
        if np.all(np.isnan(feature)):
            new_data.append(feature)
            continue
        if np.all(feature == feature[0]):
            new_data.append(feature)
            continue
        if np.any(np.isnan(feature)):
            feature = np.nan_to_num(feature, nan=np.nanmean(feature))
        if np.random.rand() < sample_percentage:
            if np.random.rand() < 0.5:
                model = LogisticRegression()
            else:
                model = RandomForestClassifier()
            X = np.delete(data, np.argwhere(data == feature).T[0], axis=1)
            y = feature.copy()
            y[np.isnan(y)] = 0
            y[np.logical_not(np.isnan(y))] = 1
            model.fit(X[~np.isnan(y)], y[~np.isnan(y)])
            predictions = model.predict_proba(X[np.isnan(y)])
            noise = gaussian_noise(predictions[:, 1], 1)
            noise = np.clip(noise, -0.5, 0.5)
            feature[np.isnan(feature)] = model.predict_proba(X[np.isnan(y)])[:, 1] + noise
        new_data.append(feature)
    return np.array(new_data).T
