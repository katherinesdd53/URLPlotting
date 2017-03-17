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
     prefix = "http://www.wunderground.com/history/airport/KLGA/2017/01/"
     suffix = "/DailyHistory"
     days = []
     mins = []           #Sets up a list to store min values
     
     for day in range(1,31): #For each day
          days.append(day)       #Add the year to the list
          url = prefix+str(day)+suffix      #Make the url
          MN = getTempFromWeb("Min",url)
          mins.append(MN)
          baseNum = mins[0]
          scaled = [i*100/baseNum-100 for i in mins]
     
     plt.scatter(days,scaled, s=75)
     plt.title("Minimum Temperatures of January 2017")
     plt.xlabel("Date")
     plt.ylabel("Percent Change")
     plt.show()
     
main()