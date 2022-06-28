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

The splitting process is based on Python's `random.sample()` function. And the number of unique IDs in the train set is calculated as 

`int((the number of all unique IDs, in this case authors) * 0.7)`


# System requirements and development
As of June 28, 2022, this software is compatible to:

- Python 3.9.1 
- Pandas 1.4.2
- Numpy 1.22.3 
- scikit-learn 1.0.2 
- matplotlib 3.5.1 

In terms of operating systems I have checked:
- Windows 10.0
- Ubuntu 20.04.4 LTS



## Get ready
If you do not have some of the libraries required (shown just above), install them.

Then, just execute `$ git clone https://github.com/Junichiro-KOBAYASHI/LASSO_with_different_IDs.git` on your terminal.

Now, the directories should look like:

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
LASSO_with_different_IDs
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

> **warning**
> Information about date/time (just like `20220628_1159_39` above) is automatically added so that no file causes name duplication.

## logfiles
All your inputs will be automatically recorded into `log.txt`.

# Usage
In general all you have to do is execute `main.py`. But you have got to be aware of the following options:
<pre>
Usage: main.py [options]

Options:
  -h, --help            show this help message and exit
  -d DATA, --data=DATA  CSV data to load. Give a data BEFORE splitting.
                        Default: demo_lasso_withID.csv
  -g GRAPH, --graph=GRAPH
                        Based on your input to -g, PDF files' titles will be
                        arranged. Default: demo (or if you go so far as adding
                        extensions, it causes no problem; demo.pdf
  -i ID, --id=ID        The name of your CSV's column that corresponds to IDs.
                        Default: ID
  -l LABEL, --label=LABEL
                        The name of your CSV's column that corresponds to
                        labels. Default: Year
</pre>

So, if you are to analyze data named `sample01.csv` and would like to get output files (TXT and PDFs) named like `experiment01_coefPath.pdf`, then you have to execute `main.py` the following way:

`$ python main.py -d sample01.csv -g experiment01`

> **warning**
> You have to make sure that the data you wish to analyze (like `sample01.csv`) is located under the directory `1_BEFORE_SPLIT`. 
> Also, in terms of `-i` and `-l`, if the default setting is not functionable for you, check your CSV and find the proper column name:
> In the below, default setting will work properly, based on the corresponding column names
> ![gazou1](https://user-images.githubusercontent.com/108203298/176132942-16a642ce-2cc8-4b25-b971-e755a5e37d12.png)

# Technology used and acknowledgements

As mentioned in [System requirements and development](#system-requirements-and-development), this software is based on the following wonderful libraries:

- Python 3.9.1 
- Pandas 1.4.2
- Numpy 1.22.3 
- scikit-learn 1.0.2 
- matplotlib 3.5.1 

Also, I have to mention that [the article](https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html#sphx-glr-auto-examples-linear-model-plot-lasso-model-selection-py) published by scikit-learn website gave me an inspiration, and the following part of the module `lasso_demo_AIC_plain.py` is (partially) cited from it, so if necessary, please cite it when using this software.
<pre>
plt.plot(
        lasso.alphas_,
        lasso.criterion_,
        color="black",
        label="AIC",
        linewidth=2
    )
    plt.axvline(lasso.alpha_, linestyle = "--", color = "black", label="best alpha")
    plt.xlabel(r"$\alpha$")
    plt.ylabel("AIC")
    plt.legend()
    plt.title("AIC vs. alphas")
    pdf2 = pdf.removesuffix(".pdf")
    pdf2 = "./3_LASSO_RESULTS/"+pdf2+"_normalScale.pdf"
    plt.savefig(pdf2)
    plt.clf()

    plt.semilogx(lasso.alphas_, lasso.criterion_, linestyle = ":")
    plt.plot(
        lasso.alphas_,
        lasso.criterion_,
        color="black",
        label="AIC",
        linewidth=2
    )
    plt.axvline(lasso.alpha_, linestyle = "--", color = "black", label="best alpha")
    plt.xlabel(r"$\alpha$")
    plt.ylabel("AIC")
    plt.legend()
    plt.title("AIC vs. alphas")
    log_pdf = pdf.removesuffix(".pdf") # Use Python3.9 or higher!
    log_pdf = "./3_LASSO_RESULTS/"+log_pdf+"_logScale.pdf"
    plt.savefig(log_pdf)
    plt.clf()
</pre>

# License

This software is distributed under the MIT license. For more details, please visit `LICENSE`.

# Contact
Junichiro KOBAYASHI almathiscenamiisento55dayone@gmail.com


