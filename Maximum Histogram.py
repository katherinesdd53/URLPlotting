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
     maxs = []           #Sets up a list so store max values
     for year in range(1990,2017): #For each year
          years.append(year)       #Add the year to the list
          url = prefix+str(year)+suffix      #Make the url
          M = getTempFromWeb("Max",url)      #Call the function to extract temp
          maxs.append(M) #Add the temp to the list
          print(year, M)
     plt.plot(years, maxs, color='r', label="Max Temp")     #Plot max as red
     plt.title("Maximum Temps for December 6")       #Title for plot
     plt.xlabel('Years')                     #Label for x-axis
     plt.ylabel('Degrees')                   #Label for the y-axis
     plt.legend(loc = 2,fontsize = 'x-small')#Make a legend in upper left corner
     plt.show()

     #Makea a histogram of the maximum temps:
     plt.hist(maxs)
     plt.title("Histogram for Max Temps, December 6, 1990-2017")
     plt.xlabel("Temperatures")
     plt.show()

     print("The list of max values is: ", maxs)

main()