satr=int(input("\nTedad satrhay mosalase khayam ra vared konid: "))
ans=[[1],[1,1]]
if satr>2:
    for i in range(satr-2):
        ans.append([])
    for i in range(2,satr):
        for j in range(i+1):
            if j==0 or j==i:    ans[i].append(1)
            else:
                ans[i].append(ans[i-1][j-1]+ans[i-1][j])
for i in range(len(ans)):
    print (ans[i])
