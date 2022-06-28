# Partially owed to:
# https://scikit-learn.org/stable/auto_examples/linear_model/plot_lasso_model_selection.html#sphx-glr-auto-examples-linear-model-plot-lasso-model-selection-py

"""
sample CSV (demo_lasso_withID.csv) looks like:

ID,feature1,feature2,feature3,feature4,feature5,Year
novelist_a,0.530816464,0.770623465,0.397336556,0.70863908,0.646731069,1880
novelist_a,0.525454129,0.677485059,0.865397932,0.718314741,0.869227219,1890
novelist_a,0.612755896,0.424613168,0.12011501,0.616683455,0.844589893,1900
novelist_b,0.820137273,0.370117628,0.250596817,0.192598386,0.740947226,1880
novelist_b,0.625196124,0.281859486,0.188411299,0.433386745,0.477944204,1890
novelist_b,0.216955246,0.396827362,0.652917988,0.175564506,0.526815876,1900
novelist_c,0.438914776,0.965428635,0.200993806,0.295013145,0.121512433,1880
novelist_c,0.606735654,0.288875545,0.890682131,0.758914839,0.69349809,1890
novelist_c,0.415426214,0.098543267,0.943588808,0.600215128,0.07944195,1900
novelist_d,0.39959745,0.605828163,0.398065823,0.190225126,0.128790398,1880
novelist_d,0.19726494,0.46563675,0.613700705,0.108250745,0.419414697,1890
novelist_d,0.032174537,0.463774774,0.876166235,0.872649821,0.770454856,1900
novelist_e,0.960868485,0.471134139,0.451083401,0.218006756,0.997003797,1880
novelist_e,0.954506727,0.783087589,0.431863861,0.271504534,0.975650397,1890
novelist_e,0.868247454,0.714496046,0.094238285,0.059245352,0.239309615,1900

"""

