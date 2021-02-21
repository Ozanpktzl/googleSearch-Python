import requests

#user search
user_input = input("enter something to search :")
print("geliyor gelmekte olan ....")


#google search
class google_search:
    def __init__(self,name_search):
      self.name = name_search
    def Gsearch(self):
        count = 0
        try :
            from googlesearch import search
        except ImportError:
            print("No Module named 'google' Found")
        for i in search(query=self.name,tld='co.in',lang='en',num=2,stop=10,pause=0): #stop - limits , pause -delay
            count += 1
            print (count)
            print(i)

if __name__=='__main__':
    gs = google_search(user_input)
    gs.Gsearch()