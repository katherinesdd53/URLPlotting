import matplotlib.pyplot as plt
import urllib
import re

def getTempFromWeb(kind,url):
     page = urllib.request.urlopen(url)
     lines = page.readlines()
     for i in range(len(lines)):
          if lines[i].decode("utf8").find(kind+" Temperature") >= 0:
               m = i
               break
     searchObj = re.search('\d+', lines[m+2].decode("utf8"))
     return int(searchObj.group(0))


def main():
     prefix = "http://www.wunderground.com/history/airport/KLGA/"
     suffix = "/12/06/DailyHistory"
     years = []          #Sets up a list to store years
     maxs = []           #Sets up a list to store max values
     mins = []           #Sets up a list to store min values
     for year in range(1990,2017): #For each year
          years.append(year)       #Add the year to the list
          url = prefix+str(year)+suffix      #Make the url
          MX = getTempFromWeb("Max",url)      #Call the function to extract temp
          MN = getTempFromWeb("Min",url)
          maxs.append(MX) #Add the temp to the list
          mins.append(MN)
          print(year, " MAX: ", MX, " MIN: ", MN)
     plt.plot(years, maxs, color='r', label="Max Temp")     #Plot max as red
     plt.plot(years, mins, color='b', label="Min Temp")     #Plot min as blue
     plt.title("Maximum and Minimum Temps for December 6")       #Title for plot
     plt.xlabel('Years')                     #Label for x-axis
     plt.ylabel('Degrees')                   #Label for the y-axis
     plt.legend(loc = 2,fontsize = 'x-small')#Make a legend in upper left corner
     plt.show()

     #Makea a histogram of the maximum temps:
     plt.hist(maxs)
     plt.hist(mins)
     plt.title("Histogram Temps, December 6, 1990-2017")
     plt.xlabel("Temperatures")
     plt.show()

     print("The list of max values is: ", maxs)
     print("The list of min values is: ", mins)

main()