def AIC_lasso_search(train="default_train.csv",test="default_test.csv", label="Year",ID="ID", pdf="default_output.pdf",fname="defalt_fname.txt"):
    out = open(fname,"a")
    
    import pandas as pd
    import numpy as np
    import sys, os
    from sklearn.linear_model import LassoLarsIC, LassoLars
    from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
    import matplotlib.pyplot as plt
    

    train = "./2_AFTER_SPLIT/"+train
    test = "./2_AFTER_SPLIT/"+test

    df = pd.read_csv(train)
    # print(df)
    
    except_label_ID = "^(?!("+label+"|"+ID+")$)"
    label = "^"+label+"$"

    # print(label, except_label_ID)
    X_train_df = df.filter(regex=except_label_ID, axis=1) # label == "Year"
    # print(X_train_df)
    X_train = X_train_df.values
    # print(X_train)

    y_train_df = df.filter(regex=label, axis=1) # label == "Year"
    # print(y_train_df)
    y = y_train_df.values
    y_train = y.T[0]
    # print(y_train)

    df = pd.read_csv(test)
    # print(df)
    
    X_test_df = df.filter(regex=except_label_ID, axis=1) # label == "Year"
    # print(X_test_df)
    X_test = X_test_df.values
    # print(X_test)

    y_test_df = df.filter(regex=label, axis=1) # label == "Year"
    # print(y_test_df)
    y = y_test_df.values
    y_test = y.T[0]
    # print(y_test)

    lasso = LassoLarsIC(criterion="aic", normalize=False).fit(X_train, y_train)
    print("Your env:\n",file=out)
    ver = sys.version_info
    version = "Python "+str(ver.major)+"."+str(ver.minor)+"."+str(ver.micro)
    print(version,"\n",file=out)
    print("Pandas",pd.__version__,"\n",file=out)
    print("Numpy",np.__version__,"\n",file=out)
    import sklearn, matplotlib
    print("scikit-learn",sklearn.__version__,"\n",file=out)
    print("matplotlib",matplotlib.__version__,"\n------",file=out)

    print("Alphas investigated:\n",file=out)
    print(list(lasso.alphas_),"\n------",file=out)
    print("The best alpha:\n",file=out)
    print(lasso.alpha_,"\n------",file=out)
    print("AICs recorded with each alpha:\n",file=out)
    print(list(lasso.criterion_),"\n------",file=out)

    print("Coefs of the best model:\n",file=out)
    features = list(X_train_df.columns)
    coefs = list(lasso.coef_)
    coef_dict = {}
    for i in range(len(features)):
        coef_dict[features[i]] = coefs[i]
    print(coef_dict,"\n------",file=out)

    print("The intercept of the best model:\n",file=out)
    print(lasso.intercept_,"\n------",file=out)

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

    feature_to_path = {}
    mse_path_train = []
    mae_path_train = []
    r2_path_train = []

    mse_path_test = []
    mae_path_test = []
    r2_path_test = []

    for i in range(len(features)):
        feature_to_path[features[i]] = []

    for al in list(lasso.alphas_):
        lasso2 = LassoLars(alpha=al,normalize=False,fit_path=False).fit(X_train,y_train)
        for i in range(len(features)):
            # print(lasso2.coef_)
            feature_to_path[features[i]].append(list(lasso2.coef_[0])[i])

        y_true_train = y_train
        y_pred_train = lasso2.predict(X_train).T[0]
        
        y_true_test = y_test
        y_pred_test = lasso2.predict(X_test).T[0]
        
        mse_path_train.append(mean_squared_error(y_true_train, y_pred_train))
        mae_path_train.append(mean_absolute_error(y_true_train, y_pred_train))
        r2_path_train.append(r2_score(y_true_train, y_pred_train))

        mse_path_test.append(mean_squared_error(y_true_test, y_pred_test))
        mae_path_test.append(mean_absolute_error(y_true_test, y_pred_test))
        r2_path_test.append(r2_score(y_true_test, y_pred_test))

    print("Coef path along with alphas investigated:\n",file=out)
    print(feature_to_path,"\n------",file=out)
    print("MSE path along with alphas investigated:\n",file=out)
    print(mse_path_train,"\n------",file=out)
    print("MAE path along with alphas investigated:\n",file=out)
    print(mae_path_train,"\n------",file=out)
    print("R^2 score path along with alphas investigated:\n",file=out)
    print(r2_path_train,"\n","="*30,file=out)

    print("Elements below are evaluation scores obtained in the TEST set:\n",file=out)
    print("MSE path along with alphas investigated:\n",file=out)
    print(mse_path_test,"\n------",file=out)
    print("MAE path along with alphas investigated:\n",file=out)
    print(mae_path_test,"\n------",file=out)
    print("R^2 score path along with alphas investigated:\n",file=out)
    print(r2_path_test,"\n------",file=out)

    for i in range(len(features)):
        plt.plot(lasso.alphas_, feature_to_path[features[i]],label=features[i],linewidth=2)
    plt.axvline(lasso.alpha_, linestyle = "--", color = "black", label="best alpha")
    plt.xlabel(r"$\alpha$")
    plt.ylabel("coefs")
    plt.legend()
    plt.title("coefs vs. alphas")
    path_pdf = pdf.removesuffix(".pdf") # Use Python3.9 or higher!
    path_pdf ="./3_LASSO_RESULTS/"+path_pdf+"_coefPath.pdf"
    plt.savefig(path_pdf)
    plt.clf()

    for i in range(len(features)):
        plt.semilogx(lasso.alphas_, feature_to_path[features[i]],label=features[i],linewidth=2)
    plt.axvline(lasso.alpha_, linestyle = "--", color = "black", label="best alpha")
    plt.xlabel(r"$\alpha$")
    plt.ylabel("coefs")
    plt.legend()
    plt.title("coefs vs. alphas")
    path_pdf2 = pdf.removesuffix(".pdf") # Use Python3.9 or higher!
    path_pdf2 ="./3_LASSO_RESULTS/"+path_pdf2+"_coefPath_logScale.pdf"
    plt.savefig(path_pdf2)
    plt.clf()
    
    out.close()

if __name__ == "__main__":
    import os
    old_dir_situation = os.listdir("./3_LASSO_RESULTS/")
    print("Now processing. Please wait ...\n")

    AIC_lasso_search(train="demo_lasso_withID_train.csv",test="demo_lasso_withID_test.csv", label="Year", ID="ID", pdf="demo.pdf")
    
    print("Process finished. Check the files:\n")
    new_dir_situation = os.listdir("./3_LASSO_RESULTS/")
    for fl in new_dir_situation:
        if fl not in old_dir_situation:
            print(fl)
