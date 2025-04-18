# Created by Mahros

# Imports
from src import scrapper as SC

class LinksModel:
  def __init__(self, links):
    self.links = links


  def display(self, tab:str=""):
    print(tab, "Socails(")
    for link in self.links:
      print(tab, "" * 3, link)
      
    print(tab, ")")
    
class PersonModel:
  def __init__(self, name:str, img:str, title:str, links):
    self.name = name
    self.img  = img
    self.title = title
    self.links = links


  def display(self):
    print("Person(")
    print("" * 3, self.name)
    print("" * 3, self.img)
    print("" * 3, self.title)
    self.links.display(tab="  ")
    print(")")

class Almdrasa(SC.Scrapper):
  def __init__(self, verbose:bool=False):
    super().__init__("https://almdrasa.com", verbose=verbose)

  def about_us_persons(self):
    result:PersonModel = []
    response = self.request("/about_us")
    html = self.scrap(response)
    persons = html.findAll("div", attrs={"class":"premium-person-container"})

    # fetch them
    for person in persons:
      result.append(PersonModel(
        name=person.h2.text,
        img=person.img["src"],
        title=person.h4.span.text,
        links=LinksModel([a["href"] for a in person.find("div", attrs={"class", "premium-person-social"}).ul.findAll("a")])
        
      ))
    return result

