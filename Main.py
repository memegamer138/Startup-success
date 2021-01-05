#Shakthi
#12-A
from time import sleep
import os
import webbrowser as web
print('Welcome to my program!')
sleep(1)
print('This program will be useful for those who are planning to create a start-up.')
sleep(1.5)
print("I will first ask you some questions based on your plans and resources.")
sleep(1)
print('''
So I will ask you what kind of business you want to start. The following is a detailed explanation of the types
you can enter:

Service- It includes businesses that provide any particular service to the general public. It ranges from services
like Operating systems, applications to public transport, e.t.c

Trade- It includes the purchase and selling of stock from any corporates

Restaurant- As the name suggests, it means starting a restaurant.
''')
sleep(12)
while True:
    typ=input("Firstly, what kind of business do you want to create?(service, trade, restaurant): ")
    if typ!='service' and typ!='trade' and typ!='restaurant':
        print("Invalid input. Please only enter from service,trade or restaurant.")
    else:
        break
with open('userdat.txt','a') as file:
    file.write('Your business type: ')
    file.write(typ)
    file.write('\n\n')
    file.close()
# Code for 'service' business begins
success=50
def service_val_check():
    global success
    service_val=input("Do you think your service has a lot of demand in the area where you plan to serve?(yes or no): ")
    while True:
        if service_val=='yes':
            success+=10
            break
        elif service_val=='no':
            success-=5
            break
        else:
            print("Please enter a valid answer! Answer should be 'yes' or 'no'.")
            service_val_check()
    if service_val=='yes':
        with open('userdat.txt','a') as file:
            file.write("Your service has a lot of demand in the area you are planning to serve.")
            file.write('\n\n')
            file.close()
        with open("service.txt",'a') as f:
            f.write('''
It was recorded that the area where you are planning has a lot of demand for your service. A high
requirement of your service is the first step towards a successful start-up. But be wary because a
high demand means a high possibility of encountering high competition. So it is recommended to stand
out from other competition by providing a unique experience to your customers.''')
            f.write('\n\n')
    elif service_val=='no':
        with open('userdat.txt','a') as file:
            file.write("Your service doesn't have a lot of demand in the area you are planning to serve.")
            file.write('\n\n')
            file.close()
        with open("service.txt",'a') as f:
            f.write('''
It was recorded there isn't much demand for your service in that area. It is recommended to establish
your business in an area where there is a high demand, so consider shifting your starting area. Later,
when your business develops significantly, you can spread your services to other areas, and
if possible, new countries. This will lead to a significant boost in your popularity.''')
            f.write('\n\n')
            f.close()
