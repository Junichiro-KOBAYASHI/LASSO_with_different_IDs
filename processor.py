def processor(data, graph_title_base, ID, label,fname):
    import sys, datetime
    sys.path.append(".")

    from mymodules.data_split_with_ID_plain import directory_coorinate, data_split_with_ID
    from mymodules.lasso_demo_AIC_plain import AIC_lasso_search
    import os

    directory_coorinate()

    old_dir_situation = os.listdir("./3_LASSO_RESULTS/")
    
    trainfile, testfile = data_split_with_ID(data=data ,ID=ID,fname=fname)

    print("\nNow processing. Please wait ...\n")
    print("Please check the following files under the folder 2_AFTER_SPLIT:\n",trainfile,"\n", testfile)
    print("\nNow processing. Please wait ...\n")

    root = data.removesuffix(".csv")
    train = root + "_train.csv"
    test = root + "_test.csv"
    AIC_lasso_search(train=train, test=test, label=label, ID=ID, pdf=graph_title_base,fname=fname)
    
    print("Process finished. Check the files:\n")
    new_dir_situation = os.listdir("./3_LASSO_RESULTS/")
    for fl in new_dir_situation:
        if fl not in old_dir_situation:
            print(fl)

    logfile = open("./logfiles/log.txt","a")
    logfile.write("------\n"+str(datetime.datetime.now())+"\n")
    logfile.write("data: "+data+"\n")
    logfile.write("graph_title_base: "+graph_title_base+"\n")
    logfile.write("ID: "+ID+"\n")
    logfile.write("label: "+label+"\n")
    logfile.close()
    