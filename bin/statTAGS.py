#!/usr/bin/python3
# -------------
# description : Réalise la statistique des TAGS passé en entrée standard.
#               Le fichier d'entrée est de la forme :
#               #TAGS #tag1 #tag2 #tag3
#               #TAGS #tag1 #tag2 
#               #TAGS #tag1 #tag2 #tag3 #tag4 
# -------------
import sys
if __name__=="__main__":

    tagsCount={}
    kline=0
    for line in sys.stdin:
        if kline == 0 : nbQ=int(line)
        for tag in line.split()[1:]:
            if tag not in tagsCount: 
                tagsCount[tag]=1
            else:
                tagsCount[tag]+=1
        kline+=1
    #print(tagsCount)
    print(37*'-')
    print(f'{"hashtag":<25s}  {"    %":}')
    print(37*'-')
    for k in sorted(tagsCount, key=tagsCount.get,reverse=True):
        print(f'{k:<25s} {(tagsCount[k]/nbQ)*100:>6.2f}% {tagsCount[k]}')

