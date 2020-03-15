import requests
from bs4 import BeautifulSoup


class Goog_Search:
    search_base_url = "https://www.google.com/search?q=%s"


    def search_keyword(self, keywords):
        # search_url = self.search_base_url % (keywords.replace(' ', '+'))
        # print(keywords)
        search_url = self.search_base_url % (keywords)
        page_html = requests.get(search_url)
        page_graph = BeautifulSoup(page_html.content,"lxml")
        res=""
        for i in page_graph.find_all('div',{'id':'main'}):
            for j in i.find_all('a'):
                if "/url?q=" in j.get("href"):
                    st=j.get('href')
                    inp=st.find("=")
                    inp1=st.find("&")
                    res=(st[inp+1:inp1])
                    break

        return res

# med = Goog_Search()
# print("Enter search detail")
# inp=input()
# med = med.search_keyword(inp)
# print(med)
# results = rf.scrape_recipe(meat_lasagna)