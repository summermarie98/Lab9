############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.



keepGoing = True

while(keepGoing == True):
    print "What is your temperature?"
    patientsTemp = int(raw_input())
    print "Have you been sick in the last 24 hours?"
    illnessAnswer = raw_input()
    print "Have you recently travelled to West Africa?"
    patientsTravelAnswer = raw_input() 

    if patientsTemp >= 105:
        print "We will need to admit you into the hospital!"
    elif patientsTemp >= 102 and illnessAnswer == "Yes":
        print "We will need to admit you into the hospital!"
    elif patientsTemp >= 100 and illnessAnswer == "Yes" and patientsTravelAnswer == "Yes":
        print "We will need to admit you into the hospital!"
    else:
        print "You are not sick. Thank you for your time!"
    print "Are there any more patients left to be checked?"
    OverallAnswer = raw_input()
    if OverallAnswer == "No":
        keepGoing = False

    