def service_capital_check():
    global success
    ch=input('''
Is your service something that requires a strong workforce, or is it a purely online service?
Example for online service are online classes, software development,e.t.c.
Please enter 'yes' if it requires a strong workforce, 'no' if it is an online service: ''')
    service_cap=int(input("Please enter the total amount of capital you have reserved for starting your service in USD: "))
    if ch=='yes':
        if service_cap<60000:
            success-=15
        elif service_cap<80000 and service_cap>=60000:
            success-=10
        elif service_cap>=80000 and service_cap<=125000:
            success+=0
        elif service_cap>125000 and service_cap<=200000:
            success+=10
        elif service_cap>200000:
            success+=15
        with open('userdat.txt','a') as file:
            file.write("Your service requires a strong workforce.")
            file.write('\n\n')
            file.close()
        if service_cap<100000:
            with open('service.txt','a') as f:
                f.write('''
It was recorded that yout total capital was below 100,000 USD. Capital is one of the most, if
not the biggest deciding factor of the success of any business. After a few calculations, I came
to a conclusion that for a service start-up, one will need 80,000 USD at a minimum, while the
recommended is above 100,000USD. So before starting, I strongly recommend you try to gather more
capital. If you wish to predict the accurate capital requirement, I suggest you visit the website below:
https://www.profitableventure.com/cost-start-a-staffing-agency/

Also I highly recommend you check out this following website:
https://smartbusinessplan.com/glossary/capital-requirements/''')
                f.write('\n')
                f.close()
        if service_cap>100000:
            with open('service.txt','a') as f:
                f.write('''
It was recorded that yout total capital was above 100,000 USD. This is a very good start as capital is one 
of the most, if not the biggest deciding factor of the success of any business. After a few calculations, 
I came to a conclusion that for a service start-up, one will need 80,000 USD at a minimum, while the recommended
is above 100,000USD. If you wish to predict the accurate capital needs, I suggest you visit the website below:
https://www.profitableventure.com/cost-start-a-staffing-agency/

Also I highly recommend you check out this following website:
https://smartbusinessplan.com/glossary/capital-requirements/''')
                f.write('\n')
                f.close()
    if ch=='no':
        if service_cap<40000:
            success-=10
        elif service_cap>=40000 and service_cap<65000:
            success-=5
        elif service_cap>=65000 and service_cap<=110000:
            success+=0
        elif service_cap>111000 and service_cap<=185000:
            success+=5
        else:
            success+=10
        if service_cap<80000:
            with open("service.txt",'a') as f:
                f.write('''
It was recorded that yout total capital was below 80,000 USD. Capital is one of the most, if
not the biggest deciding factor of the success of any business. After a few calculations, I came
to a conclusion that for a online service start-up, one will need 65,000 USD at a minimum, while the
recommended is above 80,000USD. So before starting, I strongly recommend you try to gather more
capital. If you wish to predict the accurate capital requirement, I suggest you visit the website below:
https://www.profitableventure.com/cost-start-a-staffing-agency/

Also I highly reccomend you check out this following website:
https://smartbusinessplan.com/glossary/capital-requirements/''')
                f.write('\n\n')
                f.close()
        elif service_cap>100000:
            with open('service.txt','a') as f:
                f.write('''
It was recorded that yout total capital was above 100,000 USD. This is a very good start as capital is one 
of the most, if not the biggest deciding factor of the success of any business. After a few calculations, 
I came to a conclusion that for a service start-up, one will need 80,000 USD at a minimum, while the recommended
is above 100,000USD. If you wish to predict the accurate capital needs, I suggest you visit the website below:
https://www.profitableventure.com/cost-start-a-staffing-agency/

Also I highly reccomend you check out this following website:
https://smartbusinessplan.com/glossary/capital-requirements/''')
                f.write('\n\n')
                f.close()
        with open('userdat.txt','a') as file:
            file.write("Your service is purely online.")
            file.write('\n\n')
            file.close()
    with open('userdat.txt','a') as file:
        file.write("Total capital for startup: ")
        file.write(str(service_cap))
        file.write('\n\n')
        file.close()

def service_contact():
    global success
    while True:
        check=input("Do you have any contacts or partners to spread word and help you in your business?(yes or no): ")
        if check=='yes':
            cont=int(input("Please enter how many people: "))
            if cont>5:
                success+=5
            else:
                success+=cont
            with open('userdat.txt','a') as file:
                file.write("Total number of partner/contacts availabe: ")
                file.write(str(cont))
                file.write('\n\n')
            with open("service.txt",'a') as f:
                f.write("It was recorded that you have ")
                f.write(str(cont))
                f.write(''' contacts to help you out. With more partners, you can share expenses for starting, but after
your service has been established, you will also need to share the profits equally. Also having contacts,
or people whom you trust, you can gain a substantial boost in popularity as they might spread the word about 
your service.''')
                f.write("\n\n")
                f.close()
            break   

        elif check=='no':
            print("Alright, but it is recommended to have trustworthy people to help you.")
            success-=5
            with open('userdat.txt','a') as file:
                file.write("You have no available partners/contacts.")
                file.write('\n\n')
            with open("service.txt",'a') as f:  
                f.write('''
It was recorded that you do not have any contacts to help you establish your service. Note that having a good relation
with the right people can give you an extreme boost in sales and in popularity as well. So I highly recommend you to
mingle with entrepreneurs, attend their seminars and get yourself known in the marketing world.''')
                f.write('\n\n')
                f.close()
            break
        else:
            print("Please enter a valid response! (yes or no)")

