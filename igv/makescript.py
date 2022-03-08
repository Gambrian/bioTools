import pandas as pd
import os

os.chdir(r"D:\Desktop\igv")
bwf = os.listdir("./bw")

tmp = "\n".join(["load D:\Desktop\igv\\bw\\" + i for i in bwf])


df = pd.read_table("./TCGA-COAD.DEG.csv",header=0)
df["id"] = df.index
bedDf = pd.read_table("./geneHuman.pseudogene.bed",header= None)
bedDf.columns=["chr","start","end","id","name","line","others"]

conDf = bedDf.merge(df,how="left",on= "id")
candidate = conDf.loc[conDf["log2FoldChange"] >4,["chr","start","end","id"] ]

tmp2  = "\n".join([ "goto chr%s:%s-%s\nsquish\nsort position\n\
setSleepInterval 2000\nsnapshot %s\n"%(row[0],row[1],row[2],row[3]) for index,row in candidate.iterrows()])

src = '''          #这里其实可以先手动设置一些参数，比如groupauto什么的，然后在goto，截图
new
\n
genome hg38
%s
\n
snapshotDirectory D:\Desktop\igv\output
\n
%s
''' %(tmp,tmp2)

with open("D:\Desktop\igv\script.txt","w") as f:
    f.write(src)