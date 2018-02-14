class actionOBJ:
      date=""
      action=""
      price=""
      tickers=""
      shares=""

def _init_(acdDict):
     self.date=acdDict["date"]
     self.action=acdDict["action"]
     self.price=acdDict["price"]
     self.tickers=acdDict["tickers"]
     self.shares=acdDict["shares"]
#template: 
'''
On 1992-07-14, you have:
    - 500 shares of AAPL at $12.30 per share
    - $0 of dividend income
  Transactions:
    - You bought 500 shares of AAPL at a price of $12.30 per share
'''
#
def  printSelf():
     print("On "+self.date+" you have:\n")
     print("       - "+self.share+" shares of "+self.tickers+" at a price of $"+self.price)

