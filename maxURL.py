"""
design a data structure to store web browser history：

requirements:
1. the data structure need to store "date" and "url"
2. the data structure need to return the URL with the most click on specific 
date

dict { "date" : heap}

"""
import operator
class urlRecorder:

    def __init__(self, histories):

        self.dateToURL = {}  
        self.dateToMaxURL = {}
        self.histories = histories

        self.__buildDateToURL__()
        self.__buildDateToMaxURL__()

    def __buildDateToURL__(self):

        for item in self.histories:
            date = item[0]
            url = item[1]

            if not date in self.dateToURL:
                self.dateToURL[date] = {url : 1}
            else:
                if not url in self.dateToURL[date]:
                    self.dateToURL[date][url] = 1
                else:
                    count = self.dateToURL[date][url]
                    self.dateToURL[date][url] = count + 1

    def __buildDateToMaxURL__(self):

        for date, urlList in self.dateToURL.items():
            l = sorted(urlList.items(), key = operator.itemgetter(1), reverse = True)
            print("l=",l)
            self.dateToMaxURL[date] = l[0][0]

histories = [[1 , "www.123.com"],[ 2 , "www.234.com"], [2 ,"www.234.com"],[2, "www.134.com"],[2, "www.234.com"],[4,"www.334.com"]]
a = urlRecorder(histories)

print("history=",histories)
print("date to url=",a.dateToURL)
print("date to max url = ",a.dateToMaxURL)



        



    

