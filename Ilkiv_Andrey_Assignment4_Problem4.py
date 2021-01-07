#Andrey Ilkiv Assignment 4 problem 4 section 01 10/12/2020

#initial user input
userinput = int(input("Please enter the number of seconds elapsed: "))

#loops while user value is not < 0 
while userinput >= 0 :
    #variables set to 0 at the start of each loop
    seconds = 0
    minutes = 0
    hours = 0
    #counts amount of hours and subtracts 1 hour in seconds each time till < 0
    #hours++
    #subtracts 3600 seconds each time
    while (userinput/3600) > 0.999 :
        hours = hours + 1
        userinput = userinput - 3600
    #counts amount of minutes and subtracts 1 minute in seconds each time till < 0
    #minutes++
    #subtracts 60 seconds each time
    while (userinput/60) > 0.999 :
        minutes = minutes + 1
        userinput = userinput - 60
    #counts amount of seconds and subtracts 1 second in seconds each time till < 0
    #seconds++
    #subtracts 1 seconds each time
    while (userinput/1) > 0.999 :
        seconds = seconds + 1
        userinput = userinput - 1
    #checks if a suffix should be added for singular or plural other wise suffix is empty
    if (hours != 1) :
        Hsuffix = "s"
    else:
        Hsuffix = ""
    if (minutes != 1) :
        Msuffix = "s"
    else:
        Msuffix = ""
    if (seconds != 1):
        Ssuffix = "s"
    else:
        Ssuffix = ""
    #print results
    #ask for another input till < 0 is entered
    print(str(hours) + " hour" + Hsuffix + ", " + str(minutes) + " minute" + Msuffix + ", " + str(seconds) + " second" + Ssuffix)
    userinput = int(input("Please enter the number of seconds elapsed: "))
