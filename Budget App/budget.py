class Category:
    def __init__(self,a):
        self.budget=a
        self.ledger=[]
    def deposit(self,amount,*des):
        try:
            self.dic={'amount':amount,'description':des[0]}
        except:
            self.dic={'amount':amount,'description':''}
        self.ledger.append(self.dic)
    def check_funds(self,amount):
        cf=int(self.get_balance())
        if cf >= amount:
            return True
        else:
            return False
    def withdraw(self,amount,*des):
        value=self.check_funds(amount)
        if value == True:
            try:
                self.dic1={'amount':-amount,'description':des[0]}
            except:
                self.dic1={'amount':-amount,'description':''}
            self.ledger.append(self.dic1)
            return True
        else:
            return False
    def transfer(self,amount,another_category):
        amont=amount
        value=self.check_funds(amount)
        if value == True:
            desc1=f'Transfer to {another_category.budget}'
            self.withdraw(amount,desc1)
            desc2=f'Transfer from {self.budget}'
            another_category.deposit(amount,desc2)
            return True
        else:
            return False
    def get_balance(self):
        n=0
        for i in self.ledger:
            n+=1
        self.total=0        
        for i in range(n):
            self.total=self.ledger[i]['amount']+self.total
        return self.total
    def __str__(self):
        length=len(self.budget)
        diff=30-int(length)
        div=diff/2
        strg=str(div)
        if '.5' in strg:
            div=diff//2
            sl=div+1
            sr=div
        elif '.0' in strg:
            div=diff//2
            sl=div
            sr=div
        Star='*'
        for i in range(sl-1):
            star='*'
            Star=f'{star}'+Star
        s1=Star
        Star='*'
        for i in range(sr-1):
            star='*'
            Star=f'{star}'+Star
        s2=Star
        title=s1+self.budget+s2
        Total=str(self.get_balance())
        if '.' in Total:
            lgb=Total.split('.')
            if len(lgb[1]) > 2:
                lgb[1]=lgb[1][:2]
                Total=lgb[0]+'.'+lgb[1]
            else:
                Total=lgb[0]+'.'+lgb[1]
        Total='Total: '+Total
        Des=self.ledger[0]['description']
        if len(Des) > 23:
            Des=Des[:23]
        else:
            pass
        amnt=str(self.ledger[0]['amount'])
        if '.' in amnt:
            pass
        else:
            amnt=amnt+'.00'
        lod=int(len(Des))
        loam=int(len(amnt))
        fs=30-(lod+loam)
        l1=Des
        for i in range(fs):
            S=" "
            l1=l1+F'{S}'
        l1=l1+amnt
        try:
            Des=self.ledger[1]['description']
            if len(Des) > 23:
                Des=Des[:23]
            else:
                pass
            amnt=str(self.ledger[1]['amount'])
            if '.' in amnt:
                pass
            else:
                amnt=amnt+'.00'
            lod=int(len(Des))
            loam=int(len(amnt))
            fs=30-(lod+loam)
            l2=Des
            for i in range(fs):
                S=" "
                l2=l2+F'{S}'
            l2=l2+amnt
        except:
            return f'{title}\n{l1}\n{Total}'
        try:
            Des=self.ledger[2]['description']
            if len(Des) > 23:
                Des=Des[:23]
            else:
                pass
            amnt=str(self.ledger[2]['amount'])
            if '.' in amnt:
                pass
            else:
                amnt=amnt+'.00'
            lod=int(len(Des))
            loam=int(len(amnt))
            fs=30-(lod+loam)
            l3=Des
            for i in range(fs):
                S=" "
                l3=l3+F'{S}'
            l3=l3+amnt
        except:
            return f'{title}\n{l1}\n{l2}\n{Total}'
        try:
            Des=self.ledger[3]['description']
            if len(Des) > 23:
                Des=Des[:23]
            else:
                pass
            amnt=str(self.ledger[3]['amount'])
            if '.' in amnt:
                pass
            else:
                amnt=amnt+'.00'
            lod=int(len(Des))
            loam=int(len(amnt))
            fs=30-(lod+loam)
            l4=Des
            for i in range(fs):
                S=" "
                l4=l4+F'{S}'
            l4=l4+amnt
        except:
            return f'{title}\n{l1}\n{l2}\n{l3}\n{Total}'
        try:
            Des=self.ledger[4]['description']
            if len(Des) > 23:
                Des=Des[:23]
            else:
                pass
            amnt=str(self.ledger[4]['amount'])
            if '.' in amnt:
                pass
            else:
                amnt=amnt+'.00'
            lod=int(len(Des))
            loam=int(len(amnt))
            fs=30-(lod+loam)
            l5=Des
            for i in range(fs):
                S=" "
                l5=l5+F'{S}'
            l5=l5+amnt
        except:
            return f'{title}\n{l1}\n{l2}\n{l3}\n{l4}\n{Total}'
        try:
            Des=self.ledger[5]['description']
            if len(Des) > 23:
                Des=Des[:23]
            else:
                pass
            amnt=str(self.ledger[5]['amount'])
            if '.' in amnt:
                pass
            else:
                amnt=amnt+'.00'
            lod=int(len(Des))
            loam=int(len(amnt))
            fs=30-(lod+loam)
            l6=Des
            for i in range(fs):
                S=" "
                l6=l6+F'{S}'
            l6=l6+amnt
            return f'{title}\n{l1}\n{l2}\n{l3}\n{l4}\n{l5}\n{l6}\n{Total}'
        except:
            return f'{title}\n{l1}\n{l2}\n{l3}\n{l4}\n{l5}\n{Total}'