if typ=='service':
    success=60
    with open("service.txt",'w') as f:
        f.write('A few tips before establishing your start-up:')
        f.write('\n')
        f.close()
    service_val_check()
    service_capital_check()
    service_contact()
    with open("service.txt",'a') as f:
        f.write('Your business has a success chance of ')
        f.write(str(success))
        f.write('%.')
        f.write('\n')
        f.close()

# Code for 'service' business ends.

# Code for 'trade' business begins.
def trade_capcheck():
    global success
    trade_cap=int(input("Please enter the amount of capital you have prepared to invest in trading (in USD): "))
    if trade_cap<30000:
        print("You need a minimum of 30,000$ to create a sustainable trade. So please gather more capital.")
        success-=5
    elif trade_cap>=30000 and trade_cap<=40000:
        success+=5
    elif trade_cap>40000 and trade_cap<=50000:
        success+=10
    elif trade_cap>50000 and trade_cap<=60000:
        success+=15
    else:
        success+=20
    with open('trade.txt','a') as f:
        f.write('''
Trading is a pretty risky business where you need to know when to quit on buying more and also to know
how much to sell at a given time. I highly recommend you to always take note of the change in the stock prices
and to also have multiple softwares to predict future stock prices. Also try to keep the loss factor below 1'%' of
your total capital. For example if you have an amount of 50,000$ in your trading account, do not spend more
than 500 dollars on a single stock at one time.''')
        f.write('\n')
        f.close()
    with open('userdat.txt','a') as file:
        file.write("Total capital: ")
        file.write(str(trade_cap))
        file.write('\n\n')
def trade_knowledge():
    global success
    while True:
        ch=input('''
Many people spend huge sums in trading without having a proper knowledge of what they are doing, resulting
in major losses. So do you have a clear intention of why you are getting into trading and do you have a good
knowledge about how trading works? (Please be honest): ''')
        if ch=='no':
            success-=5
            with open('trade.txt','a') as f:
                f.write('''
It was recorded that you don't have a good knowledge of how trading works. It is necessary to know what you are
doing. I highly recommend you buy books and watch videos on how the market works and also have a few contacts to 
know what is happening inside the companies of which you are a share holder.''')
                f.write('\n')
                f.close()
            with open('userdat.txt','a') as file:
                file.write("You don't have a good knowledge of how trading works." )
                file.write('\n\n')
                file.close()
            break
        elif ch=='yes':
            success+=5
            with open('trade.txt','a') as f:
                f.write('''
It was recorded that you have a good knowledge of how trading works. This is very good as you will have a good idea 
of when to sell/buy stocks. I also recommend to have a few contacts to know the profits gained by companies of which 
you are a shareholder so that you know if you need to sell or buy stock at a given time.''')
                f.write('\n')
                f.close()
            with open('userdat.txt','a') as file:
                file.write("You have a good knowledge about how trading works.")
                file.write('\n\n')
                file.close()
            break
        else:
            print("Please enter only yes or no.")

def trade_contacts():
    global success
    while True:
        ch=input("Do you have anyone who can give you an inside knowledge about the companies of which you are a shareholder?: ")
        if ch=='yes':
            with open('userdat.txt','a') as file:
                file.write('You have contacts to get inside information about companies.')
                file.write('\n\n')
                file.close()
            success+=5
            with open('trade.txt','a') as f:
                f.write('''
It was recorded that you have people who can get you detailed information about companies. It is always good to 
know about how the companies' profit is going, so that you know when to sell/buy stock. Some people might consider
this as industrial espionage, but I consider it as proactive thinking. But if you are planning on having people to
give you inside information, don't forget to have a good lawyer on your side to always stay on the safer side of the law.''')
                f.write("\n")
                f.close()
            break
        elif ch=='no':
            with open('userdat.txt','a') as file:
                file.write("You don't have contacts to get inside information about companies.")
                file.write('\n')
                file.close()
            success-=2
            with open('trade.txt','a') as f:
                f.write('''
While having insider knowledge is not necessary, it will help you a lot about when you need to sell/buy stock from
the company. This will help a lot in minimizing risky purchases and to ensure your profiit. But if you are planning
on having people to give you inside information, don't forget to have a good lawyer on your side to always stay on the
safer side of the law.''')
                f.write("\n")
                f.close()
            break
        else:
            print("Please enter yes or no only.")
            print()

