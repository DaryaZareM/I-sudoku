import copy
#get chosen num and place(row and col) return updated domains or False
def forwadChecking(row,col,num,dt,table):
    domainTable = copy.deepcopy(dt)
    for i in range(n):
        while True:
            try:
                domainTable[i][col].remove(num)
            except ValueError:
                break
        while True:
            try:
               domainTable[row][i].remove(num)
            except ValueError:
               break

        if (table[i][col]==0 and len(domainTable[i][col])==0) or (table[row][i]==0 and len(domainTable[row][i])==0):
            return 0
    return domainTable

#get domain table return MRV chosen cell
def MRV(domainTable,table,maxlen):
    mincond=maxlen+1
    mincell=[maxlen+1,0]
    for i in range(n):
        for j in range(n):
            if table[i][j]==0:
                if len(domainTable[i][j])<mincond:
                    mincell=[i,j]
                    mincond=len(domainTable[i][j])
    if mincell[0]==maxlen+1:
        return [maxlen+1,maxlen+1]
    return mincell

def f(table,domainTable,n):
    row,col = MRV(domainTable,table,n)
    if row == n+1:
        # nums filled
        return 1
    
    for assinNum in domainTable[row][col]:
        table[row][col] = assinNum
        updated = forwadChecking(row,col,assinNum,domainTable,table)
        if (updated!=0):
            if f(table,updated,n)!= 0:
                return 1
    table[row][col]=0
    return 0


if __name__=="__main__":
    # n = int(input())
    n=9
    # #initialization
    # numtable = [[0 for i in range(n)] for j in range(n)]
    numdomainTable = [[0 for i in range(n)] for j in range(n)]

    #fill the main table of nums and colors
    # for i in range(n):
    #     s = input().split()
    #     for j in range(n):
    #         if s[j] == '0':
    #             numtable[i][j]=0
    #         else:
    #             numtable[i][j]=int(s[j])

    numtable=[[0, 6, 0, 8, 0, 0, 0, 0, 0],[0, 0, 4, 0, 6, 0, 0, 0, 9],[1, 0, 0, 0, 4, 3, 0, 6, 0],[0, 5, 2, 0, 0, 0, 0, 0, 0],[0, 0, 8, 6, 0, 9, 3, 0, 0],[0, 0, 0, 0, 0, 0, 5, 7, 0],[0, 1, 0, 4, 8, 0, 0, 0, 5],[8, 0, 0, 0, 1, 0, 2, 0, 0],[0, 0, 0, 0, 0, 5, 0, 4, 0]]

    #دامنه
    for i in range(n):
        for j in range(n):
            if numtable[i][j] == 0:
                numdomainTable[i][j]=list(range(1,n+1))
            else:
                numdomainTable[i][j]=[0]

    #سازگار کمان
    for i in range(n):
        for j in range(n):
            if numtable[i][j] != 0:
                for k in range(n):
                    temp = numtable[i][j]
                    while True:
                        try:
                            numdomainTable[i][k].remove(temp)
                        except ValueError:
                            break
                    while True:
                        try:
                            numdomainTable[k][j].remove(temp)
                        except ValueError:
                            break





    f(numtable,numdomainTable,n)
    print(numtable)
