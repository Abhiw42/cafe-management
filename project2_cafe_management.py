import random
def cafe():
  if a=="order":
    print("Pav Bhaji ------------- rs. 120")
    print("Shake --- rs. 100")
    print("Pizza ------ rs. 250")
    b=(input("")).lower()
    if b=="pav bhaji":
      print("You selected Pav Bhaji")
      dict1["Total"] += 120
      print("bill")
      print("menu")
      c=(input("")).lower()
      if c=="bill":
        dict1["Name"]=input("Enter your name : ")
        bill()
        cafe()
      else:
        print("invalid input")
        cafe()
    elif b=="shake":
      print("You selected Butter scotch shake")
      dict1["Total"] += 100
      print("bill")
      print("menu")
      c=input("").lower()
      if c=="bill":
        dict1["Name"]=input("Enter your name : ")
        bill()
      elif c=="menu":
        cafe()
      else:
        print("invalid input")
        cafe()
    elif b=="pizza":
      print("You selected Farm Fresh PIzza")
      dict1["Total"] += 250
      print("bill")
      print("menu")
      c=(input(""))
      if c=="bill":
        dict1["Name"]=input("Enter your name : ")
        bill()
      elif c=="menu":
        cafe()
      else:
        print("invalid input")
        cafe()
    else:
      print("invalid input")
      cafe()
  elif a=="booking":
    dict1["Name"]=input("Enter your name : ")
    year()
    month()
    date()
    print("\nCongratulations",dict1["Name"],"Your Booking has been confirmed")
    print("Date : ",dict1["date"],"/",dict1["month"],"/",dict1["year"])
    print("Booking Reference id : ",random.randint(100000,999999))
    print("Table no. : ",random.randint(1,20))
  else:
    print("invalid input")
    

def year():
  y=int(input("Enter Year of booking: "))
  if y>=2025:
    dict1["year"]=y
  else:
    print("Invalid Year")
    year()

def month():
  m=int(input("Enter Month of booking i.e 1 - 12 : "))
  if m<=12 and m!=0:
    dict1["month"]=m
  else:
    print("invalid month")
    month()

def bill():
  print("\nCongratulations",dict1["Name"],"Your order has been placed")
  print("Order no.",random.randint(000,999))
  print("Order Total = Rs. ",dict1["Total"])

def date():
  d=int(input("Enter Date : "))
  if d==0:
    print("invalid date")
    date()
  elif dict1["month"] in [1,3,5,7,8,10,12]:
    if d<=31:
      dict1["date"]=d
    else:
      print("Date doesn't exist in the selected month")
      date()
  elif dict1["month"] in [4,6,9,11]:
    if d<=30:
      dict1["date"]=d
    else:
      print("Date doesn't exist in the selected month")
      date()
  elif dict1["month"] ==2:
    if dict1["year"]%400==0:
      if d<=29:
       dict1["date"]=d
    elif dict1["year"]%4==0:
       if d<=29:
        dict1["date"]=d
    elif d<=28:
      dict1["date"]=d
    else:
      print("Date doesn't exist in the selected month")
      date()

  # elif dict1["month"]%2==0 and dict1["month"]<=7 and dict1["month"]!=2:
  #   if d<=30:
  #     dict1["date"]=d
  #   else:
  #     print("Date doesn't exist in the selected month")
  #     date()
  # elif dict1["month"]%2!=0 and dict1["month"]<=7 and dict1["month"]!=2:
  #   if d<=31:
  #     dict1["date"]=d
  #   else:
  #     print("Date doesn't exist in the selected month")
  #     date()
  # elif dict1["month"]%2==0 and dict1["month"]<=7 and dict1["month"]==2:
  #   if dict1["year"]%400==0:
  #     if d<=29:
  #      dict1["date"]=d
  #   elif dict1["year"]%4==0:
  #      if d<=29:
  #       dict1["date"]=d
  #   elif d<=28:
  #     dict1["date"]=d
  #   else:
  #     print("Date doesn't exist in the selected month")
  #     date()
  # elif dict1["month"]%2==0 and dict1["month"]>7:
  #   if d<=31:
  #     dict1["date"]=d
  #   else:
  #     print("Date doesn't exist in the selected month")
  #     date()
  # else:
  #   if d<=30:
  #     dict1["date"]=d
  #   else:
  #     print("Date doesn't exist in the selected month")
  #     date()
print("Welcome to SkillCircle Cafe")
dict1={"Name":"null", "Total": 0,"month":1,"date":1,"year":2025}
print("order")
print("booking")
a=(input(""))
cafe()
