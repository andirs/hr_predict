# Human Resource: Understanding and predicting why employees leave

## Abstract
Measuring employee satisfaction is a tough and highly complex task. There are a lot of different dimensions in play and turning them into quantifiable format, less to say machine-readable information, can pose a challenge. Information from employee reviews, demographics, balanced scorecards and key performance indicators can offer a first gateway to understanding employee turnover. Modern machine learning algorithms offer tools to leverage this pool of information and extract actionable insights regarding employee behaviour. In this research a model is introduced using supervised and unsupervised algorithms to predict employee turnover. The novelty of the work is in the hybrid approach leveraging both unsupervised and supervised learning results. Based on recent research it was possible to increase the prediction outcome and to introduce a hybrid model that could work as a blueprint for similar tasks in this domain.

## Introduction

According to the [Bureau of Labor Statistics](http://www.bls.gov/news.release/tenure.nr0.htm) the median number of years that wage and salary workers had been with their current employer is 4.2 years \cite{labor1:bls}. While this number varies from industry to industry the story of an employee who sticks with one company for the entirety of a working life seems to be rather antiquated. This observation is combined with economical aspects. Employee turnover has been identified as a key issue for organizations because of its adverse impact on work place productivity and long term growth strategies. One of the key issues with a high employee turnover rate combined with, but reaching beyond, cultural and sociological effects is the cost associated with it. Research shows that the replacement cost for an hourly worker can be as high as 50\% of her annual salary. This number increases with the skill set of the worker up to 200\% for senior-level workers and surges up to 400\% for [executive level positions](www.visier.com/tech-insights/do-predictive-workforce-analytics-actually-work/). It becomes obvious that the trend of shorter tenure in addition to high employee turnover rates can be a costly endeavour. Therefore it becomes increasingly important to acquire the necessary tools for employers to understand where its workforce is standing. Additional insights from employee reports, scorecards as well as general statistical information can offer prediction values for companies when it comes to the longevity of jobs. This research aims to predict the likelihood of an employee quitting her job based on available information. It tries to deliver a hybrid machine learning method to gain actionable insights on how to prevent a high employee turnover. The novel contribution of this research is the usage of a two-layered approach using unsupervised and supervised machine learning algorithms to achieve a higher predictive outcome.

## Research Paper
The complete research paper can be found [here](https://github.com/andirs/hr_prediction/Predicting_Why_Employees_Leave.pdf).

## Code
All code can be found [here](https://github.com/andirs/hr_prediction/Human Resource Prediction.ipynb).

## Dataset
In a dataset published on [kaggle](https://www.kaggle.com/ludobenistant/hr-analytics) we are offered information on current and former employees in concert with key features of their exmployment status. The dataset consists out of almost 15.000 data points and 10 variables.

In order to run the analysis of this research, please follow these quick instructions.

## Files
- *proposal.pdf*: Initial proposal of the project.
- *report.pdf*: Final report of the research.
- *Human Resource Prediction.ipynb*: Contains all code to produce the results in report.pdf

## Frameworks
All code has been written in Python 2.7.12 and has been run on a Jupyter notebook server (4.2.3). 

Frameworks used are

* numpy: For data wrangling. Installing instructions can be found [here](https://docs.scipy.org/doc/numpy/user/install.html)
* pandas: For data wrangling. Installing instructions can be found [here](http://pandas.pydata.org/pandas-docs/stable/install.html)
* seaborn: For plotting. Installing instructions can be found [here](http://seaborn.pydata.org/installing.html)
* bokeh: For plotting. Installing instructions can be found [here](http://bokeh.pydata.org/en/latest/docs/installation.html)
* sklearn: For machine-learning algorithms. Installing instructions can be found [here](http://scikit-learn.org/stable/install.html)