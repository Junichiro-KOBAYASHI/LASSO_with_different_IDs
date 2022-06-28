import optparse

parser = optparse.OptionParser()

parser.add_option("-d","--data",type="string",help="CSV data to load. Give a data BEFORE splitting. Default: demo_lasso_withID.csv",default="demo_lasso_withID.csv",dest="data")
parser.add_option("-g","--graph",type="string",help="Based on your input to -g, PDF files' titles will be arranged. Default: demo (or if you go so far as adding extensions, it causes no problem; demo.pdf",default="demo",dest="graph")
parser.add_option("-i","--id",type="string",help="The name of your CSV's column that corresponds to IDs. Default: ID",default="ID",dest="id")
parser.add_option("-l","--label",type="string",help="The name of your CSV's column that corresponds to labels. Default: Year",default="Year",dest="label")

options,args = parser.parse_args()
options = eval(str(options))

data = options["data"]
graph_title_base = options["graph"]
ID = options["id"]
label = options["label"]

# -----------------------------
import datetime 
now = datetime.datetime.now()
d = now.strftime("%Y%m%d_%H%M_%S_")
graph_title_base = d+graph_title_base
fname = "./3_LASSO_RESULTS/"+d+"output.txt"

import sys
sys.path.append(".")
from processor import processor
processor(data=data, graph_title_base=graph_title_base, ID=ID, label=label,fname=fname)
