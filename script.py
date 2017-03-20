from setup import *  

b,i=import_years(2014, 2016) 

func_rate=lambda x:"%.2f%%" % (x*100)

#取得列名列表
def cols(dfs):
    columns=list(dfs.popitem()[1].columns)
    for i,x in enumerate(columns):
        print(i,"=>",x)
    return columns

#取得某表的一列数据
def icol(dfs,period,i):    #icol( dataframes, 'yyyy-m', No. of columns name )
    result=dfs[period].iloc[:,i]
    result=result.swaplevel().unstack()
    return result    

def checkcol(dfs, i):
    result=[]
    for k,v in dfs.items():
        result.append("%s=>%s" % (k,v.columns[i]))
    result.sort()
    return result
    
def checkpat(dfs,item_pat):
    result=[]
    def _getitem(df,pat):
        m=False
        pat=re.compile( pat )
        cols=list(df.columns)
        for i in range(len(cols)):
            if pat.search( cols[i] ) is not None:
                return df.columns[i] 
        if m is not True:
            return "No item matches!!!"
    for k,v in dfs.items():
        result.append("%s=>%s" % (k,_getitem(v,item_pat)))
    result.sort()
    return result    
    
#生成比较表
def comp(this,that):     
    #that=that.swaplevel().unstack()
    #this=this.swaplevel().unstack()
    if this.columns[0]<that.columns[0]:
        this,that=that,this
    result=pd.concat([this,that],axis=1)
    result.columns=result.columns.map(str)
    result['incr']=result.iloc[:,0]-result.iloc[:,1]
    result['rate']=result['incr']/result.iloc[:,1]
    result.rate=result.rate.map(func_rate)
    return result
       
    
if __name__=='__main__':
    b,i=import_years(2014, 2016)
    print("Done!")