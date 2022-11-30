
import xml.etree.ElementTree as ET
class ProjetTDS:
    def __init__(self):
        tree = ET.parse(r'C:\Users\gaeta\Documents\Course_a_pied\Données\435357192.tcx')
        root = tree.getroot()
        numéro=0



        battementMoyenCoureur=[]
        battementMaxCoureur=[]
        battementprécisCoureur=[]
        calories=[]
        coordonnées=[]
        tempsInstant=[]
        chronoParJoueur=[]
        vitesseParCoureur=[]
        for section in root:
            for packet in section[0]:
                phrase="Joueur numéro "+str(numéro)


                for information in packet:
                    
                    if"AverageHeartRateBpm" in information.tag:
                        for battement in information:
                            battementMoyenCoureur.append({"Battement moyen "+phrase:battement.text})
                    if"MaximumHeartRateBpm" in information.tag:
                        for battement in information:
                            battementMaxCoureur.append({"Battement max "+phrase:battement.text})
                    if"Calories" in information.tag:
                        for battement in information:
                            calories.append(battement.text)

                    if"Track" in information.tag:
                        for geolocalisation in information:
                            for tempsAltDist in geolocalisation:
                                if "Time" in tempsAltDist.tag:
                                    tempsInstant.append({"Temps enregistré "+phrase:tempsAltDist.text})
                                if "AltitudeMeters"in tempsAltDist.tag:
                                    tempsAltDist.text.strip()
                                    coordonnées.append({"Altitude "+phrase:tempsAltDist.text})
                                if "DistanceMeters"in tempsAltDist.tag:
                                    tempsAltDist.text.strip()
                                    coordonnées.append({"Distance parcourue "+phrase:tempsAltDist.text})
                                if "Position" in tempsAltDist.tag:
                                    for latLong in tempsAltDist:
                                        if 'LatitudeDegrees' in latLong.tag:
                                            coordonnées.append({"Lattitude "+phrase:latLong.text})
                                                
                                        if 'LongitudeDegrees' in latLong.tag:
                                            coordonnées.append({"Longitude "+phrase:latLong.text})
                                        
                                if "HeartRateBpm" in tempsAltDist.tag:
                                    for donneeCardiaque in tempsAltDist:
                                        battementprécisCoureur.append({"Battement inst "+phrase:donneeCardiaque.text})
                                if "Extensions" in tempsAltDist.tag:
                                    for extension in tempsAltDist:
                                        for lx in extension:
                                            vitesseParCoureur.append({"Vitesse inst "+phrase:lx.text})
                    

                    if "TotalTimeSeconds" in information.tag:
                        chronoParJoueur.append({"Temps Total "+phrase:information.text})
                    if "DistanceMeters" in information.tag:
                        chronoParJoueur.append({"Distance Totale "+phrase:information.text})
                    if "MaximumSpeed" in information.tag:
                        chronoParJoueur.append({"Vitesse maximale "+phrase:information.text})
                    if "Calories" in information.tag:
                        calories.append({"Nombre de calories brûlées : "+phrase:information.text})
                numéro=int(numéro)
                numéro+=1
                
        list=[vitesseParCoureur,chronoParJoueur,tempsInstant,coordonnées,battementMaxCoureur,battementMoyenCoureur,battementprécisCoureur,calories]        
        nomchoisi=battementMaxCoureur
        #Plus qu'à remplacer nomchoisi pour piocher la liste désirée   
        for each in list:
            if each==nomchoisi:
                print(each)     
    """
        Affichage des données de manière brute

        
        print(vitesseParCoureur) #Affiche la vitesse instantanée
        print(chronoParJoueur) #Affiche le temps total,distance totale et vitesse  max
        print(tempsInstant) #Affiche l'heure des prises d'échantillons
        print(coordonnées) #Affiche les données relatives à la géolocalisation
        print(battementMaxCoureur) #Affiche les battements max par coureurs 
        print(battementMoyenCoureur) #Affiche les battements moyens des coureurs        
        print(battementprécisCoureur) #Affiche les battements d'un coureur au moment des échantillons
        print(calories) #Affiche les calories brûlées par le coureur au moment des échantillons
    """   
                
                



            
        
ProjetTDS()        

                
        
                