def create_spend_chart(categories):
    # for first catagory
    I=0
    j=0 
    T=0  
    for i in categories[I].ledger:
        t=categories[I].ledger[j]['amount']
        if '-' in str(categories[I].ledger[j]['amount']):
            # print(categories[k].ledger[j]['amount'])
            T=T+t
        j+=1
    j=0
    V=0
    for i in categories[I].ledger:
        c=categories[I].ledger[j]['amount']
        if '-' not in str(categories[I].ledger[j]['amount']):
            # print(categories[k].ledger[j]['amount'])
            V=V+c
        j+=1
    try:
        V=int(V)
    except:
        V=float(V)
        V=round(V)
    # print("td=",V)
    st=str(T)
    st=st.replace("-","")
    try:
        st=int(st)
    except:
        st=float(st)
        st=round(st)
    # print("Total=",st)
    per=(st/V)*100
    try:
        per1=int(pr)
    except:
        per1=float(per)
        per1=round(per)
    # print('percentage1=',per1)
    # for second catagory
    try:
        I=1
        j=0 
        T=0  
        for i in categories[I].ledger:
            t=categories[I].ledger[j]['amount']
            if '-' in str(categories[I].ledger[j]['amount']):
                # print(categories[k].ledger[j]['amount'])
                T=T+t
            j+=1
        j=0
        V=0
        for i in categories[I].ledger:
            c=categories[I].ledger[j]['amount']
            if '-' not in str(categories[I].ledger[j]['amount']):
                # print(categories[k].ledger[j]['amount'])
                V=V+c
            j+=1
        try:
            V=int(V)
        except:
            V=float(V)
            V=round(V)
        # print("td=",V)
        st=str(T)
        st=st.replace("-","")
        try:
            st=int(st)
        except:
            st=float(st)
            st=round(st)
        # print("Total=",st)
        per=(st/V)*100
        try:
            per2=int(pr)
        except:
            per2=float(per)
            per2=round(per)
        # print('percentage2=',per2)
    except:
        pass
    # for third catagory
    try: 
        I=2
        j=0 
        T=0  
        for i in categories[I].ledger:
            t=categories[I].ledger[j]['amount']
            if '-' in str(categories[I].ledger[j]['amount']):
                # print(categories[k].ledger[j]['amount'])
                T=T+t
            j+=1
        j=0
        V=0
        for i in categories[I].ledger:
            c=categories[I].ledger[j]['amount']
            if '-' not in str(categories[I].ledger[j]['amount']):
                # print(categories[k].ledger[j]['amount'])
                V=V+c
            j+=1
        try:
            V=int(V)
        except:
            V=float(V)
            V=round(V)
        # print("td=",V)
        st=str(T)
        st=st.replace("-","")
        try:
            st=int(st)
        except:
            st=float(st)
            st=round(st)
        # print("Total=",st)
        per=(st/V)*100
        try:
            per3=int(pr)
        except:
            per3=float(per)
            per3=round(per)
        # print('percentage3=',per3)
    except:
        pass
    # for fourth catagorty
    try:
        I=3
        j=0 
        T=0  
        for i in categories[I].ledger:
            t=categories[I].ledger[j]['amount']
            if '-' in str(categories[I].ledger[j]['amount']):
                # print(categories[k].ledger[j]['amount'])
                T=T+t
            j+=1
        j=0
        V=0
        for i in categories[I].ledger:
            c=categories[I].ledger[j]['amount']
            if '-' not in str(categories[I].ledger[j]['amount']):
                # print(categories[k].ledger[j]['amount'])
                V=V+c
            j+=1
        try:
            V=int(V)
        except:
            V=float(V)
            V=round(V)
        # print("td=",V)
        st=str(T)
        st=st.replace("-","")
        try:
            st=int(st)
        except:
            st=float(st)
            st=round(st)
        # print("Total=",st)
        per=(st/V)*100
        try:
            per4=int(pr)
        except:
            per4=float(per)
            per4=round(per)
        # print('percentage4=',per4)
    except:
        pass
    # for fifth catagory
    try:
        I=4
        j=0 
        T=0  
        for i in categories[I].ledger:
            t=categories[I].ledger[j]['amount']
            if '-' in str(categories[I].ledger[j]['amount']):
                # print(categories[k].ledger[j]['amount'])
                T=T+t
            j+=1
        j=0
        V=0
        for i in categories[I].ledger:
            c=categories[I].ledger[j]['amount']
            if '-' not in str(categories[I].ledger[j]['amount']):
                # print(categories[k].ledger[j]['amount'])
                V=V+c
            j+=1
        try:
            V=int(V)
        except:
            V=float(V)
            V=round(V)
        # print("td=",V)
        st=str(T)
        st=st.replace("-","")
        try:
            st=int(st)
        except:
            st=float(st)
            st=round(st)
        # print("Total=",st)
        per=(st/V)*100
        try:
            per5=int(pr)
        except:
            per5=float(per)
            per5=round(per)
        # print('percentage5=',per5)
    except:
        pass
    b10='100| '
    NO=90
    if per1>NO:
        b10=b10+"o  "
        try:
            if per2>NO:
                b10=b10+"o  "
                try:
                    if per3>NO:
                        b10=b10+"o  "
                        try:
                            if per4>NO:
                                b10=b10+"o  "
                                try:
                                    if per5>NO:
                                        b10=b10+"o  "
                                    else:
                                        b10=b10+"   "
                                except:
                                    pass
                            else:
                                b10=b10+"   "
                                try:
                                    if per5>NO:
                                        b10=b10+"o  "
                                    else:
                                        b10=b10+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b10=b10+"   "
                        try:
                            if per4>NO:
                                b10=b10+"o  "
                                try:
                                    if per5>NO:
                                        b10=b10+"o  "
                                    else:
                                        b10=b10+"   "
                                except:
                                    pass
                            else:
                                b10=b10+"   "
                                try:
                                    if per5>NO:
                                        b10=b10+"o  "
                                    else:
                                        b10=b10+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b10=b10+"   "
                try:
                    if per3>NO:
                        b10=b10+"o  "
                        try:
                            if per4>NO:
                                b10=b10+"o  "
                                try:
                                    if per5>NO:
                                        b10=b10+"o  "
                                    else:
                                        b10=b10+"   "
                                except:
                                    pass
                            else:
                                b10=b10+"   "
                                try:
                                    if per5>NO:
                                        b10=b10+"o  "
                                    else:
                                        b10=b10+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b10=b10+"   "
                        try:
                            if per4>NO:
                                b10=b10+"o  "
                                try:
                                    if per5>NO:
                                        b10=b10+"o  "
                                    else:
                                        b10=b10+"   "
                                except:
                                    pass
                            else:
                                b10=b10+"   "
                                try:
                                    if per5>NO:
                                        b10=b10+"o  "
                                    else:
                                        b10=b10+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    else:
        b10=b10+"   "
        try:
            if per2>NO:
                b10=b10+"o  "
                try:
                    if per3>NO:
                        b10=b10+"o  "
                        try:
                            if per4>NO:
                                b10=b10+"o  "
                                try:
                                    if per5>NO:
                                        b10=b10+"o  "
                                    else:
                                        b10=b10+"   "
                                except:
                                    pass
                            else:
                                b10=b10+"   "
                                try:
                                    if per5>NO:
                                        b10=b10+"o  "
                                    else:
                                        b10=b10+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b10=b10+"   "
                        try:
                            if per4>NO:
                                b10=b10+"o  "
                                try:
                                    if per5>NO:
                                        b10=b10+"o  "
                                    else:
                                        b10=b10+"   "
                                except:
                                    pass
                            else:
                                b10=b10+"   "
                                try:
                                    if per5>NO:
                                        b10=b10+"o  "
                                    else:
                                        b10=b10+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b10=b10+"   "
                try:
                    if per3>NO:
                        b10=b10+"o  "
                        try:
                            if per4>NO:
                                b10=b10+"o  "
                                try:
                                    if per5>NO:
                                        b10=b10+"o  "
                                    else:
                                        b10=b10+"   "
                                except:
                                    pass
                            else:
                                b10=b10+"   "
                                try:
                                    if per5>NO:
                                        b10=b10+"o  "
                                    else:
                                        b10=b10+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b10=b10+"   "
                        try:
                            if per4>NO:
                                b10=b10+"o  "
                                try:
                                    if per5>NO:
                                        b10=b10+"o  "
                                    else:
                                        b10=b10+"   "
                                except:
                                    pass
                            else:
                                b10=b10+"   "
                                try:
                                    if per5>NO:
                                        b10=b10+"o  "
                                    else:
                                        b10=b10+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    NO=80
    b9=' 90| '
    if per1>NO:
        b9=b9+"o  "
        try:
            if per2>NO:
                b9=b9+"o  "
                try:
                    if per3>NO:
                        b9=b9+"o  "
                        try:
                            if per4>NO:
                                b9=b9+"o  "
                                try:
                                    if per5>NO:
                                        b9=b9+"o  "
                                    else:
                                        b9=b9+"   "
                                except:
                                    pass
                            else:
                                b9=b9+"   "
                                try:
                                    if per5>NO:
                                        b9=b9+"o  "
                                    else:
                                        b9=b9+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b9=b9+"   "
                        try:
                            if per4>NO:
                                b9=b9+"o  "
                                try:
                                    if per5>NO:
                                        b9=b9+"o  "
                                    else:
                                        b9=b9+"   "
                                except:
                                    pass
                            else:
                                b9=b9+"   "
                                try:
                                    if per5>NO:
                                        b9=b9+"o  "
                                    else:
                                        b9=b9+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b9=b9+"   "
                try:
                    if per3>NO:
                        b9=b9+"o  "
                        try:
                            if per4>NO:
                                b9=b9+"o  "
                                try:
                                    if per5>NO:
                                        b9=b9+"o  "
                                    else:
                                        b9=b9+"   "
                                except:
                                    pass
                            else:
                                b9=b9+"   "
                                try:
                                    if per5>NO:
                                        b9=b9+"o  "
                                    else:
                                        b9=b9+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b9=b9+"   "
                        try:
                            if per4>NO:
                                b9=b9+"o  "
                                try:
                                    if per5>NO:
                                        b9=b9+"o  "
                                    else:
                                        b9=b9+"   "
                                except:
                                    pass
                            else:
                                b9=b9+"   "
                                try:
                                    if per5>NO:
                                        b9=b9+"o  "
                                    else:
                                        b9=b9+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    else:
        b9=b9+"   "
        try:
            if per2>NO:
                b9=b9+"o  "
                try:
                    if per3>NO:
                        b9=b9+"o  "
                        try:
                            if per4>NO:
                                b9=b9+"o  "
                                try:
                                    if per5>NO:
                                        b9=b9+"o  "
                                    else:
                                        b9=b9+"   "
                                except:
                                    pass
                            else:
                                b9=b9+"   "
                                try:
                                    if per5>NO:
                                        b9=b9+"o  "
                                    else:
                                        b9=b9+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b9=b9+"   "
                        try:
                            if per4>NO:
                                b9=b9+"o  "
                                try:
                                    if per5>NO:
                                        b9=b9+"o  "
                                    else:
                                        b9=b9+"   "
                                except:
                                    pass
                            else:
                                b9=b9+"   "
                                try:
                                    if per5>NO:
                                        b9=b9+"o  "
                                    else:
                                        b9=b9+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b9=b9+"   "
                try:
                    if per3>NO:
                        b9=b9+"o  "
                        try:
                            if per4>NO:
                                b9=b9+"o  "
                                try:
                                    if per5>NO:
                                        b9=b9+"o  "
                                    else:
                                        b9=b9+"   "
                                except:
                                    pass
                            else:
                                b9=b9+"   "
                                try:
                                    if per5>NO:
                                        b9=b9+"o  "
                                    else:
                                        b9=b9+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b9=b9+"   "
                        try:
                            if per4>NO:
                                b9=b9+"o  "
                                try:
                                    if per5>NO:
                                        b9=b9+"o  "
                                    else:
                                        b9=b9+"   "
                                except:
                                    pass
                            else:
                                b9=b9+"   "
                                try:
                                    if per5>NO:
                                        b9=b9+"o  "
                                    else:
                                        b9=b9+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    
    NO=70
    b8=' 80| '
    if per1>NO:
        b8=b8+"o  "
        try:
            if per2>NO:
                b8=b8+"o  "
                try:
                    if per3>NO:
                        b8=b8+"o  "
                        try:
                            if per4>NO:
                                b8=b8+"o  "
                                try:
                                    if per5>NO:
                                        b8=b8+"o  "
                                    else:
                                        b8=b8+"   "
                                except:
                                    pass
                            else:
                                b8=b8+"   "
                                try:
                                    if per5>NO:
                                        b8=b8+"o  "
                                    else:
                                        b8=b8+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b8=b8+"   "
                        try:
                            if per4>NO:
                                b8=b8+"o  "
                                try:
                                    if per5>NO:
                                        b8=b8+"o  "
                                    else:
                                        b8=b8+"   "
                                except:
                                    pass
                            else:
                                b8=b8+"   "
                                try:
                                    if per5>NO:
                                        b8=b8+"o  "
                                    else:
                                        b8=b8+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b8=b8+"   "
                try:
                    if per3>NO:
                        b8=b8+"o  "
                        try:
                            if per4>NO:
                                b8=b8+"o  "
                                try:
                                    if per5>NO:
                                        b8=b8+"o  "
                                    else:
                                        b8=b8+"   "
                                except:
                                    pass
                            else:
                                b8=b8+"   "
                                try:
                                    if per5>NO:
                                        b8=b8+"o  "
                                    else:
                                        b8=b8+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b8=b8+"   "
                        try:
                            if per4>NO:
                                b8=b8+"o  "
                                try:
                                    if per5>NO:
                                        b8=b8+"o  "
                                    else:
                                        b8=b8+"   "
                                except:
                                    pass
                            else:
                                b8=b8+"   "
                                try:
                                    if per5>NO:
                                        b8=b8+"o  "
                                    else:
                                        b8=b8+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    else:
        b8=b8+"   "
        try:
            if per2>NO:
                b8=b8+"o  "
                try:
                    if per3>NO:
                        b8=b8+"o  "
                        try:
                            if per4>NO:
                                b8=b8+"o  "
                                try:
                                    if per5>NO:
                                        b8=b8+"o  "
                                    else:
                                        b8=b8+"   "
                                except:
                                    pass
                            else:
                                b8=b8+"   "
                                try:
                                    if per5>NO:
                                        b8=b8+"o  "
                                    else:
                                        b8=b8+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b8=b8+"   "
                        try:
                            if per4>NO:
                                b8=b8+"o  "
                                try:
                                    if per5>NO:
                                        b8=b8+"o  "
                                    else:
                                        b8=b8+"   "
                                except:
                                    pass
                            else:
                                b8=b8+"   "
                                try:
                                    if per5>NO:
                                        b8=b8+"o  "
                                    else:
                                        b8=b8+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b8=b8+"   "
                try:
                    if per3>NO:
                        b8=b8+"o  "
                        try:
                            if per4>NO:
                                b8=b8+"o  "
                                try:
                                    if per5>NO:
                                        b8=b8+"o  "
                                    else:
                                        b8=b8+"   "
                                except:
                                    pass
                            else:
                                b8=b8+"   "
                                try:
                                    if per5>NO:
                                        b8=b8+"o  "
                                    else:
                                        b8=b8+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b8=b8+"   "
                        try:
                            if per4>NO:
                                b8=b8+"o  "
                                try:
                                    if per5>NO:
                                        b8=b8+"o  "
                                    else:
                                        b8=b8+"   "
                                except:
                                    pass
                            else:
                                b8=b8+"   "
                                try:
                                    if per5>NO:
                                        b8=b8+"o  "
                                    else:
                                        b8=b8+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    
    NO=60
    b7=' 70| '
    if per1>NO:
        b7=b7+"o  "
        try:
            if per2>NO:
                b7=b7+"o  "
                try:
                    if per3>NO:
                        b7=b7+"o  "
                        try:
                            if per4>NO:
                                b7=b7+"o  "
                                try:
                                    if per5>NO:
                                        b7=b7+"o  "
                                    else:
                                        b7=b7+"   "
                                except:
                                    pass
                            else:
                                b7=b7+"   "
                                try:
                                    if per5>NO:
                                        b7=b7+"o  "
                                    else:
                                        b7=b7+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b7=b7+"   "
                        try:
                            if per4>NO:
                                b7=b7+"o  "
                                try:
                                    if per5>NO:
                                        b7=b7+"o  "
                                    else:
                                        b7=b7+"   "
                                except:
                                    pass
                            else:
                                b7=b7+"   "
                                try:
                                    if per5>NO:
                                        b7=b7+"o  "
                                    else:
                                        b7=b7+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b7=b7+"   "
                try:
                    if per3>NO:
                        b7=b7+"o  "
                        try:
                            if per4>NO:
                                b7=b7+"o  "
                                try:
                                    if per5>NO:
                                        b7=b7+"o  "
                                    else:
                                        b7=b7+"   "
                                except:
                                    pass
                            else:
                                b7=b7+"   "
                                try:
                                    if per5>NO:
                                        b7=b7+"o  "
                                    else:
                                        b7=b7+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b7=b7+"   "
                        try:
                            if per4>NO:
                                b7=b7+"o  "
                                try:
                                    if per5>NO:
                                        b7=b7+"o  "
                                    else:
                                        b7=b7+"   "
                                except:
                                    pass
                            else:
                                b7=b7+"   "
                                try:
                                    if per5>NO:
                                        b7=b7+"o  "
                                    else:
                                        b7=b7+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    else:
        b7=b7+"   "
        try:
            if per2>NO:
                b7=b7+"o  "
                try:
                    if per3>NO:
                        b7=b7+"o  "
                        try:
                            if per4>NO:
                                b7=b7+"o  "
                                try:
                                    if per5>NO:
                                        b7=b7+"o  "
                                    else:
                                        b7=b7+"   "
                                except:
                                    pass
                            else:
                                b7=b7+"   "
                                try:
                                    if per5>NO:
                                        b7=b7+"o  "
                                    else:
                                        b7=b7+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b7=b7+"   "
                        try:
                            if per4>NO:
                                b7=b7+"o  "
                                try:
                                    if per5>NO:
                                        b7=b7+"o  "
                                    else:
                                        b7=b7+"   "
                                except:
                                    pass
                            else:
                                b7=b7+"   "
                                try:
                                    if per5>NO:
                                        b7=b7+"o  "
                                    else:
                                        b7=b7+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b7=b7+"   "
                try:
                    if per3>NO:
                        b7=b7+"o  "
                        try:
                            if per4>NO:
                                b7=b7+"o  "
                                try:
                                    if per5>NO:
                                        b7=b7+"o  "
                                    else:
                                        b7=b7+"   "
                                except:
                                    pass
                            else:
                                b7=b7+"   "
                                try:
                                    if per5>NO:
                                        b7=b7+"o  "
                                    else:
                                        b7=b7+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b7=b7+"   "
                        try:
                            if per4>NO:
                                b7=b7+"o  "
                                try:
                                    if per5>NO:
                                        b7=b7+"o  "
                                    else:
                                        b7=b7+"   "
                                except:
                                    pass
                            else:
                                b7=b7+"   "
                                try:
                                    if per5>NO:
                                        b7=b7+"o  "
                                    else:
                                        b7=b7+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    
    NO=50
    b6=' 60| '
    if per1>NO:
        b6=b6+"o  "
        try:
            if per2>NO:
                b6=b6+"o  "
                try:
                    if per3>NO:
                        b6=b6+"o  "
                        try:
                            if per4>NO:
                                b6=b6+"o  "
                                try:
                                    if per5>NO:
                                        b6=b6+"o  "
                                    else:
                                        b6=b6+"   "
                                except:
                                    pass
                            else:
                                b6=b6+"   "
                                try:
                                    if per5>NO:
                                        b6=b6+"o  "
                                    else:
                                        b6=b6+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b6=b6+"   "
                        try:
                            if per4>NO:
                                b6=b6+"o  "
                                try:
                                    if per5>NO:
                                        b6=b6+"o  "
                                    else:
                                        b6=b6+"   "
                                except:
                                    pass
                            else:
                                b6=b6+"   "
                                try:
                                    if per5>NO:
                                        b6=b6+"o  "
                                    else:
                                        b6=b6+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b6=b6+"   "
                try:
                    if per3>NO:
                        b6=b6+"o  "
                        try:
                            if per4>NO:
                                b6=b6+"o  "
                                try:
                                    if per5>NO:
                                        b6=b6+"o  "
                                    else:
                                        b6=b6+"   "
                                except:
                                    pass
                            else:
                                b6=b6+"   "
                                try:
                                    if per5>NO:
                                        b6=b6+"o  "
                                    else:
                                        b6=b6+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b6=b6+"   "
                        try:
                            if per4>NO:
                                b6=b6+"o  "
                                try:
                                    if per5>NO:
                                        b6=b6+"o  "
                                    else:
                                        b6=b6+"   "
                                except:
                                    pass
                            else:
                                b6=b6+"   "
                                try:
                                    if per5>NO:
                                        b6=b6+"o  "
                                    else:
                                        b6=b6+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    else:
        b6=b6+"   "
        try:
            if per2>NO:
                b6=b6+"o  "
                try:
                    if per3>NO:
                        b6=b6+"o  "
                        try:
                            if per4>NO:
                                b6=b6+"o  "
                                try:
                                    if per5>NO:
                                        b6=b6+"o  "
                                    else:
                                        b6=b6+"   "
                                except:
                                    pass
                            else:
                                b6=b6+"   "
                                try:
                                    if per5>NO:
                                        b6=b6+"o  "
                                    else:
                                        b6=b6+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b6=b6+"   "
                        try:
                            if per4>NO:
                                b6=b6+"o  "
                                try:
                                    if per5>NO:
                                        b6=b6+"o  "
                                    else:
                                        b6=b6+"   "
                                except:
                                    pass
                            else:
                                b6=b6+"   "
                                try:
                                    if per5>NO:
                                        b6=b6+"o  "
                                    else:
                                        b6=b6+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b6=b6+"   "
                try:
                    if per3>NO:
                        b6=b6+"o  "
                        try:
                            if per4>NO:
                                b6=b6+"o  "
                                try:
                                    if per5>NO:
                                        b6=b6+"o  "
                                    else:
                                        b6=b6+"   "
                                except:
                                    pass
                            else:
                                b6=b6+"   "
                                try:
                                    if per5>NO:
                                        b6=b6+"o  "
                                    else:
                                        b6=b6+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b6=b6+"   "
                        try:
                            if per4>NO:
                                b6=b6+"o  "
                                try:
                                    if per5>NO:
                                        b6=b6+"o  "
                                    else:
                                        b6=b6+"   "
                                except:
                                    pass
                            else:
                                b6=b6+"   "
                                try:
                                    if per5>NO:
                                        b6=b6+"o  "
                                    else:
                                        b6=b6+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    
    NO=40
    b5=' 50| '
    if per1>NO:
        b5=b5+"o  "
        try:
            if per2>NO:
                b5=b5+"o  "
                try:
                    if per3>NO:
                        b5=b5+"o  "
                        try:
                            if per4>NO:
                                b5=b5+"o  "
                                try:
                                    if per5>NO:
                                        b5=b5+"o  "
                                    else:
                                        b5=b5+"   "
                                except:
                                    pass
                            else:
                                b5=b5+"   "
                                try:
                                    if per5>NO:
                                        b5=b5+"o  "
                                    else:
                                        b5=b5+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b5=b5+"   "
                        try:
                            if per4>NO:
                                b5=b5+"o  "
                                try:
                                    if per5>NO:
                                        b5=b5+"o  "
                                    else:
                                        b5=b5+"   "
                                except:
                                    pass
                            else:
                                b5=b5+"   "
                                try:
                                    if per5>NO:
                                        b5=b5+"o  "
                                    else:
                                        b5=b5+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b5=b5+"   "
                try:
                    if per3>NO:
                        b5=b5+"o  "
                        try:
                            if per4>NO:
                                b5=b5+"o  "
                                try:
                                    if per5>NO:
                                        b5=b5+"o  "
                                    else:
                                        b5=b5+"   "
                                except:
                                    pass
                            else:
                                b5=b5+"   "
                                try:
                                    if per5>NO:
                                        b5=b5+"o  "
                                    else:
                                        b5=b5+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b5=b5+"   "
                        try:
                            if per4>NO:
                                b5=b5+"o  "
                                try:
                                    if per5>NO:
                                        b5=b5+"o  "
                                    else:
                                        b5=b5+"   "
                                except:
                                    pass
                            else:
                                b5=b5+"   "
                                try:
                                    if per5>NO:
                                        b5=b5+"o  "
                                    else:
                                        b5=b5+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    else:
        b5=b5+"   "
        try:
            if per2>NO:
                b5=b5+"o  "
                try:
                    if per3>NO:
                        b5=b5+"o  "
                        try:
                            if per4>NO:
                                b5=b5+"o  "
                                try:
                                    if per5>NO:
                                        b5=b5+"o  "
                                    else:
                                        b5=b5+"   "
                                except:
                                    pass
                            else:
                                b5=b5+"   "
                                try:
                                    if per5>NO:
                                        b5=b5+"o  "
                                    else:
                                        b5=b5+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b5=b5+"   "
                        try:
                            if per4>NO:
                                b5=b5+"o  "
                                try:
                                    if per5>NO:
                                        b5=b5+"o  "
                                    else:
                                        b5=b5+"   "
                                except:
                                    pass
                            else:
                                b5=b5+"   "
                                try:
                                    if per5>NO:
                                        b5=b5+"o  "
                                    else:
                                        b5=b5+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b5=b5+"   "
                try:
                    if per3>NO:
                        b5=b5+"o  "
                        try:
                            if per4>NO:
                                b5=b5+"o  "
                                try:
                                    if per5>NO:
                                        b5=b5+"o  "
                                    else:
                                        b5=b5+"   "
                                except:
                                    pass
                            else:
                                b5=b5+"   "
                                try:
                                    if per5>NO:
                                        b5=b5+"o  "
                                    else:
                                        b5=b5+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b5=b5+"   "
                        try:
                            if per4>NO:
                                b5=b5+"o  "
                                try:
                                    if per5>NO:
                                        b5=b5+"o  "
                                    else:
                                        b5=b5+"   "
                                except:
                                    pass
                            else:
                                b5=b5+"   "
                                try:
                                    if per5>NO:
                                        b5=b5+"o  "
                                    else:
                                        b5=b5+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    
    NO=30
    b4=' 40| '
    if per1>NO:
        b4=b4+"o  "
        try:
            if per2>NO:
                b4=b4+"o  "
                try:
                    if per3>NO:
                        b4=b4+"o  "
                        try:
                            if per4>NO:
                                b4=b4+"o  "
                                try:
                                    if per5>NO:
                                        b4=b4+"o  "
                                    else:
                                        b4=b4+"   "
                                except:
                                    pass
                            else:
                                b4=b4+"   "
                                try:
                                    if per5>NO:
                                        b4=b4+"o  "
                                    else:
                                        b4=b4+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b4=b4+"   "
                        try:
                            if per4>NO:
                                b4=b4+"o  "
                                try:
                                    if per5>NO:
                                        b4=b4+"o  "
                                    else:
                                        b4=b4+"   "
                                except:
                                    pass
                            else:
                                b4=b4+"   "
                                try:
                                    if per5>NO:
                                        b4=b4+"o  "
                                    else:
                                        b4=b4+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b4=b4+"   "
                try:
                    if per3>NO:
                        b4=b4+"o  "
                        try:
                            if per4>NO:
                                b4=b4+"o  "
                                try:
                                    if per5>NO:
                                        b4=b4+"o  "
                                    else:
                                        b4=b4+"   "
                                except:
                                    pass
                            else:
                                b4=b4+"   "
                                try:
                                    if per5>NO:
                                        b4=b4+"o  "
                                    else:
                                        b4=b4+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b4=b4+"   "
                        try:
                            if per4>NO:
                                b4=b4+"o  "
                                try:
                                    if per5>NO:
                                        b4=b4+"o  "
                                    else:
                                        b4=b4+"   "
                                except:
                                    pass
                            else:
                                b4=b4+"   "
                                try:
                                    if per5>NO:
                                        b4=b4+"o  "
                                    else:
                                        b4=b4+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    else:
        b4=b4+"   "
        try:
            if per2>NO:
                b4=b4+"o  "
                try:
                    if per3>NO:
                        b4=b4+"o  "
                        try:
                            if per4>NO:
                                b4=b4+"o  "
                                try:
                                    if per5>NO:
                                        b4=b4+"o  "
                                    else:
                                        b4=b4+"   "
                                except:
                                    pass
                            else:
                                b4=b4+"   "
                                try:
                                    if per5>NO:
                                        b4=b4+"o  "
                                    else:
                                        b4=b4+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b4=b4+"   "
                        try:
                            if per4>NO:
                                b4=b4+"o  "
                                try:
                                    if per5>NO:
                                        b4=b4+"o  "
                                    else:
                                        b4=b4+"   "
                                except:
                                    pass
                            else:
                                b4=b4+"   "
                                try:
                                    if per5>NO:
                                        b4=b4+"o  "
                                    else:
                                        b4=b4+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b4=b4+"   "
                try:
                    if per3>NO:
                        b4=b4+"o  "
                        try:
                            if per4>NO:
                                b4=b4+"o  "
                                try:
                                    if per5>NO:
                                        b4=b4+"o  "
                                    else:
                                        b4=b4+"   "
                                except:
                                    pass
                            else:
                                b4=b4+"   "
                                try:
                                    if per5>NO:
                                        b4=b4+"o  "
                                    else:
                                        b4=b4+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b4=b4+"   "
                        try:
                            if per4>NO:
                                b4=b4+"o  "
                                try:
                                    if per5>NO:
                                        b4=b4+"o  "
                                    else:
                                        b4=b4+"   "
                                except:
                                    pass
                            else:
                                b4=b4+"   "
                                try:
                                    if per5>NO:
                                        b4=b4+"o  "
                                    else:
                                        b4=b4+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    
    NO=20
    b3=' 30| '
    if per1>NO:
        b3=b3+"o  "
        try:
            if per2>NO:
                b3=b3+"o  "
                try:
                    if per3>NO:
                        b3=b3+"o  "
                        try:
                            if per4>NO:
                                b3=b3+"o  "
                                try:
                                    if per5>NO:
                                        b3=b3+"o  "
                                    else:
                                        b3=b3+"   "
                                except:
                                    pass
                            else:
                                b3=b3+"   "
                                try:
                                    if per5>NO:
                                        b3=b3+"o  "
                                    else:
                                        b3=b3+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b3=b3+"   "
                        try:
                            if per4>NO:
                                b3=b3+"o  "
                                try:
                                    if per5>NO:
                                        b3=b3+"o  "
                                    else:
                                        b3=b3+"   "
                                except:
                                    pass
                            else:
                                b3=b3+"   "
                                try:
                                    if per5>NO:
                                        b3=b3+"o  "
                                    else:
                                        b3=b3+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b3=b3+"   "
                try:
                    if per3>NO:
                        b3=b3+"o  "
                        try:
                            if per4>NO:
                                b3=b3+"o  "
                                try:
                                    if per5>NO:
                                        b3=b3+"o  "
                                    else:
                                        b3=b3+"   "
                                except:
                                    pass
                            else:
                                b3=b3+"   "
                                try:
                                    if per5>NO:
                                        b3=b3+"o  "
                                    else:
                                        b3=b3+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b3=b3+"   "
                        try:
                            if per4>NO:
                                b3=b3+"o  "
                                try:
                                    if per5>NO:
                                        b3=b3+"o  "
                                    else:
                                        b3=b3+"   "
                                except:
                                    pass
                            else:
                                b3=b3+"   "
                                try:
                                    if per5>NO:
                                        b3=b3+"o  "
                                    else:
                                        b3=b3+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    else:
        b3=b3+"   "
        try:
            if per2>NO:
                b3=b3+"o  "
                try:
                    if per3>NO:
                        b3=b3+"o  "
                        try:
                            if per4>NO:
                                b3=b3+"o  "
                                try:
                                    if per5>NO:
                                        b3=b3+"o  "
                                    else:
                                        b3=b3+"   "
                                except:
                                    pass
                            else:
                                b3=b3+"   "
                                try:
                                    if per5>NO:
                                        b3=b3+"o  "
                                    else:
                                        b3=b3+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b3=b3+"   "
                        try:
                            if per4>NO:
                                b3=b3+"o  "
                                try:
                                    if per5>NO:
                                        b3=b3+"o  "
                                    else:
                                        b3=b3+"   "
                                except:
                                    pass
                            else:
                                b3=b3+"   "
                                try:
                                    if per5>NO:
                                        b3=b3+"o  "
                                    else:
                                        b3=b3+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b3=b3+"   "
                try:
                    if per3>NO:
                        b3=b3+"o  "
                        try:
                            if per4>NO:
                                b3=b3+"o  "
                                try:
                                    if per5>NO:
                                        b3=b3+"o  "
                                    else:
                                        b3=b3+"   "
                                except:
                                    pass
                            else:
                                b3=b3+"   "
                                try:
                                    if per5>NO:
                                        b3=b3+"o  "
                                    else:
                                        b3=b3+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b3=b3+"   "
                        try:
                            if per4>NO:
                                b3=b3+"o  "
                                try:
                                    if per5>NO:
                                        b3=b3+"o  "
                                    else:
                                        b3=b3+"   "
                                except:
                                    pass
                            else:
                                b3=b3+"   "
                                try:
                                    if per5>NO:
                                        b3=b3+"o  "
                                    else:
                                        b3=b3+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    
    NO=10
    b2=' 20| '
    if per1>NO:
        b2=b2+"o  "
        try:
            if per2>NO:
                b2=b2+"o  "
                try:
                    if per3>NO:
                        b2=b2+"o  "
                        try:
                            if per4>NO:
                                b2=b2+"o  "
                                try:
                                    if per5>NO:
                                        b2=b2+"o  "
                                    else:
                                        b2=b2+"   "
                                except:
                                    pass
                            else:
                                b2=b2+"   "
                                try:
                                    if per5>NO:
                                        b2=b2+"o  "
                                    else:
                                        b2=b2+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b2=b2+"   "
                        try:
                            if per4>NO:
                                b2=b2+"o  "
                                try:
                                    if per5>NO:
                                        b2=b2+"o  "
                                    else:
                                        b2=b2+"   "
                                except:
                                    pass
                            else:
                                b2=b2+"   "
                                try:
                                    if per5>NO:
                                        b2=b2+"o  "
                                    else:
                                        b2=b2+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b2=b2+"   "
                try:
                    if per3>NO:
                        b2=b2+"o  "
                        try:
                            if per4>NO:
                                b2=b2+"o  "
                                try:
                                    if per5>NO:
                                        b2=b2+"o  "
                                    else:
                                        b2=b2+"   "
                                except:
                                    pass
                            else:
                                b2=b2+"   "
                                try:
                                    if per5>NO:
                                        b2=b2+"o  "
                                    else:
                                        b2=b2+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b2=b2+"   "
                        try:
                            if per4>NO:
                                b2=b2+"o  "
                                try:
                                    if per5>NO:
                                        b2=b2+"o  "
                                    else:
                                        b2=b2+"   "
                                except:
                                    pass
                            else:
                                b2=b2+"   "
                                try:
                                    if per5>NO:
                                        b2=b2+"o  "
                                    else:
                                        b2=b2+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    else:
        b2=b2+"   "
        try:
            if per2>NO:
                b2=b2+"o  "
                try:
                    if per3>NO:
                        b2=b2+"o  "
                        try:
                            if per4>NO:
                                b2=b2+"o  "
                                try:
                                    if per5>NO:
                                        b2=b2+"o  "
                                    else:
                                        b2=b2+"   "
                                except:
                                    pass
                            else:
                                b2=b2+"   "
                                try:
                                    if per5>NO:
                                        b2=b2+"o  "
                                    else:
                                        b2=b2+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b2=b2+"   "
                        try:
                            if per4>NO:
                                b2=b2+"o  "
                                try:
                                    if per5>NO:
                                        b2=b2+"o  "
                                    else:
                                        b2=b2+"   "
                                except:
                                    pass
                            else:
                                b2=b2+"   "
                                try:
                                    if per5>NO:
                                        b2=b2+"o  "
                                    else:
                                        b2=b2+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b2=b2+"   "
                try:
                    if per3>NO:
                        b2=b2+"o  "
                        try:
                            if per4>NO:
                                b2=b2+"o  "
                                try:
                                    if per5>NO:
                                        b2=b2+"o  "
                                    else:
                                        b2=b2+"   "
                                except:
                                    pass
                            else:
                                b2=b2+"   "
                                try:
                                    if per5>NO:
                                        b2=b2+"o  "
                                    else:
                                        b2=b2+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b2=b2+"   "
                        try:
                            if per4>NO:
                                b2=b2+"o  "
                                try:
                                    if per5>NO:
                                        b2=b2+"o  "
                                    else:
                                        b2=b2+"   "
                                except:
                                    pass
                            else:
                                b2=b2+"   "
                                try:
                                    if per5>NO:
                                        b2=b2+"o  "
                                    else:
                                        b2=b2+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    
    NO=5
    b1=' 10| '
    if per1>NO:
        b1=b1+"o  "
        try:
            if per2>NO:
                b1=b1+"o  "
                try:
                    if per3>NO:
                        b1=b1+"o  "
                        try:
                            if per4>NO:
                                b1=b1+"o  "
                                try:
                                    if per5>NO:
                                        b1=b1+"o  "
                                    else:
                                        b1=b1+"   "
                                except:
                                    pass
                            else:
                                b1=b1+"   "
                                try:
                                    if per5>NO:
                                        b1=b1+"o  "
                                    else:
                                        b1=b1+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b1=b1+"   "
                        try:
                            if per4>NO:
                                b1=b1+"o  "
                                try:
                                    if per5>NO:
                                        b1=b1+"o  "
                                    else:
                                        b1=b1+"   "
                                except:
                                    pass
                            else:
                                b1=b1+"   "
                                try:
                                    if per5>NO:
                                        b1=b1+"o  "
                                    else:
                                        b1=b1+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b1=b1+"   "
                try:
                    if per3>NO:
                        b1=b1+"o  "
                        try:
                            if per4>NO:
                                b1=b1+"o  "
                                try:
                                    if per5>NO:
                                        b1=b1+"o  "
                                    else:
                                        b1=b1+"   "
                                except:
                                    pass
                            else:
                                b1=b1+"   "
                                try:
                                    if per5>NO:
                                        b1=b1+"o  "
                                    else:
                                        b1=b1+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b1=b1+"   "
                        try:
                            if per4>NO:
                                b1=b1+"o  "
                                try:
                                    if per5>NO:
                                        b1=b1+"o  "
                                    else:
                                        b1=b1+"   "
                                except:
                                    pass
                            else:
                                b1=b1+"   "
                                try:
                                    if per5>NO:
                                        b1=b1+"o  "
                                    else:
                                        b1=b1+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    else:
        b1=b1+"   "
        try:
            if per2>NO:
                b1=b1+"o  "
                try:
                    if per3>NO:
                        b1=b1+"o  "
                        try:
                            if per4>NO:
                                b1=b1+"o  "
                                try:
                                    if per5>NO:
                                        b1=b1+"o  "
                                    else:
                                        b1=b1+"   "
                                except:
                                    pass
                            else:
                                b1=b1+"   "
                                try:
                                    if per5>NO:
                                        b1=b1+"o  "
                                    else:
                                        b1=b1+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b1=b1+"   "
                        try:
                            if per4>NO:
                                b1=b1+"o  "
                                try:
                                    if per5>NO:
                                        b1=b1+"o  "
                                    else:
                                        b1=b1+"   "
                                except:
                                    pass
                            else:
                                b1=b1+"   "
                                try:
                                    if per5>NO:
                                        b1=b1+"o  "
                                    else:
                                        b1=b1+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b1=b1+"   "
                try:
                    if per3>NO:
                        b1=b1+"o  "
                        try:
                            if per4>NO:
                                b1=b1+"o  "
                                try:
                                    if per5>NO:
                                        b1=b1+"o  "
                                    else:
                                        b1=b1+"   "
                                except:
                                    pass
                            else:
                                b1=b1+"   "
                                try:
                                    if per5>NO:
                                        b1=b1+"o  "
                                    else:
                                        b1=b1+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b1=b1+"   "
                        try:
                            if per4>NO:
                                b1=b1+"o  "
                                try:
                                    if per5>NO:
                                        b1=b1+"o  "
                                    else:
                                        b1=b1+"   "
                                except:
                                    pass
                            else:
                                b1=b1+"   "
                                try:
                                    if per5>NO:
                                        b1=b1+"o  "
                                    else:
                                        b1=b1+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    
    NO=0.1
    b0='  0| '
    if per1>NO:
        b0=b0+"o  "
        try:
            if per2>NO:
                b0=b0+"o  "
                try:
                    if per3>NO:
                        b0=b0+"o  "
                        try:
                            if per4>NO:
                                b0=b0+"o  "
                                try:
                                    if per5>NO:
                                        b0=b0+"o  "
                                    else:
                                        b0=b0+"   "
                                except:
                                    pass
                            else:
                                b0=b0+"   "
                                try:
                                    if per5>NO:
                                        b0=b0+"o  "
                                    else:
                                        b0=b0+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b0=b0+"   "
                        try:
                            if per4>NO:
                                b0=b0+"o  "
                                try:
                                    if per5>NO:
                                        b0=b0+"o  "
                                    else:
                                        b0=b0+"   "
                                except:
                                    pass
                            else:
                                b0=b0+"   "
                                try:
                                    if per5>NO:
                                        b0=b0+"o  "
                                    else:
                                        b0=b0+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b0=b0+"   "
                try:
                    if per3>NO:
                        b0=b0+"o  "
                        try:
                            if per4>NO:
                                b0=b0+"o  "
                                try:
                                    if per5>NO:
                                        b0=b0+"o  "
                                    else:
                                        b0=b0+"   "
                                except:
                                    pass
                            else:
                                b0=b0+"   "
                                try:
                                    if per5>NO:
                                        b0=b0+"o  "
                                    else:
                                        b0=b0+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b0=b0+"   "
                        try:
                            if per4>NO:
                                b0=b0+"o  "
                                try:
                                    if per5>NO:
                                        b0=b0+"o  "
                                    else:
                                        b0=b0+"   "
                                except:
                                    pass
                            else:
                                b0=b0+"   "
                                try:
                                    if per5>NO:
                                        b0=b0+"o  "
                                    else:
                                        b0=b0+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass
    else:
        b0=b0+"   "
        try:
            if per2>NO:
                b0=b0+"o  "
                try:
                    if per3>NO:
                        b0=b0+"o  "
                        try:
                            if per4>NO:
                                b0=b0+"o  "
                                try:
                                    if per5>NO:
                                        b0=b0+"o  "
                                    else:
                                        b0=b0+"   "
                                except:
                                    pass
                            else:
                                b0=b0+"   "
                                try:
                                    if per5>NO:
                                        b0=b0+"o  "
                                    else:
                                        b0=b0+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b0=b0+"   "
                        try:
                            if per4>NO:
                                b0=b0+"o  "
                                try:
                                    if per5>NO:
                                        b0=b0+"o  "
                                    else:
                                        b0=b0+"   "
                                except:
                                    pass
                            else:
                                b0=b0+"   "
                                try:
                                    if per5>NO:
                                        b0=b0+"o  "
                                    else:
                                        b0=b0+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
            else:
                b0=b0+"   "
                try:
                    if per3>NO:
                        b0=b0+"o  "
                        try:
                            if per4>NO:
                                b0=b0+"o  "
                                try:
                                    if per5>NO:
                                        b0=b0+"o  "
                                    else:
                                        b0=b0+"   "
                                except:
                                    pass
                            else:
                                b0=b0+"   "
                                try:
                                    if per5>NO:
                                        b0=b0+"o  "
                                    else:
                                        b0=b0+"   "
                                except:
                                    pass
                        except:
                            pass
                    else:
                        b0=b0+"   "
                        try:
                            if per4>NO:
                                b0=b0+"o  "
                                try:
                                    if per5>NO:
                                        b0=b0+"o  "
                                    else:
                                        b0=b0+"   "
                                except:
                                    pass
                            else:
                                b0=b0+"   "
                                try:
                                    if per5>NO:
                                        b0=b0+"o  "
                                    else:
                                        b0=b0+"   "
                                except:
                                    pass
                        except:
                            pass
                except:
                    pass
        except:
            pass

    phl='Percentage spent by category'
    z=0
    for i in categories:
        z+=1
    # print(z)
    dash='    '
    Dash='-'
    for i in range(z):
        dsh='---'
        Dash=f'{dsh}'+Dash
    dash=dash+Dash
    lst1=[]
    lst2=[]
    for i in categories:
        lst1.append(i.budget)
        lst2.append(i.budget)
    lnth=0
    for i in range(lst1.__len__()):
        try:
            a=lst1[i]
        except:
            break
        v=lst1.index(lst1[i])
        lst1.pop(v)
        try:
            b=lst1[i]
            if len(a) >= lnth:
                lnth=len(a)
                if lnth <= len(b):
                    lnth=len(b)
                else:
                    pass
            else:
                pass
        except:
            if len(a) >= lnth:
                lnth=len(a)
            else:
                pass
            break
    # print(lnth)
    for i in range(lst2.__len__()):
        diff=lnth-len(lst2[i])
        if diff > 0:
            h=lst2[i]
            a=lst2[i]
            for j in range(diff):
                S=' '
                h=h+S
            lst2[i]=lst2[i].replace(a,h)
        else:
            pass
    P=0
    if lst2.__len__() == 4:
        item=''
        for i in lst2[0]:
            item=item+"     "+i+"  "
            for i in lst2[1]:
                item=item+i+'  '
                lst2[1]=lst2[1][1:]
                # break
                for i in lst2[2]:
                    item=item+i+'  '
                    lst2[2]=lst2[2][1:]
                    for i in lst2[3]:
                        P+=1
                        if P != 13:
                            item=item+i+'  '+'\n'
                        else:
                            item=item+i+'  '
                        lst2[3]=lst2[3][1:]
                        break
                    break
                break
    elif lst2.__len__() ==3:
        item=''
        for i in lst2[0]:
            item=item+"     "+i+"  "
            for i in lst2[1]:
                # item=item+'  '+i
                item=item+i+'  '
                lst2[1]=lst2[1][1:]
                # break
                for i in lst2[2]:
                    P+=1
                    if P != 13:
                        item=item+i+'  '+'\n'
                    else:
                        item=item+i+'  '
                    lst2[2]=lst2[2][1:]
                    break
                break
    
    
    B=phl+'\n'+b10+'\n'+b9+'\n'+b8+'\n'+b7+'\n'+b6+'\n'+b5+'\n'+b4+'\n'+b3+'\n'+b2+'\n'+b1+'\n'+b0+'\n'+dash+'\n'+item
    # print(B)
    # print(B[823])
    return B
if __name__ == "__main__":
    food=Category('Food')
    enter=Category('Entertainment')
    bu=Category("Business")
    sal=Category('Saloon')
    # sal.deposit(500,'deposit')
    # sal.withdraw(150)
    food.deposit(900, "deposit")
    enter.deposit(900, "deposit")
    bu.deposit(900, "deposit")
    food.withdraw(105.55)
    enter.withdraw(33.40)
    bu.withdraw(10.99)
    print(create_spend_chart([bu,food,enter]))