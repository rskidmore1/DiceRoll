import random 
import time  


 
raw_input("gangster: Hi friend, would you like to gamble some of your hard earned coinage")
print "You: ***Nods yes***"
time.sleep(1)
raw_input("gangster: Here you go.")
time.sleep(1)
print "***Hands you the dice***"
time.sleep(1)
print '***You shake your hand and throw the dice***'
time.sleep(1)

def roll(): 
  rand = random.random()

  if rand <= 0.166666667:
    return(1)
  elif rand <= 0.333333334:
    return(2)
  elif rand <= 0.500000001:
    return(3)
  elif rand <= 0.666666668:
    return(4)
  elif rand <= 0.833333335:
    return(5)
  else:
    return(6)

gansterroll = roll()

youroll = roll()

print "Gansters roll was %i" % gansterroll
print "You roll was %i" % youroll


if gansterroll > youroll:
  print("***You hand the gangster the last of your money. He laugh knowing that you will miss your rent.***")
elif gansterroll < youroll:
  print("***Smiles nicely and gives you your winnings.***")
else:
  print("***The clash cause a power ball to expand and consume the ajcent city block.***")



time.sleep(1)

#print "Good job. Let's do this again soon"
