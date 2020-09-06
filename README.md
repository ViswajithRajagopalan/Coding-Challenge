# ACM Research Coding Challenge (Fall 2020)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using . `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Email the link of your repo to research@acmutd.co with the same email you used to submit your application. Be sure to include your name in the email.

## Question One

![Image of Cluster Plot](ClusterPlot.png)
<br/>
Given the following dataset in `ClusterPlot.csv`, determine the number of clusters by using any clustering algorithm. **You're allowed to use any Python library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file.

## Answer with Explanation:

**The are 2 clusters in the dataset.** I've worked with the pandas and matplotlib python libraries before but had to do additional research on clustering algorithms. After reading [this](https://towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68) article, I settled on the Gaussian Mixture Model (GMM) over K-Mean Clustering. This is because K-Mean Clustering is heavily reliant on the mean values and if the means are too close than it fails to correctly identify the number of clusters. The Gaussian model avoids this by also factoring in standard deviation. I've also worked with Gaussian (Normal) distributions in statistics class so I had some familiarity with how it would operate. Gaussian Mixture Models uses probabilities through Expectation-Maximization to determine the maximum likelihood estimates. A quick glance one could estimate that there are potentially two or three clusters and the Gaussian model confirms that. I read [this](https://towardsdatascience.com/gaussian-mixture-modelling-gmm-833c88587c7f) article and used the sklearn library in python to do the heavy lifting for the calculations. After creating two models for both a 2 and 3 cluster outcome I turned to probability to determine the answer. Looking at sklearns GaussianMixture's [documentation](https://scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html) I used the 'predict_proba' to determine the number of clusters and after analyzing the outcome I determined the number of clusters was 2. 

**Libraries Used:** pandas, sklearn, numpy and matplotlib

**Citations:** 

Seif, George. “The 5 Clustering Algorithms Data Scientists Need to Know.” Medium, Towards Data Science, 14 Sept. 2019, towardsdatascience.com/the-5-clustering-algorithms-data-scientists-need-to-know-a36d136ef68. 

Foley, Daniel. “Gaussian Mixture Modelling (GMM).” Medium, Towards Data Science, 28 Mar. 2019, towardsdatascience.com/gaussian-mixture-modelling-gmm-833c88587c7f. 

“Sklearn.mixture.GaussianMixture¶.” Scikit, scikit-learn.org/stable/modules/generated/sklearn.mixture.GaussianMixture.html. 

