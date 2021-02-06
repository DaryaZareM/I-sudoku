import copy


#prototype
def sazegar_konande_yek_cell(row,col,colortable,cdt,numtable,m):
    colordomainTable = copy.deepcopy(cdt)
    temp = colortable[row][col]
    if col>0:
        if numtable[row][col] > numtable[row][col-1]:
            for color in range(1,temp):
                while True:
                    try:
                        colordomainTable[row][col-1].remove(color)
                    except ValueError:
                        break
        else:
            for color in range(temp,m+1):
                while True:
                    try:
                        colordomainTable[row][col-1].remove(color)
                    except ValueError:
                        break

        while True:
                try:
                    colordomainTable[row][col-1].remove(temp)
                except ValueError:
                    break
        if (colortable[row][col-1]==0 and len(colordomainTable[row][col-1])==0) or (colortable[row][col-1]==0 and len(colordomainTable[row][col-1])==0):
            return 0
    if col<n-1:
        if numtable[row][col] > numtable[row][col+1]:
                for color in range(1,temp):
                    while True:
                        try:
                            colordomainTable[row][col+1].remove(color)
                        except ValueError:
                            break
        else:
            for color in range(temp,m+1):
                while True:
                    try:
                        colordomainTable[row][col+1].remove(color)
                    except ValueError:
                        break

        while True:
            try:
                colordomainTable[row][col+1].remove(temp)
            except ValueError:
                break
        if (colortable[row][col+1]==0 and len(colordomainTable[row][col+1])==0) or (colortable[row][col+1]==0 and len(colordomainTable[row][col+1])==0):
            return 0
    if row>0:
        if numtable[row][col] > numtable[row-1][col]:
            for color in range(1,temp):
                while True:
                    try:
                        colordomainTable[row-1][col].remove(color)
                    except ValueError:
                        break
        else:
            for color in range(temp,m+1):
                while True:
                    try:
                        colordomainTable[row-1][col].remove(color)
                    except ValueError:
                        break

        while True:
            try:
                colordomainTable[row-1][col].remove(temp)
            except ValueError:
                break
        if (colortable[row-1][col]==0 and len(colordomainTable[row-1][col])==0) or (colortable[row-1][col]==0 and len(colordomainTable[row-1][col])==0):
            return 0
    if row<n-1:
        if numtable[row][col] > numtable[row+1][col]:
            for color in range(1,temp):
                while True:
                    try:
                        colordomainTable[row+1][col].remove(color)
                    except ValueError:
                        break
        else:
            for color in range(temp,m+1):
                while True:
                    try:
                        colordomainTable[row+1][col].remove(color)
                    except ValueError:
                        break

        while True:
            try:
                colordomainTable[row+1][col].remove(temp)
            except ValueError:
                break
        if (colortable[row+1][col]==0 and len(colordomainTable[row+1][col])==0) or (colortable[row+1][col]==0 and len(colordomainTable[row+1][col])==0):
            return 0
    return colordomainTable
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


def co(table,colortable,colordomainTable,m):
    row,col = MRV(colordomainTable,colortable,m)
    if row == m+1:
        #colors filled
        return 1
    for assinNum in colordomainTable[row][col]:
        colortable[row][col] = assinNum
        updated = sazegar_konande_yek_cell(row,col,colortable,colordomainTable,table,m)
        if (updated!=0):
            if co(table,colortable,updated,m)!= 0:
                return 1
    colortable[row][col]=0
    return 0

def f(table,domainTable,colortable,colordomainTable,m,n):
    row,col = MRV(domainTable,table,n)
    if row == n+1:
        # nums filled
        if co(table,colortable,colordomainTable,m)!= 0:
                return 1
        return 0
    for assinNum in domainTable[row][col]:
        table[row][col] = assinNum
        updated = forwadChecking(row,col,assinNum,domainTable,table)
        if (updated!=0):
            if f(table,updated,colortable,colordomainTable,m,n)!= 0:
                return 1
    table[row][col]=0
    return 0

def sazegar_kaman(row,col,colortable,colordomainTable,numtable):
    temp = colortable[row][col]
    if col>0:
        while True:
                try:
                    colordomainTable[row][col-1].remove(temp)
                except ValueError:
                    break
    if col<n-1:
        while True:
            try:
                colordomainTable[row][col+1].remove(temp)
            except ValueError:
                break
    if row>0:
        while True:
            try:
                colordomainTable[row-1][col].remove(temp)
            except ValueError:
                break
    if row<n-1:
        while True:
            try:
                colordomainTable[row+1][col].remove(temp)
            except ValueError:
                break
    return colordomainTable



if __name__=="__main__":
    m,n = map(int,input().split())
    colors = dict()

    temp=input().split()
    for i in range(m):
        colors[temp[i]]=i+1
    colors['0']=0

    #initialization
    numtable = [[0 for i in range(n)] for j in range(n)]
    numdomainTable = [[0 for i in range(n)] for j in range(n)]

    colortable = [[0 for i in range(n)] for j in range(n)]
    colordomainTable = [[0 for i in range(n)] for j in range(n)]

    #fill the main table of nums and colors
    for i in range(n):
        s = input().split()
        for j in range(n):
            if (s[j][1] == '#'):
                colortable[i][j]=colors['0']
            else:
                colortable[i][j]=colors[s[j][1]]
            if s[j][0] == '*':
                numtable[i][j]=0
            else:
                numtable[i][j]=int(s[j][0])

    #دامنه
    for i in range(n):
        for j in range(n):
            if numtable[i][j] == 0:
                numdomainTable[i][j]=list(range(1,n+1))
            else:
                numdomainTable[i][j]=[0]

    for i in range(n):
        for j in range(n):
            if colortable[i][j] == 0:
                colordomainTable[i][j]=list(range(1,m+1))
            else:
                colordomainTable[i][j]=[0]

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





    #سازگار کمان رنگی
    for i in range(n):
        for j in range(n):
            if colortable[i][j] != 0:
                colordomainTable = sazegar_kaman(i,j,colortable,colordomainTable,numtable)
        
    
    f(numtable,numdomainTable,colortable,colordomainTable,m,n)

    print(numtable)
    print(colortable)