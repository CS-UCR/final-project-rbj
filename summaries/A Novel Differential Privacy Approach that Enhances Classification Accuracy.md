# A Novel Differential Privacy Approach that Enhances Classification Accuracy

Paper Link:
https://dl.acm.org/doi/10.1145/2948992.2949027

## Introduction
In order to achieve an adequate level of protective privacy for the individuals that share their data for the purpose of research, there must be appropriate layers of privacy that are added in order to ensure this. Data anonymization is pivotal to ensuring that data is not breached and allows for protection against public exposure to private information. Such anonymization is executed through the use of various different algorithms and techniques. There are two different types of frameworks and they are interactive and non-interactive. Non-interactive frameworks carry many advantages over the other and one of the main ones is that a data miner has complete access to the entirety of the data set. Interactive frameworks allow for only a limited amount of access to those that are seeking to use the data. Most typically it is found that the differential privacy method is used in interactive frameworks. This particular article covers the adoption of a non-interactive framework which utilizes an algorithm that fulfills requirements for $\epsilon$-differential privacy. The implementation of this particular approach will be compared with other familiar and existing algorithms for the purpose of anlyzing its efficiency in relation to other techniques. 

## Related Works
The content of this article is concerning the the recent studies found in privacy preserving data publishing and the usability of the said datasets. There are a number of related works in this study that have been produced by different authors and researchers, and the article takes a dive into each of these different techniques and algorithms that have been executed. 

## Proposed System and Experimental Design
The research work presented here is seeking to develop a differentially private PPDP (Privacy Preserving Data Publishing) system. One of the main goals here is to publish usable and secure data for different applications like classification. 

### Privacy Constraint
In models for privacy preservation, there are often cases of problems with table linkage, record linkage, attribute linkage, and probabilistic attacks. The given technique of this article will propose ways to avoid such issues. Specifically with partition-based privacy models, they are able to ensure privacy by enacting syntactic constraints on the output. When drawing information from the dataset, no individual data should be targeted, and the differentially private output should not be associated with any specific record. In this way, differential privacy allows for the given output to produce a certain generalization as if it did not take into consideration a certain individual's data. 

### Definition $e-differential privacy$
$${Pr(An(DB1) = Rs) \over Pr(An(DB2) = Rs)} \leq e^\epsilon$$
$DB1$ and $DB2$ are two datasets that differ in one element. An represents an anonymization algorithm. We consider that $e^\epsilon > 0$ and the lower the value of $\epsilon$ then the stronger the privacy. 

### Laplace Mechanism
The Laplace mechanism is used in order to add noise to the dataset for the purpose of increasing the strength of differential privacy. 
$DB$ is the database used as an input. $f$ is the function. $\lambda$ is representative of the privacy parameter which tells us how much noise should be added. A Laplace distribution with a probabiliy density function looks like this:
$$pdf{x \over \lambda} = {1 \over 2 \lambda} e^-|x|/\lambda$$
Sensitivity of noise is defined with this formula:
$$ \hat{f} (DB) = f(DB) + lap(\lambda)$$
Ultimately, the following formula gives us $e$-differential privacy. 
$$\hat{f}(DB) = f(DB) + lap( {1 \over \epsilon})$$

### Exponential Mechanism
The exponential mechanism is used to handle non-numeric data. The input is a dataset $DB$, output range $\tau$, privacy parameter $\epsilon$, and function $u : (DB x \tau) \rightarrow R$. The sensitivity of the function is given with the following:
$$\Delta u = max_{\Delta_(t, DB, \hat{DB})}|u(DB,t)=(\hat{DB},t)|$$
The probability associated with every output is proportional with 
$$e^{\epsilon u(DB,t) \over 2 \Delta u}$$
The exponential mechanism is commonly used for interactive differential privacy models when it is non-numeric. 

### Anonymization
Data anonymization is used for converting data to a new form in order to increase security of the data and preventing any leaks. Despite a new form of data, the information is still used for processing and analyze for results. The article goes into depth on the generalization approach which implements data anonymization.

Generalization will replace the original values in a dataset for certain attributes with a more general form of the value. General values are decided according to the specific characteristic of the attribute. An example given in the article is the jobs **filmaker** and **singer** are generalized as **artist**. Another example is that the age **30** can be generalized to **30-35**. The definition for generalization is:
Let
$$DB = r_1, r_2, ..., r_n$$
be a set of records. Each record $r_i$ is the information of an individual with attributes
$$A=A_1, A_2, ..., A_d$$
Each attribute $A_i$ has finite domain, denoted by $\Omega (A_i)$. The domain of $DB$ is defined as 
$$\Omega(DB)=\Omega(A_1) \cdot ... \cdot \Omega(A_d)$$

## Problem Statement
The main challenge for PPDP is being able to produce usable data despite undergoing differential privacy approaches to secure privacy of individuals' data. This way any data miners are able to further process and analyze the generalized data. The research of this article seeks to have a balance of both usability and privacy with the data. In order to acheive this, there are two phases:
* Converting micro-data that contains identifiable attributes into anonymous form to meet $\epsilon$-differential privacy.
* Applying the classification algorithm to measure accuracy to check usability of the anonymous data

## Data Set
The data set is pulled from the UCI machine learning repository. The Adult dataset contains 45,222 tuples and it is 5.4MB in size. There are 6 numeric attributes, 8 categorical attributes, and class information to differentiate between incomes of greater and less than 50k.

## Results
| TTd |  $\epsilon$=0.1 |$\epsilon$=0.25 |$\epsilon$=0.5 |$\epsilon$ =1|$\epsilon$=2 |$\epsilon$ =3|$\epsilon$ =4|
| - | - | - | - | - | - | - | - |
| 2 | 76.37	| 75.71 | 76.5 | 75.55 | 75.42 | 75.16 | 75.84|
| 4 | 77.98| 76.74 | 79.14 | 76.09 | 75.62 | 75.45 | 75.4|
| 8 | 77.98 | 80.75 | 80.35 | 77.4 | 78.71 | 76.85 | 78.26|
| 12 | 81.85 | 80.83 | 79.47 | 76.41 | 75.26 | 75.81 | 79.13|
| 16 | 83.28 | 80.85 | 78.48 | 75.09 | 75.29 | 76.02 | 75.25|

The above table shows the results of classification accuracies with the sanitized data from the proposed algorithm. The different tree depths of the Decision Tree are shown with $d$ = 2, 4, 8, 12, 16. At each depth, the values of $\epsilon$ changes from 0.1, 0.25, 0.5, 1, 2, 3, and 4 for the classification accuracy. Each experiment at any given point is done 5 times and the average of the five was taken and listed in the above table. As seen in the table, the algorithm was able to hit 83% accuracy when $\epsilon$ = 0.1. Therefore, highest classification accuracy occurred with the most secure data because the smaller the value of $\epsilon$, the stronger the privacy. 

### Comparisons
When compared to four other algorithms, this algorithm was proven to be much better in performance. $k$-anonymity, $k$-map, $\delta$-Presence, $e,d$-Differential Privacy each had accuracies of 81.16%, 74.91%, 82.9%, and 81.59% respectively. 

## Conclusion
The given algorithm in this paper is a non-interactive data sensitization technique. The usability of the new anonymous data is determined through the classification tests. As seen in the results, the performance of this algorithm is better than other familiar techniques and we can conclude that differential privacy and generalization can work towards providing secure data that is still usable for data miners. 
