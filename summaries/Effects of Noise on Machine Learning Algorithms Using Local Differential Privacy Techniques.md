# Effects of Noise on Machine Learning Algorithms Using Local Differential Privacy Techniques

Paper [Link](https://ieeexplore.ieee.org/document/9422609)

## Introduction 

The article discusses the potential invasion of privacy through data collection and the use of machine learning algorithms. It also highlights a casein whicha computer scientist was able to match medical records with voter information, demonstrating the need for privacy protection. The concept of differentialprivacy is introduced,a quantifiable measure that provides formalguaranteesthat information is notleaking.Differentially private algorithmscananswer statistical queries approximately without revealing too much about an individual's personal data. Thepaperexploresthemethods for implementing localdifferences inprivacy, such as randomization, the Laplacemethod,and the Exponential Mechanism, to generaterandomresponsesto thefeaturesofmachine learning models.

## Defnition 

The article suggest to use mathematical noise and use randomly generated values as the features for the machine learning algorithms 

### Gaussian random variable 
Probability density function:   
<p align="center">
  <img src="https://latex.codecogs.com/svg.image?p(x)=\frac{1}{\sqrt{2\pi\sigma^2}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}" title="PDF of a Gaussian random variable" />
</p>

where μ is the mean of the distribution and σ is the standard deviation.

### Laplacian Mechanism

The Laplace Distribution (centred at 0) with scale b is the distribution with probability density function:
<p align="center">
  <img src="https://latex.codecogs.com/svg.image?p(x)=\frac{1}{2b}e^{-\frac{|x|}{b}}" title="PDF of a Laplace Distribution" />  
</p>

where |x| is the absolute value of x, and b is the scale parameter that controls the spread of the distribution. 

### Pearson Correlation

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?r_{xy}=\frac{\sum_{i=1}^n(x_i-\bar{x})(y_i-\bar{y})}{\sqrt{\sum_{i=1}^n(x_i-\bar{x})^2}\sqrt{\sum_{i=1}^n(y_i-\bar{y})^2}}" title="Pearson Correlation Coefficient in a Sample" />
</p>

where r_xy is the Pearson correlation coefficient between X and Y, n is the number of observations in the sample, x_i and y_i are the values of X and Y respectively for the i-th observation in the sample, x̄ and ȳ are the sample means of X and Y respectively.

## Methodology

The IBM-Watson Customer Marketing Value dataset was used to explore the impact of randomization and noise on machine learning models. The dataset was preprocessed by converting the 'Engaged' output column into binary values of 1 and 0, and factorizing the categorical variables. Eleven features were selected for randomization, including 'Customer Lifetime Value', 'Education', 'Gender', 'Income', 'Location Code', 'Marital Status', 'Months Since Last Claim', 'Months Since Policy Inception', 'Number of Open Complaints', 'Number of Policies', and 'Sales Channel'.

The randomization process involved adding noise to different columns using a Gaussian noise function, with the method differing depending on whether the feature was categorical or not. For categorical features, a new random value was introduced based on the data, while for non-categorical features, a random sample was taken with a sampling probability of L/N, and noise was added within a specified bound. The machine learning models were then trained both with and without noise.

It highlights the potential of randomization and noise in improving the accuracy and privacy of machine learning models. However, it is important to carefully consider the choice of features and the method of randomization to avoid introducing bias or compromising privacy.


The results showed that there was no significant difference in the accuracy of the logistic regression model when trained on data before and afternoise application. In addition, it has been found that the "LocationCode" feature has the highest Pearson correlation value, which indicates that it has the closest linear relationship to the output variable "Engaged". Multiple machine learning algorithms were used, including random forest classification and K nearest neighbours (KNNs),and accuracy of these models was also similar.

## Conclusion 

The study conducted on the dataset shows that machine learning applications can benefit from differential privacy preservation mechanisms without compromising model accuracy. By carefully adding noise to the data, it was observed that the models trained with and without noise were almost identical. The methodology used  can be applied to other machine learning applications such as targeting customers, marketing funnels, segmentation, churn prediction in ecommerce, communication, retail, and healthcare, to protect the privacy of end user data while preserving personalization. The results of this study highlight the importance of including different privacy techniques and local differences in privacy in machine learning applications to ensure the privacy of end-users.