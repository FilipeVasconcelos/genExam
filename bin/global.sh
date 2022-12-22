# -------------
# description : Variables et fonctions globales 
# -------------
RED='\033[0;31m' #Rouge
NC='\033[0m'     #No Color

errorArg(){
    if [ $2 -ne $1 ]
    then 
        echo -e "${RED}Usage : $3 ${NC} $4"
        exit 1
    fi
}

errorFileNotFound(){
    echo -e "${RED}Erreur :${NC} fichier $1 non trouvé"
    exit 1
}
