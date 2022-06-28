# LASSO_with_different_IDs
A software that helps you keep separated different IDs (e.g., AUTHORS_OF_THE_NOVELS) when doing LASSO regression (e.g., whose data label is PUBLICATION_YEAR) and hold-out validation.

# About
This software helps you handle LASSO analysis with such data as:

![table2022](https://user-images.githubusercontent.com/108203298/176083539-db34aff0-d9e8-4f58-8f15-63c2479e8798.png)

Let's assume that the table above is related to novels by five authors (novelist_a - novelist_e). And for each novelist, we have three works, published in 1880, 1890 and 1900. 

If you are to analyze/predict the value of "Year" with LASSO analysis based on hold-out validation, you will face one problem. That is, you should not have the same author both in train and test sets.

For instance, if your train set contains works by novelist_b, then your test set should not contain any of their writings, to make hold-out validation secure.

This software arranges that, having the data split like:

(Train set: novelist_b, _c and _e)
![table2022_train](https://user-images.githubusercontent.com/108203298/176084789-a6968cf0-e4e3-40ab-8277-5ca8c89e885a.png)


(Test set: novelist _a, and _d)
![table2022_test](https://user-images.githubusercontent.com/108203298/176084984-175dfa26-d8f5-40ee-ab7e-a9a6775d4e45.png)

The splitting process is based on Python's `random.sample()` function. And the proportion of the train set is calculated as 

`int((the number of all IDs, in this case authors) * 0.7)`


# System requirements and development
As of June 28, 2022, this software is compatible to:

- Python 3.9.1 
- Pandas 1.4.2
- Numpy 1.22.3 
- scikit-learn 1.0.2 
- matplotlib 3.5.1 


<h2>Obtain this software</h2>
If you do not have some of the libraries required (shown just above), install them.

Then, just execute `git clone ~~` on your terminal.

Now, the directories should look like:<br>
<pre>
LASSO_with_different_IDs
│  main.py
│  processor.py
│
├─1_BEFORE_SPLIT
│      demo_lasso_withID.csv
│
└─mymodules
        data_split_with_ID_plain.py
        lasso_demo_AIC_plain.py
</pre>

To check the compatibility and arrange an environment, go to the directory you've cloned this and execute the following:

`$ python main.py`

If you have successfully passed this, process the directory will now look like:
<pre>
LASSO_PROJECT_WITH_AUTHOR_ID_TEST
│  main.py
│  processor.py
│
├─1_BEFORE_SPLIT
│      demo_lasso_withID.csv
│
├─2_AFTER_SPLIT
│      demo_lasso_withID_test.csv
│      demo_lasso_withID_train.csv
│
├─3_LASSO_RESULTS
│      20220628_1159_39_demo_coefPath.pdf
│      20220628_1159_39_demo_coefPath_logScale.pdf
│      20220628_1159_39_demo_logScale.pdf
│      20220628_1159_39_demo_normalScale.pdf
│      20220628_1159_39_output.txt
│
├─logfiles
│      log.txt
│
├─mymodules
│  │  data_split_with_ID_plain.py
│  │  lasso_demo_AIC_plain.py
│  │
│  └─__pycache__
│          data_split_with_ID_plain.cpython-39.pyc
│          lasso_demo_AIC_plain.cpython-39.pyc
│
└─__pycache__
        processor.cpython-39.pyc
</pre>

For each of the above, you can find explanations below.


<h2>1_BEFORE_SPLIT</h2>
You will find `demo_lasso_withID.csv` , which is 
        
# Usage
# Technology used
