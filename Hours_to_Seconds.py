#By INNAN Nouhaila
#Compute the number of seconds in a given number of hours, minutes, and seconds.

#For example we will convert 7h21min37s to seconds 
hours = 7
minutes = 21
seconds = 37

# Hours, minutes, and seconds to seconds conversion formula
total_seconds = (hours * 60 + minutes) * 60 + seconds

print(str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds totals to " + str(total_seconds) + " seconds.")
