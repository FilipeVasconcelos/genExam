#!/usr/bin/python3
# -------------
# description : Retourne le code LaTeX pour le tikzpicture d'une question de type
#               appariement (A). Prend une question dans l'entrée standard.
# -------------
import sys
import re
# template tikzpicture first answer
def template_1(G,D,gw="80mm",dw="80mm"):
    GL=G.group(0).split(" ",1)
    DL=D.group(0).split(" ",1)
    print("""
    \\node[text width={4:},align=left] (a1) at (0,0) {{\\textbf{{ {0:} }} {1:} }};
    \\node (b1) at ($(a1.east)+(1,0)$) {{}};
    \\node (c1) at ($(b1.east)+(2,0)$) {{}};
    \\draw[thick,outer sep=8mm] (b1) circle(0.5ex);
    \\draw[thick,outer sep=8mm] (c1) circle(0.5ex);
    \\node[text width={5:},align = right] (d1) at ($(c1.east)+(6,0)$) {{\\textbf{{ {2:} }} {3:} }};""".format(GL[0],GL[1],DL[0],DL[1],gw,dw))
# template tikzpicture for the other answers
def template_2(G,D,N,gw="80mm",dw="80mm"):
    GL=G.group(0).split(" ",1)
    DL=D.group(0).split(" ",1)
    print("""
    \\node[text width={6:},below=0.75cm of a{4:}.center,anchor=center,align=left] (a{5:}) {{\\textbf{{ {0:} }} {1:} }};
    \\node[below=0.75cm of b{4:}.center,anchor=center] (b{5:}) {{}};
    \\node[below=0.75cm of c{4:}.center,anchor=center] (c{5:}) {{}};
    \\draw[thick,outer sep=8mm] (b{5:}) circle(0.5ex);
    \\draw[thick,outer sep=8mm] (c{5:}) circle(0.5ex);
    \\node[below=0.75cm of d{4:}.center,anchor=center,text width={7:},align = right] (d{5:}) {{\\textbf{{ {2:} }} {3:} }};""".format(GL[0],GL[1],DL[0],DL[1],N,N+1,gw,dw))

if __name__=="__main__":

    print("\\indent\\resizebox{\\linewidth}{!}{%")
    print("\\begin{tikzpicture}")
    M1=[]
    M2=[]
    maxm1,maxm2=0,0
    for line in sys.stdin:
        m1 = re.search('(?=[A-Z]\. )(.*)(?=[1-9]\.)', line)
        m2 = re.search('(?=[1-9]\.)(.*)',line)
        if m1 and m2 : 
            M1.append(m1)
            M2.append(m2)
            maxm1=max(maxm1,(len(m1.group(0).split(" ",1)[1])+12)*1.51323)
            maxm2=max(maxm2,(len(m2.group(0).split(" ",1)[1])+12)*1.51323)
    k = 0
    for m1,m2 in zip(M1,M2):
        if k==0 : template_1(m1,m2,str(maxm1)+'mm',str(maxm2)+'mm')
        if k>=1 : template_2(m1,m2,k,str(maxm1)+'mm',str(maxm2)+'mm')
        k+=1
    print("")
    if len(sys.argv) == 2 :
        with open(sys.argv[1],'r') as f:
            print(f.read())
    print("\\end{tikzpicture}")
    print("}%")
