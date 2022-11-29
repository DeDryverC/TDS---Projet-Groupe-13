
import xml.etree.ElementTree as ET
class ProjetTDS:
    def __init__(self):
        tree = ET.parse(r'C:\Users\gaeta\Documents\Course_a_pied\Données\435357192.tcx')
        root = tree.getroot()
        numéro=1



        battementMoyenCoureur=[]
        battementMaxCoureur=[]
        battementprécisCoureur=[]
        calories=[]
        coordonnées=[]
        chrono={}

        chronoParJoueur={}
        caloriesParCoureur={}
        coordonnéesParCoureur={}
        vitesseParCoureur={}
        informationsCoureur={}
        informationParCoureur={}
        for section in root:
            for packet in section[0]:
                phrase="Joueur numéro "+str(numéro)


                for information in packet:
                    
                    if"AverageHeartRateBpm" in information.tag:
                        for battement in information:
                            battementMoyenCoureur.append(battement.text)
                    if"MaximumHeartRateBpm" in information.tag:
                        for battement in information:
                            battementMaxCoureur.append(battement.text)
                    if"Calories" in information.tag:
                        for battement in information:
                            calories.append(battement.text)

                    if"Track" in information.tag:
                        for geolocalisation in information:
                            for tempsAltDist in geolocalisation:
                                if "Time" in tempsAltDist.tag:
                                    chronoParJoueur.update({"Temps enregistré":tempsAltDist.text})

                                if "Position" in tempsAltDist.tag:
                                    for latLong in tempsAltDist:
                                        if 'LatitudeDegrees' in latLong.tag:
                                            coordonnées.append(latLong.text)
                                                
                                        if 'LongitudeDegrees' in latLong.tag:
                                            coordonnées.append(latLong.text)
                                        
                                if "HeartRateBpm" in tempsAltDist.tag:
                                    for donneeCardiaque in tempsAltDist:
                                        battementprécisCoureur.append(donneeCardiaque.text)
                                if "Extensions" in tempsAltDist.tag:
                                    for extension in tempsAltDist:
                                        for lx in extension:
                                            print(lx.text)
                                            vitesseParCoureur.update({"Vitesse instantannée : "+str(numéro):lx.text})
                                            print(vitesseParCoureur)

                    if "TotalTimeSeconds" in information.tag:
                        chronoParJoueur.update({"Temps Total":information.text})
                    if "DistanceMeters" in information.tag:
                        chronoParJoueur.update({"Distance Totale":information.text})
                    if "MaximumSpeed" in information.tag:
                        chronoParJoueur.update({"Vitesse maximale":information.text})
                
                chrono.update({phrase:chronoParJoueur})
                
                numéro=int(numéro)
                numéro+=1

           

                

                
                



            
        
ProjetTDS()        

                
        
                




