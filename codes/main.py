import psycopg2
if __name__ == '__main__':
    #fonction de connexion a la base de donnée
    def connecDb():
        connexion = psycopg2.connect(
            host="localhost",
            port=5432,
            database="projetTut",
            user="postgres",
            password="Mamady2011@")
        if connexion :
            print("connexion success")
            return connexion
        else :
            return ("une erreur s'est produite")

conn=connecDb()

#creation de curseur pour la base de deonnée
cur=conn.cursor()

#execution d'une requette
cur.execute("select * from lichens")
#print("Nombre de ligne: ", cur.rowcount)
#print(conn.encoding)
size=15
#Lecture de toutes les lignes
row = cur.fetchmany(size)

#Boucle sur la données
print(row)
for i in row:
    print(i)

#fermeture de la connexion à pg
cur.close


