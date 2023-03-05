# Differential Privacy Made Easy
Paper Link:\
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=10007322&tag=1



## Introduction
Data collection and analysis plays an increasingly large role in the decision-making of various organizations ranging from government agencies to private and public companies. By analyzing data, these organizations are better able to act on their goals whether those goals are providing better services to customers or fair allocation of government resources. However, when such organizations are able to analyze data without restraints they are able to glean private information that otherwise would remain known only by individuals and whomever they trust with the information. There is also the issue that organizations often sell the data that they collect to third-parties, which further reduces the privacy of individuals as their data becomes more widespread. Thus there is naturally a conflict of interest between organizations acting on analyzed data and maintaining the privacy of individuals. Put simply, the problem is how to maximize the privacy of individuals while maintaining the usefullness of aggregated data.\



## Previous Privacy Failures
Although much effort has been put into solving the aforementioned privacy problem, there have inevitably been significant failures on the behalf of various organizations. Many such failures can be attributed to naive approches to privacy implementation which fail to account for the various forms of attacks which could be used to breach an individual's privacy. Robust privacy measures should be developed using the lessons learned from previous data privacy scandals.\
### Insufficiency of Anonymization
Anonymization is generally insufficient in ensuring individual privacy, as it can easily be circumvented by cross-referencing anonymized records with non-anonymized records. In 2006, AOL users fell victim to this insufficiency when AOL released hundreds of thousands of anonymized records without any other privacy measures. The ineptitude of AOL's privacy measures only became known after a New York Times article was published which demonstrated how the data could be reidentified. A similar scandal occured in Massachusetts when an MIT graduate student was able to access the Governor's health records. She gained access to anonymized hospital data and cross-referenced the data with publicly available voter rolls to identify the Governor.

These examples reinforce that anonymization is only one of several steps that organizations should take to protect individual privacy. Once a hostile organization or individual has access to anonymized data, it is only a matter of time until they are able to reidentify various individuals contained in the data.



## Differential Privacy
Within the realm of data analysis, robust privacy measures are generally understood to minimize the ability to learn new information from a dataset when a single entry is removed or ommitted. Put simply, adding or removing a single entry in a database should not have a significant impact on the aggregate statistics of the database. While this definition provides a solid foundation for conceptual understandings of privacy, it does little to enforce such a notion of privacy, especially against bad actors. To address the shortcomings of this definition, Cynthia Dwork established differential privacy as a new framework that would enforce the principles of the pre-existing definition, while shifting the emphasis to the affected individuals. Under Dwork's definition, differential privacy requires that the risk to an individual's privacy does not drastically increase because of their presence in a dataset. This can be enforced by adding noise to datasets which make identification of individuals difficult, but maintain aggregate information. Since the advent of differential privacy in the early 2000s, many researchers have attempted to establish the theoretical capabilities of the framework, as well as its effectiveness in real-world implementations. Statistically, differential privacy is defined as the following:\
$\epsilon$-differential privacy
$$P[M(D1)\in S] \leq e^{\epsilon} \cdot P[M(D2)\in S]$$
$(\epsilon, \delta)$-differential privacy
$$P[M(D1)\in S] \leq e^{\epsilon} \cdot P[M(D2)\in S] + \delta$$
In each of the above definitions, M is a randomized function, equivalent to a search query, while D1 and D2 are datasets which differ by only 1 entry and $\epsilon$ is the privacy coefficient. Under these definitions, differential privacy occurs when the probability of the result of M(D2) is at most $e^{\epsilon}$ times more likely than M(D1). The second definition also includes $\delta$, which is simply the probability of data leakage.

### Noise Mechanisms
There are a variety of mechanisms by which noise can be introduced to a dataset. Each of these mechanisms aim to add plausible deniability for participants of a database, often by generating data according to statistical distributions. Some of the mechanisms include: randomized response, Laplace, Gaussian, and exponential.

#### Randomized Response
Randomized response mechanisms use random outcomes, such as coin flips, to follow a decision tree to determine how an individual's data should be recorded. Noise is introduced by recording forced responses which may or may not reflect the truth about the individual in question. Aggregate information can easily be retrieved by accounting for the expected level of noise introduced.
#### Laplace
Laplace noise mechanisms generate noise according to a Laplace distribution with mean 0 and sensitivity $\frac{GS(f)}{\epsilon}$. As a result, the noise introduced is always at the appropriate level to ensure that aggregate information remains usable. The Laplace mechanism is very popular for $\epsilon$-differential privacy with sensitivity of up to 11.
#### Gaussian
Similar to the Laplace mechanism, the Gaussian mechanism generates noise according to a Gaussian distribution with mean 0. However, such noise only satisfies $(\epsilon, \delta)$-differential privacy, which is generally weaker than $\epsilon$-differential privacy. The Gaussian mechanism also scales with sensitivity of 12.
#### Exponential
Although the Laplace and Gaussian noise mechanisms are effective for numeric data, they do not work otherwise. The exponential mechanism can be applied in such instances, as it assigns probabilities to potential query results. The probabilities scale with the exponenetial function, so accurate answers are substantially more likely to occur, though privacy remains intact because there is no guarantee of the ideal answer. Also unlike the Laplace and Gaussian mechanisms, the exponential mechanism does not add noise to the dataset directly since it only manipulates the query results.