if typ=='trade':
    success=50
    with open("trade.txt",'w') as f:
        f.write('A few tips before establishing your start-up:')
        f.write('\n')
        f.close()
    trade_capcheck()
    trade_contacts()
    trade_knowledge()
    with open("trade.txt",'a') as f:
        f.write('\n')
        f.write('Your business has a success chance of ')
        f.write(str(success))
        f.write('%.')
        f.write('\n')
        f.close()
# End of code for Trade

# Beginning of code for Restaurant
def restaurant_capcheck():
    global success
    cap=int(input("Enter the amount of capital you have reserved (in USD): "))
    if cap<150000:
        print('''Please note that you will need a minimum of 180,000 USD to start a most basic restaurant. So please try to 
increase your capital.''')
        with open("restaurant.txt",'a') as f:
            f.write('''
It was recorded that you have a capital less than 180,000 USD. Please note that you will need a minimum of 180,000 USD
to start a most basic restaurant. So please try to increase your starting capital. I tshould also be noted that you will
have to pay for the maintenance of your restaurant too. I highly recommend that you visit the following website so that
you have a clear knowledge of the expenditures, both for starting and for maintenance: 
https://www.sage.com/en-us/accounting-software/startup-costs/restaurant/ 
''')
        success-=10
    elif cap>=150000 and cap<200000:
        success-=5
        with open('restaurant.txt','a') as f:
            f.write("It was recorded that you have a capital of ")
            f.write(str(cap))
            f.write('''
While this amount is above the minimum of 180,000 USD, please note that the reccomended amount is above 200,000. So try to gain a bit more
capital to ensure a successful start-up. I highly recommend that you visit the following website so that you have a 
clear knowledge of the expenditures, both for starting and for maintenance:
https://www.sage.com/en-us/accounting-software/startup-costs/restaurant/ 
''')
            f.close()
    elif cap>=200000 and cap<250000:
        success+=5
        with open('restaurant.txt','a') as f:
            f.write("It was recorded that you have a capital of ")
            f.write(str(cap))
            f.write(' USD. ')
            f.write('''
This is a good start as the reccomended amount for starting a basic restaurant is above 200,000 USD. To get a more 
detailed and accurate information about your capital and maintenance costs, I highly recommend that you visit the 
following website so that you have a clear knowledge of the expenditures, both for starting and for maintenance:
https://www.sage.com/en-us/accounting-software/startup-costs/restaurant/ 
''')
            f.close()
    elif cap>=250000 and cap<300000:
        success+=10
        with open('restaurant.txt','a') as f:
            f.write("It was recorded that you have a capital of ")
            f.write(str(cap))
            f.write(' USD. ')
            f.write('''
This is a great start as the reccomended amount for starting a basic restaurant is above 200,000 USD. To get a more 
detailed and accurate information about your capital and maintenance costs, I highly recommend that you visit the 
following website so that you have a clear knowledge of the expenditures, both for starting and for maintenance:
https://www.sage.com/en-us/accounting-software/startup-costs/restaurant/ 
''')
            f.close()
    else:
        success+=15
        with open('restaurant.txt','a') as f:
            f.write("It was recorded that you have a capital of ")
            f.write(str(cap))
            f.write(' USD. ')
            f.write('''
This is a great start as the reccomended amount for starting a basic restaurant is above 200,000 USD. To get a more 
detailed and accurate information about your capital and maintenance costs, I highly recommend that you visit the 
following website so that you have a clear knowledge of the expenditures, both for starting and for maintenance:
https://www.sage.com/en-us/accounting-software/startup-costs/restaurant/ 
''')
            f.close()
    with open('userdat.txt','a') as f:
        f.write("You have a total startup of: ")
        f.write(str(cap))
        f.write(' USD. ')
        f.write('\n\n')
