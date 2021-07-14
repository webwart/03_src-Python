#!/user/  .in Unix only

#  ------------------------------------
#  Porject: LEARN
#   Author: Rainer Warth
#  Version: 28-02-2020
#    Goals: learn how to present calculations.
#      Ref: --
#    Satus: <runs> - <bug (false output , script does not run)> - <broken (link, module, file is missing)> 
#    Satus: runs 
#       >N: -- 
#  ------------------------------------ 

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

def fib(n):
    print(n)
    if n <= 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print("\n")
print(f'This is my fib function {fib(20)}  ')
