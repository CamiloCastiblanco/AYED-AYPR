import sys
#El algoritmo dfs fue explicado en clase
def dfs(u):
    global lAdj, vis, par, color
    if len(lAdj) == 0:
        return True
    #print(color,lAdj,u)
    #hayCiclo = False
    res = True
    # marcar al vertice u como vertice visitado
    vis.add(u)
    if u not in color:
        color[u] = "A"
    #print(lAdj[u])
    if u in lAdj:
        for v in lAdj[u]: # por cada uno de los vertices adyacentes a u
            if v in color and color[v] == color[u]:
                return False
            if color[u] == "A":
                color[v] = "B"
            else:
                color[v] = "A"
            if not v in vis: # si no ha sido visitado
                par[v] = u # pongale padre
                res = dfs(v) and res
            #hayCiclo = dfs(v) or hayCiclo
            #haga dfs desde v para buscar otro padre,
            #en cuyo caso habrá un ciclo
            #elif par[u] != v:  # hay ciclo, ya que posee otro padre
                #hayCiclo = True
    else:
        if color[par[u]] == "A":
            color[u] = "B"
        else:
            color[u] = "A"
    return res
def bicolor(n,orden):
    global lAdj
    for i in range(n):
        for j in orden:
            if j[0] == str(i):
                if str(i) in lAdj:
                    lAdj[str(i)] = lAdj[str(i)]+[j[1]]
                else:
                    lAdj[str(i)] = [j[1]]
    res = dfs("0")
    if res:
        return "BICOLORABLE."
    else:
        return "NOT BICOLORABLE."
def main():
    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break
        global vis, par, color,lAdj
        lAdj = {}
        vis = set()#vertices ya vistos
        par = {}#padres
        color = {}
        l = int(sys.stdin.readline().strip())
        orden = []
        for i in range(l):
            orden.append(sys.stdin.readline().strip().split(" "))
        #print(orden,n,l)
        print(bicolor(n,orden))
            
main()
