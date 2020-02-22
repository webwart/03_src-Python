# Final account
Pat_Voiture     = 645/3     # 2 pilots et 1 co-pilot 
Lei_Chambre1    = 85.05     # Hotel a Vannes 
Lei_Diner       = 242/4     # Hmmm, Fruit de mer a 4
Rai_Chambre1    = 200.70    # Hotel a Nantes
Rai_Chambre2    = 227.00    # Hotel a Nantes

# Rainer - Leila
RainerFromLeila = Rai_Chambre2 - Lei_Chambre1 - Lei_Diner

# Rainer - Patrick
RainerFromPatrick = Rai_Chambre1 - Pat_Voiture

# Patrick - Leila
PatrickFromLeila = Pat_Voiture - Lei_Chambre1 - Lei_Diner

print("Voila !") 
print("Rainer will receive from Leila {0:.2f} .".format(RainerFromLeila))

print("Rainer will receive from Patrick {0:.2f} .".format(RainerFromPatrick))

print("Patrick will receive from Leila {0:.2f} ." .format(PatrickFromLeila)) 

