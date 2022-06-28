# LASSO_with_different_IDs
A software that helps you keep separated different IDs (e.g., AUTHORS_OF_THE_NOVELS) when doing LASSO regression (e.g., whose data label is PUBLICATION_YEAR) and hold-out validation.

<h2>How it works</h2>
This software helps you handle LASSO analysis with such data as:

![table2022](https://user-images.githubusercontent.com/108203298/176083539-db34aff0-d9e8-4f58-8f15-63c2479e8798.png)

Let's assume that the table above is related to novels by five authors (novelist_a - novelist_e). And for each novelist, we have three works, published in 1880, 1890 and 1900. 

If you are to analyze/predict the value of "Year" with LASSO analysis based on hold-out validation, you will face one problem. That is, you should not have the same author both in train and test sets.

For instance, if your train set contains works by novelist_a, then your test set should not contain any of their writings, to make hold-out validation secure.

This software arranges that, having the data split like:



<h2>System requirements</h2>
As of June 28, 2022, this software is compatible to:

- Python 3.9.1 
- Pandas 1.4.2
- Numpy 1.22.3 
- scikit-learn 1.0.2 
- matplotlib 3.5.1 
