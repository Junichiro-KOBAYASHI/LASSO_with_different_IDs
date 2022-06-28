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

Then, just execute `git clone ○○` on your terminal.

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


## 1_BEFORE_SPLIT
You will find (by default) a file named `demo_lasso_withID.csv` , which was shown on the top of [About](#About)


## 2_AFTER_SPLIT
In this directory, you will find CSV files after being split. File names are automatically arranged (`xxx_train.csv` and `xxx_test.csv`).

## 3_LASSO_RESULTS
The text file named `xxx_output.txt` contains the following information:
- IDs (e.g., author_a, author_b, ...) included in the train/test set
- Your envirioment (version information of the library used)
- Results obtained in the train set
  - Alphas (regularization parameter of LASSO) investigated (in `list` format)
  - The best alpha in terms of AIC (Akaike Information Criterion) (in `float` format)
  - AIC scores recorded with each alpha (in `list` format)
  - The coefficient values recorded in terms of the AIC (in `dictionary` format; key: feature names, value: correponding coefficient value) 
  - The intercept (bias) of the best model in terms of the AIC  (in `float` format)
  - Coefficient path along with each alpha (in `dictionary` format; key: feature names, value: a `list` of coefficient values) 
  - The path of MSEs (mean squared errors) along with alphas investigated (in `list` format)
  - The path of MAEs (mean absolute errors) along with alphas investigated (in `list` format)
  - The path of R^2 scores (coefficient of determination) along with alphas investigated (in `list` format)
- Results obtained in the train set
  - The path of MSEs (mean squared errors) along with alphas investigated (in `list` format)
  - The path of MAEs (mean absolute errors) along with alphas investigated (in `list` format)
  - The path of R^2 scores (coefficient of determination) along with alphas investigated (in `list` format)

The PDF files are the graphs between:
- Alphas (in normal scale) and AICs(`xxx_normalScale.pdf`)
- Alphas (in log scale) and AICs (`xxx_logScale.pdf`)
- Alphas (in normal scale) and coefficients of every feature(`xxx_coefPath.pdf`)
- Alphas (in log scale) and coefficients of every feature(`xxx_coefPath_logScale.pdf`)

:::note warn

These parts are partially owed to [an article of scikit-learn](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html#sphx-glr-auto-examples-linear-model-plot-lasso-model-selection-py), so check it too

:::
z


# Usage
# Technology used
