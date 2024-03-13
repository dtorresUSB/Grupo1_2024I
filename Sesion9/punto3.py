
def matriz_mult(a,b):
    row_a=len(a)
    col_a=len(a[0])
    row_b=len(b)
    col_b=len(b[0])

    val=0
    #txt=''
    res=[]

    if col_a==row_b:
        for i in range(row_a):
            res.append([])
            for j in range(col_b):
                for k in range(col_a):
                    val+=a[i][k]*b[k][j]
                    #txt+=f'[{i}][{k}]x[{k}][{j}]'
                res[i].append(val)
                val=0
                #print(txt)
                #txt=''
            print(res[i])
    else:
        print('error')


if __name__=="__main__":
    a=[[1,2,2,4],[3,4,-1,1],[2,1,0,2]]
    b=[[0,1],[2,3],[1,2],[0,0]]
    matriz_mult(a,b)

# ----------------- Analisis ---------------
#  i      k      j     i      k      j
#     ---------           ---------
# [0] |[0]*[0]| [0] + [0] |[1]*[1]| [0]
# [0] |[0]*[0]| [1] + [0] |[1]*[1]| [1]
# [1] |[0]*[0]| [0] + [1] |[1]*[1]| [0]
# [1] |[0]*[0]| [1] + [1] |[1]*[1]| [1]
#     ---------           ---------
    
# i= rows_a 
# k= cols_a or rows_b
# j= cols_b