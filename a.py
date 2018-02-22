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
        profit=0
        dividendincome=0

        def  actionProcess(x):  # we set a center to process all the transcation
            if x.action='BUY':# once the action is BUY
                    name=x.ticker
                    price=x.price
                    share=x.shares
                    if not self.nameexist(name) or not record: # means i have this ticker
                            record.append({'ticker':name,'price':price,'share':share})
                    elif self.nameexist(name):
                        i=0
                        for t in record:
                            if t['ticker']=name:
                                t['share']=t['share']+share
            elif: x.action='SELL': # once the action is SELL
                    name=x.ticker
                    price=x.price
                    share=x.shares
                    i=0
                    for t in record:
                        if t['ticker']=name:
                            t['share']=t['share']-share
                            profit=profit+(share*(t['price']-self.price))
                            if(t['share']==0):
                                record.pop(i)
                        elif:
                            i=i+1   # to find the exact index

        def  nameexist(self,name):
            for i in self.record:
                if i['name']==name:
                    return True
                else:
                    return False

        def  stockActionProcess(y,self):
            name=y.stock
            if y.split==0 and not y.dividend==0:   #dividend
                for i in self.record:
                    if i['name']==name:
                        dividendincome=dividendincome+i['share']*i['price']*y.dividend
            elif not y.split==0 and y.dividend==0:
                for t in self.record:
                    if['name']==name:
                        i['share']=i['share']*y.dividend
                        i['price']=i['price']/y.dividend




        def  printRecord(self):
            if record:
                for i in self.record:
                    print("    - "+i['share']+" shares of "+i['name']+" at $"+i['price']+" per share")
                    print("    - $"+self.dividendincome+" of dividend income")
        def actionTransaction(x,y):
            print("Transaction:\n")
            if not y:
                print("    - "+)



    #template:
    '''
    On 1992-07-14, you have:
        - 500 shares of AAPL at $12.30 per share
        - $0 of dividend income
    Transactions:
        - You bought 500 shares of AAPL at a price of $12.30 per share
    '''
    #orginal data input:


    actions = [{'date': '1992/07/14 11:12:30', 'action': 'BUY', 'price': '12.3', 'ticker': 'AAPL', 'shares': '500'},
    {'date': '1992/09/13 11:15:20', 'action': 'SELL', 'price': '15.3', 'ticker': 'AAPL', 'shares': '100'},
    {'date': '1992/10/14 15:14:20', 'action': 'BUY', 'price': '20', 'ticker': 'MSFT', 'shares': '300'},
    {'date': '1992/10/17 16:14:30', 'action': 'SELL', 'price': '20.2', 'ticker': 'MSFT', 'shares': '200'},
    {'date': '1992/10/19 15:14:20', 'action': 'BUY', 'price': '21', 'ticker': 'MSFT', 'shares': '500'},
    {'date': '1992/10/23 16:14:30', 'action': 'SELL', 'price': '18.2', 'ticker': 'MSFT', 'shares': '600'}, {'date': '1992/10/25 10:15:20', 'action': 'SELL', 'price': '20.3', 'ticker': 'AAPL', 'shares': '300'}, {'date': '1992/10/25 16:12:10', 'action': 'BUY', 'price': '18.3', 'ticker': 'MSFT', 'shares': '500'}]

    stock_actions = [{'date': '1992/08/14', 'dividend': '0.10', 'split': '', 'stock': 'AAPL'},
    {'date': '1992/09/01', 'dividend': '', 'split': '3', 'stock': 'AAPL'},
    {'date': '1992/10/15', 'dividend': '0.20', 'split': '', 'stock': 'MSFT'},{'date': '1992/10/16', 'dividend': '0.20', 'split': '', 'stock': 'ABC'}]
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

    def printDate(date):
        print("On "+date+", you have:")

    def compareDate(a,b):
        year1,month1,day1=a.split('-')
        year2,month2,day2=b.split('-')
        if year1<year2:
            return 1
        elif year1>year2:
            return 2
        elif year1==year2:
            if month1<month2:
                return 1
            elif month1>month2:
                return 2
            elif month1==monty2:
                if day1<day2:
                    return 1
                elif day1>day2:
                    return 2
                elif day1==day2:
                    return 0


    def main () :
        mainSession=Mytransaction()
        currentDate='unknown'
        aindex=0
        sindex=0
        while aindex<len(actions) and sindex<len(stock_actions):
            d=actions[aindex]
            a = actionOBJ()
            a.convert(d)
            if currentDate=='unknow':
                currentDate=a.date

            #Mytransaction.actionProcess(i)
        #actionArray[index]=i
        #index=index+1
        #print(i.date)
        #i.setDate(d["date"])
            #i.printSelf()
        #print"\n"

            s=stock_actions[sindex]
            t=stockActionOBJ()
            t.convert(s)
            if compareDate(a.date,t.date)==1:
                printDate(a.date)
                Mytransaction.actionProcess(a)
                aindex=aindex+1
                Mytransaction.printRecord()
                Mytransaction.printTransaction()
            elif compareDate(a.date,t.date)==2:
                printDate(t.date)
                Mytransaction.stockActionProcess(t)
                sindex=sindex+1
            elif compareDate(a.date,t.date)==0:
                 printDate(a.date)
                 Mytransaction.actionProcess(a)
                 aindex=aindex+1
                 Mytransaction.stockActionProcess(t)
                 sindex=sindex+1



        #stockAction[index]=i
        #index=index+1
            #i.printSelf()
        #print"\n"

    Mytransaction.printAll()


main()
