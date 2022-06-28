def directory_coorinate():
    import os
    dir1 = "./1_BEFORE_SPLIT"
    dir2 = "./2_AFTER_SPLIT"
    dir3 = "./3_LASSO_RESULTS"

    if os.path.isdir(dir1) == False:
        os.mkdir(dir1)

    if os.path.isdir(dir2) == False:
        os.mkdir(dir2)

    if os.path.isdir(dir3) == False:
        os.mkdir(dir3)


def data_split_with_ID(data="default_data._withID.csv",ID="ID",fname="defalt_fname.txt"):
    out = open(fname,"a")

    import pandas as pd
    import numpy as np
    import random
    import re
    import os

    id_int_dict = {}
    int_id_dict = {}
    
    data = "./1_BEFORE_SPLIT/"+data
    df = pd.read_csv(data)
    # print(df)

    IDs_array = df.filter(items = [ID,], axis=1)
    # print(IDs_array)
    IDs = []
    for i in list(IDs_array.values.T[0]):
        if i not in IDs:
            IDs.append(i)
    # print(IDs)
    for id in IDs:
        new_int = len(id_int_dict)
        id_int_dict[id] = new_int
        int_id_dict[new_int] = id
    # print(id_int_dict)
    # print(int_id_dict)
    
    n_trainset = int(len(id_int_dict) * 0.7)
    train_int = random.sample(range(len(id_int_dict)), n_trainset)
    # print(train_int)
    train_int = sorted(train_int, reverse=False)
    # print(train_int)
    train_id = []
    for tr_inte in train_int:
        train_id.append(int_id_dict[tr_inte])
    # print(train_id)
    
    test_int = []
    for inte in int_id_dict.keys():
        if inte not in train_int:
            test_int.append(inte)
    # print(test_int)
    test_id = []
    for ts_inte in test_int:
        test_id.append(int_id_dict[ts_inte])
    # print(test_id)
    
    root = re.sub("\.csv","",data)
    root = re.sub("./1_BEFORE_SPLIT/","",root)
    trainfile = r"./2_AFTER_SPLIT/"+ root + "_train.csv"
    testfile = r"./2_AFTER_SPLIT/"+ root + "_test.csv"

    train_df = df[df[ID].isin(train_id)]
    # print(train_df)
    test_df = df[df[ID].isin(test_id)]
    # print(test_df)
    
    if os.path.isfile(trainfile) == False:
        if os.path.isfile(testfile) == False:
            train_df.to_csv(trainfile, header=True, index=False)
            test_df.to_csv(testfile, header=True, index=False)
            print("IDs included in the train set:\n",file=out)
            print(train_id,"\n",file=out)
            print("IDs included in the test set:\n",file=out)
            print(test_id,"\n------",file=out)
    else:
        print("You have already files split. If you wish to split another way, please eliminate existing files:", trainfile, "and",testfile,"\n------",file=out)
        print("You have already files split. If you wish to split another way, please eliminate existing files:", trainfile, "and",testfile,"\n------")

        df_train_already = pd.read_csv(trainfile)
        IDs_train_already_array = df_train_already.filter(items = [ID,], axis=1)
        IDs_train_already = []
        for ii in list(IDs_train_already_array.values.T[0]):
            if ii not in IDs_train_already:
                IDs_train_already.append(ii)
        #IDs_train_already = list(set(IDs_train_already.values.T[0]))
        print("IDs included in the train set:\n",file=out)
        print(IDs_train_already,"\n",file=out)

        df_test_already = pd.read_csv(testfile)
        IDs_test_already_array = df_test_already.filter(items = [ID,], axis=1)
        IDs_test_already = []
        for iii in list(IDs_test_already_array.values.T[0]):
            if iii not in IDs_test_already:
                IDs_test_already.append(iii)
        # IDs_test_already = list(set(IDs_test_already.values.T[0]))
        print("IDs included in the test set:\n",file=out)
        print(IDs_test_already,"\n------",file=out)
    out.close()
    return trainfile, testfile

if __name__ == "__main__":

    directory_coorinate()

    trainfile, testfile = data_split_with_ID(data="demo_lasso_withID.csv" ,ID="ID")
    print("Now processing. Please wait ...\n")
    print("Splitting finished. Please check the following files under the folder 2_AFTER_SPLIT:\n",trainfile,"\n", testfile)
