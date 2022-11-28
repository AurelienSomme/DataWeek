from PIL import Image
import numpy as np

# On charge l'image et on la transforme en tableau contenant les couleurs
image_entrée = Image.open("test.jpg")
image = np.asarray(image_entrée)
nb_lignes,nb_colonnes,_ = image.shape

# On crée notre image de sortie sous forme de tableau numpy (ici on fait juste une copie de l'image originale)
image_sortie = image[0:-1,0:-1]

# On sauvegarde les images pour pouvoir les afficher
#Image.fromarray(image).save(r"C:\Users\Bryan\OneDrive\Bureau\Data_Week\Photos test\image_entree.png")
#Image.fromarray(image_sortie).save(r"C:\Users\Bryan\OneDrive\Bureau\Data_Week\Photos test\image_sortie.png")

def split_image():
    iLigne = 0
    num_img = 1
    while iLigne <= nb_lignes :
        iColonne = 0
        while iColonne <= nb_colonnes-1 : 
            Image.fromarray(image[iLigne : iLigne+int(nb_lignes/3), iColonne:iColonne+int(nb_colonnes/2)]).save("image_sortie" + str(num_img) +".png")
            iColonne += int(nb_colonnes/2)
            num_img += 1
        iLigne += int(nb_lignes/3)

split_image()