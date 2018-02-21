##import actions


class actionOBJ:
      date="unknow"
      action="unknow"
      price="unknow"
      ticker="unknow"
      shares="unknow"

      def convert(self,x):
          date=x['date']
          D,T=date.split(" ")
          #print(D)
          #print(T)
          year,month,day=D.split("/")
          self.date=year+"-"+month+"-"+day
          self.action=x['action']
          self.price=x['price']
          self.ticker=x['ticker']
          self.shares=x['shares']
      def  printSelf(self):
           print("On "+self.date+" you have:\n")
           print("       - "+self.shares+" shares of "+self.ticker+" at a price of $"+self.price)

class stockActionOBJ:
       date="unknow"
       dividend="unknow"
       split="unknow"
       stock="unknow"
       def  convert(self,x):
            D=x['date']
            year,month,day=D.split("/")
            self.date=year+"-"+month+"-"+day
            self.dividend=x['dividend']
            self.split=x['split']
            self.stock=x['stock']

       def  printSelf(self):
            print("On "+self.date+"\n")
            print("       - "+self.dividend+"   "+self.split+"    "+self.stock)



class Mytransaction:
    record=[]
      def  actionProcess(x):  # we set a center to process all the transcation
           if x.action='BUY':
                name=x.ticker
                price=x.price
                share=x.shares
                boughtTicker=record['ticker']
                if name not in boughtTicker or not boughtTicker: #means i have this ticker
                         record.append({'ticker':name,'price':price,'share':share})
                else:
                     i=0
                     for t in record:
                         if t['ticker']=name:
                             t['share']


      def  stockActionProcess(y):


      def  printAll():










#template:
'''
On 1992-07-14, you have:
    - 500 shares of AAPL at $12.30 per share
    - $0 of dividend income
  Transactions:
    - You bought 500 shares of AAPL at a price of $12.30 per share
'''
#


#orginal data input:


actions = [{'date': '1992/07/14 11:12:30', 'action': 'BUY', 'price': '12.3', 'ticker': 'AAPL', 'shares': '500'}, {'date': '1992/09/13 11:15:20', 'action': 'SELL', 'price': '15.3', 'ticker': 'AAPL', 'shares': '100'}, {'date': '1992/10/14 15:14:20', 'action': 'BUY', 'price': '20', 'ticker': 'MSFT', 'shares': '300'}, {'date': '1992/10/17 16:14:30', 'action': 'SELL', 'price': '20.2', 'ticker': 'MSFT', 'shares': '200'}, {'date': '1992/10/19 15:14:20', 'action': 'BUY', 'price': '21', 'ticker': 'MSFT', 'shares': '500'}, {'date': '1992/10/23 16:14:30', 'action': 'SELL', 'price': '18.2', 'ticker': 'MSFT', 'shares': '600'}, {'date': '1992/10/25 10:15:20', 'action': 'SELL', 'price': '20.3', 'ticker': 'AAPL', 'shares': '300'}, {'date': '1992/10/25 16:12:10', 'action': 'BUY', 'price': '18.3', 'ticker': 'MSFT', 'shares': '500'}]

stock_actions = [{'date': '1992/08/14', 'dividend': '0.10', 'split': '', 'stock': 'AAPL'}, {'date': '1992/09/01', 'dividend': '', 'split': '3', 'stock': 'AAPL'}, {'date': '1992/10/15', 'dividend': '0.20', 'split': '', 'stock': 'MSFT'},{'date': '1992/10/16', 'dividend': '0.20', 'split': '', 'stock': 'ABC'}]
"""
On 1992-07-14, you have:
    - 500 shares of AAPL at $12.30 per share
    - $0 of dividend income
  Transactions:
    - You bought 500 shares of AAPL at a price of $12.30 per share
On 1992-08-14, you have:
    - 500 shares of AAPL at $12.30 per share
    - $50.00 of dividend income
  Transactions:
    - AAPL paid out $0.10 dividend per share, and you have 500 shares
On 1992-09-01, you have:
    - 1500 shares of AAPL at $4.10 per share
    - $50.00 of dividend income
  Transactions:
    - AAPL split 3 to 1, and you have 1500 shares
On 1992-09-13, you have:
    - 1400 shares of AAPL at $4.10 per share
    - $50.00 of dividend income
  Transactions:
    - You sold 100 shares of AAPL at a price of $15.30 per share for a profit of $1120.00
On 1992-10-14, you have:
    - 1400 shares of AAPL at $4.10 per share
    - 300 shares of MSFT at $20.00 per share
    - $50.00 of dividend income
  Transactions:
    - You bought 300 shares of MSFT at a price of $20.00 per share
On 1992-10-15, you have:
    - 1400 shares of AAPL at $4.10 per share
    - 300 shares of MSFT at $20.00 per share
    - $110.00 of dividend income
  Transactions:
    - MSFT paid out $0.20 dividend per share, and you have 300 shares
On 1992-10-17, you have:
    - 1400 shares of AAPL at $4.10 per share
    - 100 shares of MSFT at $20.00 per share
    - $110.00 of dividend income
  Transactions:
    - You sold 200 shares of MSFT at a price of $20.20 per share for a profit of $40.00
On 1992-10-19, you have:
    - 1400 shares of AAPL at $4.10 per share
    - 600 shares of MSFT at $20.83 per share
    - $110.00 of dividend income
  Transactions:
    - You bought 500 shares of MSFT at a price of $21.00 per share
On 1992-10-23, you have:
    - 1400 shares of AAPL at $4.10 per share
    - $110.00 of dividend income
  Transactions:
    - You sold 600 shares of MSFT at a price of $18.20 per share for a loss of $-1580.00
On 1992-10-25, you have:
    - 1100 shares of AAPL at $4.10 per share
    - 500 shares of MSFT at $18.30 per share
    - $110.00 of dividend income
  Transactions:
    - You sold 300 shares of AAPL at a price of $20.30 per share for a profit of $4860.00
    - You bought 500 shares of MSFT at a price of $18.30 per share
"""




#Lets see what we can do here
#we first convert the actions from List of Dictionary into small piece.


mainSession=Mytransaction()

index=0
for x in actions:
    d=x
    #print d['date']
    i = actionOBJ()
    i.convert(d)
    Mytransaction.actionProcess(i)
    #actionArray[index]=i
    #index=index+1
    #print(i.date)
    #i.setDate(d["date"])
    i.printSelf()
    #print"\n"

print("\n")
index=0
for y in stock_actions:
    s=y
    i=stockActionOBJ()
    i.convert(s)
    Mytransaction.stockActionProcess(i)
    #stockAction[index]=i
    #index=index+1
    i.printSelf()
    #print"\n"

Mytransaction.printAll()