def restaurant_valcheck():
    global success
    while True:
        ch=input("Do you think there are a lot of restaurants in the area where you begin to start yours? (yes or no): ")
        if ch=='yes' or ch=='no':
            break
        else:
            print("Please enter a valid response.")

    if ch=='yes':
        success-=2
        with open('restaurant.txt','a') as f:
            f.write('''
It was recorded that there are many restaurants in the area you are planning to start a restaurant. This is usually
not a very big factor of success, but you should expect a lot of competition. So it is highly reccomended to have
unique styles and ideas for your restaurnt. After a successful establishment, if things go well, you can even plan
on creating multiple branches in different places to expand your business.''') 
            f.close()
        with open('userdat.txt','a') as f:
            f.write("There are many restaurants in the area that you are planning to start a restaurant")
            f.write('\n\n')
    else:
        success+=3
        with open('restaurant.txt','a') as f:
            f.write('''
It was recorded that there aren't many restaurants in the area you are planning to start a restaurant. This is usually
not a very big factor of success, but starting a restaurant in that area, there is a good chance that with a good idea,
you can easily gain the peoples' attention. So it is highly reccomended to have unique styles and ideas for your restaurnt.
After a successful establishment, if things go well, you can even plan on creating multiple branches in different places to 
expand your business.''') 
            f.close()

def restaurant_ideacheck():
    global success
    while True:
        ch=input("Do you have any unique idea for your restaurant to make yourself stand out from other competition? (yes or no): ")
        if ch=='yes' or ch=='no':
            break
        else:
            print("Please enter a valid response.")
    if ch=='yes':
        success+=5
        with open("restaurant.txt",'a') as f:
            f.write('\n')
            f.write(r'''
It was recorded that you have unique ideas for your restaurant. A unique idea/theme is essential for any restaurants, 
especially when there is heavy competition. This might also improve customer experience, which in turn will ensure
a maximized profit.''')
            f.close()
        with open('userdat.txt','a') as f:
            f.write("You have unique ideas for your restaurant to make yourself stand out from other competition.")
            f.write('\n')
            f.close()
    else:
        success-=5
        with open("restaurant.txt",'a') as f:
            f.write('\n')
            f.write(r'''
It was recorded that you don't have unique ideas for your restaurant. A unique idea/theme is essential for any restaurants, 
especially when there is heavy competition. This might also improve customer experience, which in turn will ensure
a maximized profit.''')
        f.close()
        with open('userdat.txt','a') as f:
            f.write("You don't have unique ideas for your restaurant to make yourself stand out from other competition.")
            f.close()
if typ=='restaurant':
    success=50
    with open("restaurant.txt",'w') as f:
        f.write('A few tips before establishing your start-up:')
        f.write('\n\n')
        f.close()
    restaurant_capcheck()
    restaurant_valcheck()
    restaurant_ideacheck()
    with open("restaurant.txt",'a') as f:
        f.write('\n')
        f.write('Your business has a success chance of ')
        f.write(str(success))
        f.write('%.')
        f.write('\n')
        f.close()
# Code for restaurant ends
# End code begins
sleep(2)
print("Your response has been recorded and the results are compiled. Thank you very much for using my program.")
sleep(3)
while True:
    ch=int(input('''
You now have the following options:
1. View your responses.
2. View your results.
3. View the current directory.
4. Visit the home page for SSP.
5. Exit
Note that the files will still exist in the current directory even after the program is closed. 
Please enter the corresponding number to what you need: '''))
    if ch==1:
        web.open('userdat.txt')
    elif ch==2:
        if typ=='service':
            web.open('service.txt')
        elif typ=='trade':
            web.open('trade.txt')
        else:
            web.open('restaurant.txt')
    elif ch==3:
        print(os.getcwd())
    elif ch==4:
        web.open("WebPages/Home.html")
    elif ch==5:
        break
    else:
        print("Invalid response.")
    print("-------------------------------------------------------------------------------------------------")
