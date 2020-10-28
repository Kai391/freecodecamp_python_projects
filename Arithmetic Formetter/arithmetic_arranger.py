def arithmetic_arranger(problems,*k):
    l=problems
    n=0
    for i in l:
        n+=1
    if n <=5:
        a=0
        for i in l:
            if '+' in i or '-' in i:
                pass
            else:
                a+=1
        if a == 0:
            b=0
            for i in l:
                if '+' in i:
                    f=i.split(" + ")
                elif '-' in i:
                    f=i.split(' - ')
                if f[0].isdigit() and f[1].isdigit():
                    pass
                else:
                    b +=1
            if b==0:
                c=0
                for i in l:
                    if '+' in i:
                        f=i.split(" + ")
                    elif '-' in i:
                        f=i.split(' - ')
                    if len(f[0]) <=4 and len(f[1]) <=4:
                        pass
                    else:
                        c+=1
                if c == 0:
                    l=problems
                    D0='-'
                    if "+" in l[0]:
                        f0=l[0].split(" + ")
                        o1=f0[0]
                        x=int(o1)
                        o2=f0[1]
                        y=int(o2)
                        s=x+y
                        s=str(s)
                        if len(f0[0]) >= len(f0[1]):
                            diff=len(f0[0]) - len(f0[1])
                            for i in range(diff):
                                S=' '
                                o2=f'{S}'+o2
                            f0o1='  '+o1
                            f0o2='+ '+o2
                            for i in range(len(f0[0])):
                                d='-'
                                D0=f"{d}"+D0
                            D0='-'+D0
                        else:
                            diff=len(f0[1])-len(f0[0])
                            for i in range(diff):
                                S=' '
                                o1=f'{S}'+o1
                            f0o1='  '+o1
                            f0o2='+ '+o2
                            for i in range(len(f0[1])):
                                d='-'
                                D0=f"{d}"+D0
                            D0='-'+D0
                        if s:
                            if len(s) == len(o1) or len(s) == len(o2):
                                ans0="  "+s
                            else:
                                ans0 = " "+s
                    elif '-' in l[0]:
                        f0=l[0].split(" - ")
                        o1=f0[0]
                        x=int(o1)
                        o2=f0[1]
                        y=int(o2)
                        s=x-y
                        s=str(s)
                        if len(f0[0]) >= len(f0[1]):
                            diff=len(f0[0]) - len(f0[1])
                            for i in range(diff):
                                S=' '
                                o2=f'{S}'+o2
                            f0o1='  '+o1
                            f0o2='- '+o2
                            for i in range(len(f0[0])):
                                d='-'
                                D0=f'{d}'+D0
                            D0='-'+D0
                        else:
                            diff=len(f0[1])-len(f0[0])
                            for i in range(diff):
                                S=' '
                                o1=f'{S}'+o1
                            f0o1='  '+o1
                            f0o2='- '+o2
                            for i in range(len(f0[1])):
                                d='-'
                                D0=f'{d}'+D0
                            D0='-'+D0
                        if s:
                            if '-' not in s:
                                if len(s) == len(o1):
                                    ans0='  '+s
                                else:
                                    diff=len(o1) - len(s)
                                    for i in range(diff):
                                        S=' '
                                        s=f'{S}'+s
                                    ans0='  '+s
                            else:
                                if len(s) == len(o2):
                                    ans0='  '+s
                                elif len(s) < len(o2):
                                    diff=len(o2)-len(s)
                                    for i in range(diff):
                                        S=' '
                                        s=f'{S}'+s
                                        ans0='  '+s
                                elif len(s) > len(o2):
                                    ans0=' '+s
                    try:
                        D1='-'
                        if "+" in l[1]:
                            f1=l[1].split(" + ")
                            o1=f1[0]
                            x=int(o1)
                            o2=f1[1]
                            y=int(o2)
                            s=x+y
                            s=str(s)
                            if len(f1[0]) >= len(f1[1]):
                                # print('diff=',diff)
                                diff=len(f1[0]) - len(f1[1])
                                for i in range(diff):
                                    S=' '
                                    o2=f'{S}'+o2
                                f1o1='  '+o1
                                f1o2='+ '+o2
                                for i in range(len(f1[0])):
                                    d='-'
                                    D1=f'{d}'+D1
                                D1='-'+D1
                            else:
                                diff=len(f1[1])-len(f1[0])
                                # print('diff=',diff)
                                for i in range(diff):
                                    S=' '
                                    o1=f'{S}'+o1
                                f1o1='  '+o1
                                f1o2='+ '+o2
                                for i in range(len(f1[1])):
                                    d='-'
                                    D1=f'{d}'+D1
                                D1='-'+D1
                            if s:
                                if len(s) == len(o1) or len(s) == len(o2):
                                    ans1="  "+s
                                else:
                                    ans1 = " "+s
                        elif '-' in l[1]:
                            f1=l[1].split(" - ")
                            o1=f1[0]
                            x=int(o1)
                            o2=f1[1]
                            y=int(o2)
                            s=x-y
                            s=str(s)
                            if len(f1[0]) >= len(f1[1]):
                                diff=len(f1[0]) - len(f1[1])
                                for i in range(diff):
                                    S=' '
                                    o2=f'{S}'+o2
                                f1o1='  '+o1
                                f1o2='- '+o2
                                for i in range(len(f1[0])):
                                    d='-'
                                    D1=f'{d}'+D1
                                D1='-'+D1
                            else:
                                diff=len(f1[1])-len(f1[0])
                                for i in range(diff):
                                    S=' '
                                    o1=f'{S}'+o1
                                f1o1='  '+o1
                                f1o2='- '+o2
                                for i in range(len(f1[1])):
                                    d='-'
                                    D1=f'{d}'+D1
                                D1='-'+D1
                            if s:
                                if '-' not in s:
                                    if len(s) == len(o1):
                                        ans1='  '+s
                                    else:
                                        diff=len(o1) - len(s)
                                        for i in range(diff):
                                            S=' '
                                            s=f'{S}'+s
                                        ans1='  '+s
                                else:
                                    if len(s) == len(o2):
                                        ans1='  '+s
                                    elif len(s) < len(o2):
                                        diff=len(o2)-len(s)
                                        for i in range(diff):
                                            S=' '
                                            s=f'{S}'+s
                                            ans0='  '+s
                                    elif len(s) > len(o2):
                                        ans1=' '+s
                    except:
                        pass
                    try:
                        D2='-'
                        if "+" in l[2]:
                            f2=l[2].split(" + ")
                            o1=f2[0]
                            x=int(o1)
                            o2=f2[1]
                            y=int(o2)
                            s=x+y
                            s=str(s)
                            if len(f2[0]) >= len(f2[1]):
                                diff=len(f2[0]) - len(f2[1])
                                for i in range(diff):
                                    S=' '
                                    o2=f'{S}'+o2
                                f2o1='  '+o1
                                f2o2='+ '+o2
                                for i in range(len(f2[0])):
                                    d='-'
                                    D2=f'{d}'+D2
                                D2='-'+D2
                            else:
                                diff=len(f2[1])-len(f2[0])
                                for i in range(diff):
                                    S=' '
                                    o1=f'{S}'+o1
                                f2o1='  '+o1
                                f2o2='+ '+o2
                                for i in range(len(f2[1])):
                                    d='-'
                                    D2=f'{d}'+D2
                                D2='-'+D2
                            if s:
                                if len(s) == len(o1) or len(s) == len(o2):
                                    ans2="  "+s
                                else:
                                    ans2 = " "+s
                        elif '-' in l[2]:
                            f2=l[2].split(" - ")
                            o1=f2[0]
                            x=int(o1)
                            o2=f2[1]
                            y=int(o2)
                            s=x-y
                            s=str(s)
                            if len(f2[0]) >= len(f2[1]):
                                diff=len(f2[0]) - len(f2[1])
                                for i in range(diff):
                                    S=' '
                                    o2=f'{S}'+o2
                                f2o1='  '+o1
                                f2o2='- '+o2
                                for i in range(len(f2[0])):
                                    d='-'
                                    D2=f'{d}'+D2
                                D2='-'+D2
                            else:
                                diff=len(f2[1])-len(f2[0])
                                for i in range(diff):
                                    S=' '
                                    o1=f'{S}'+o1
                                f2o1='  '+o1
                                f2o2='- '+o2
                                for i in range(len(f2[1])):
                                    d='-'
                                    D2=f'{d}'+D2
                                D2='-'+D2
                            if s:
                                if '-' not in s:
                                    if len(s) == len(o1):
                                        ans2='  '+s
                                    else:
                                        diff=len(o1) - len(s)
                                        for i in range(diff):
                                            S=' '
                                            s=f'{S}'+s
                                        ans2='  '+s
                                else:
                                    if len(s) == len(o2):
                                        ans2='  '+s
                                    elif len(s) < len(o2):
                                        diff=len(o2)-len(s)
                                        for i in range(diff):
                                            S=' '
                                            s=f'{S}'+s
                                            ans0='  '+s
                                    elif len(s) > len(o2):
                                        ans2=' '+s
                    except:
                        pass
                    try:
                        D3='-'
                        if "+" in l[3]:
                            f3=l[3].split(" + ")
                            o1=f3[0]
                            x=int(o1)
                            o2=f3[1]
                            y=int(o2)
                            s=x+y
                            s=str(s)
                            if len(f3[0]) >= len(f3[1]):
                                diff=len(f3[0]) - len(f3[1])
                                for i in range(diff):
                                    S=' '
                                    o2=f'{S}'+o2
                                f3o1='  '+o1
                                f3o2='+ '+o2
                                for i in range(len(f3[0])):
                                    d='-'
                                    D3=f'{d}'+D3
                                D3='-'+D3
                            else:
                                diff=len(f3[1])-len(f3[0])
                                for i in range(diff):
                                    S=' '
                                    o1=f'{S}'+o1
                                f3o1='  '+o1
                                f3o2='+ '+o2
                                for i in range(len(f3[1])):
                                    d='-'
                                    D3=f'{d}'+D3
                                D3='-'+D3
                            if s:
                                if len(s) == len(o1) or len(s) == len(o2):
                                    ans3="  "+s
                                else:
                                    ans3 =" "+s
                        elif '-' in l[3]:
                            f3=l[3].split(" - ")
                            o1=f3[0]
                            x=int(o1)
                            o2=f3[1]
                            y=int(o2)
                            s=x-y
                            s=str(s)
                            if len(f3[0]) >= len(f3[1]):
                                diff=len(f3[0]) - len(f3[1])
                                for i in range(diff):
                                    S=' '
                                    o2=f'{S}'+o2
                                f3o1='  '+o1
                                f3o2='- '+o2
                                for i in range(len(f3[0])):
                                    d='-'
                                    D3=f'{d}'+D3
                                D3='-'+D3
                            else:
                                diff=len(f3[1])-len(f3[0])
                                for i in range(diff):
                                    S=' '
                                    o1=f'{S}'+o1
                                f3o1='  '+o1
                                f3o2='- '+o2
                                for i in range(len(f3[1])):
                                    d='-'
                                    D3=f'{d}'+D3
                                D3='-'+D3
                            if s:
                                if '-' not in s:
                                    if len(s) == len(o1):
                                        ans3='  '+s
                                    else:
                                        diff=len(o1) - len(s)
                                        for i in range(diff):
                                            S=' '
                                            s=f'{S}'+s
                                        ans3='  '+s
                                else:
                                    if len(s) == len(o2):
                                        ans3='  '+s
                                    elif len(s) < len(o2):
                                        diff=len(o2)-len(s)
                                        for i in range(diff):
                                            S=' '
                                            s=f'{S}'+s
                                            ans0='  '+s
                                    elif len(s) > len(o2):
                                        ans3=' '+s
                    except:
                        pass
                    try:
                        D4='-'
                        if "+" in l[4]:
                            f4=l[4].split(" + ")
                            o1=f4[0]
                            x=int(o1)
                            o2=f4[1]
                            y=int(o2)
                            s=x+y
                            s=str(s)
                            if len(f4[0]) >= len(f4[1]):
                                diff=len(f4[0]) - len(f4[1])
                                for i in range(diff):
                                    S=' '
                                    o2=f'{S}'+o2
                                f4o1='  '+o1
                                f4o2='+ '+o2
                                for i in range(len(f4[0])):
                                    d='-'
                                    D4=f'{d}'+D4
                                D4='-'+D4
                            else:
                                diff=len(f4[1])-len(f4[0])
                                for i in range(diff):
                                    S=' '
                                    o1=f'{S}'+o1
                                f4o1='  '+o1
                                f4o2='+ '+o2
                                for i in range(len(f4[1])):
                                    d='-'
                                    D4=f'{d}'+D4
                                D4='-'+D4
                            if s:
                                if len(s) == len(o1) or len(s) == len(o2):
                                    ans4="  "+s
                                else:
                                    ans4 = " "+s
                        elif '-' in l[4]:
                            f4=l[4].split(" - ")
                            o1=f4[0]
                            x=int(o1)
                            o2=f4[1]
                            y=int(o2)
                            s=x-y
                            s=str(s)
                            if len(f4[0]) >= len(f4[1]):
                                diff=len(f4[0]) - len(f4[1])
                                for i in range(diff):
                                    S=' '
                                    o2=f'{S}'+o2
                                f4o1='  '+o1
                                f4o2='- '+o2
                                for i in range(len(f4[0])):
                                    d='-'
                                    D4=f'{d}'+D4
                                D4='-'+D4
                            else:
                                diff=len(f4[1])-len(f4[0])
                                for i in range(diff):
                                    S=' '
                                    o1=f'{S}'+o1
                                f4o1='  '+o1
                                f4o2='- '+o2
                                for i in range(len(f4[1])):
                                    d='-'
                                    D4=f'{d}'+D4
                                D4='-'+D4
                            if s:
                                if '-' not in s:
                                    if len(s) == len(o1):
                                        ans4='  '+s
                                    else:
                                        diff=len(o1) - len(s)
                                        for i in range(diff):
                                            S=' '
                                            s=f'{S}'+s
                                        ans4='  '+s
                                else:
                                    if len(s) == len(o2):
                                        ans4='  '+s
                                    elif len(s) < len(o2):
                                        diff=len(o2)-len(s)
                                        for i in range(diff):
                                            S=' '
                                            s=f'{S}'+s
                                            ans0='  '+s
                                    elif len(s) > len(o2):
                                        ans4=' '+s
                    except:
                        pass
                    ss="    "
                    nw='\n'
                    try:
                        K=k[0]
                        if K == True:
                            n=0
                            for i in l:
                                n+=1
                            if n == 1:
                                p=f"{f0o1}{nw}{f0o2}{nw}{D0}{nw}{ans0}"
                                return p
                            elif n == 2:
                                p=f"{f0o1}{ss}{f1o1}{nw}{f0o2}{ss}{f1o2}{nw}{D0}{ss}{D1}{nw}{ans0}{ss}{ans1}"
                                return p
                            elif n == 3:
                                p=f"{f0o1}{ss}{f1o1}{ss}{f2o1}{nw}{f0o2}{ss}{f1o2}{ss}{f2o2}{nw}{D0}{ss}{D1}{ss}{D2}{nw}{ans0}{ss}{ans1}{ss}{ans2}"
                                return p
                            elif n == 4:
                                p=f"{f0o1}{ss}{f1o1}{ss}{f2o1}{ss}{f3o1}{nw}{f0o2}{ss}{f1o2}{ss}{f2o2}{ss}{f3o2}{nw}{D0}{ss}{D1}{ss}{D2}{ss}{D3}{nw}{ans0}{ss}{ans1}{ss}{ans2}{ss}{ans3}"
                                return p
                            elif n == 5:
                                p=f"{f0o1}{ss}{f1o1}{ss}{f2o1}{ss}{f3o1}{ss}{f4o1}{nw}{f0o2}{ss}{f1o2}{ss}{f2o2}{ss}{f3o2}{ss}{f4o2}{nw}{D0}{ss}{D1}{ss}{D2}{ss}{D3}{ss}{D4}{nw}{ans0}{ss}{ans1}{ss}{ans2}{ss}{ans3}{ss}{ans4}"
                                return p
                    except:
                        n=0
                        for i in l:
                            n+=1
                        if n == 1:
                            p=f"{f0o1}{nw}{f0o2}{nw}{D0}"
                            return p
                        elif n == 2:
                            p=f"{f0o1}{ss}{f1o1}{nw}{f0o2}{ss}{f1o2}{nw}{D0}{ss}{D1}"
                            return p
                        elif n == 3:
                            p=f"{f0o1}{ss}{f1o1}{ss}{f2o1}{nw}{f0o2}{ss}{f1o2}{ss}{f2o2}{nw}{D0}{ss}{D1}{ss}{D2}"
                            return p
                        elif n == 4:
                            p=f"{f0o1}{ss}{f1o1}{ss}{f2o1}{ss}{f3o1}{nw}{f0o2}{ss}{f1o2}{ss}{f2o2}{ss}{f3o2}{nw}{D0}{ss}{D1}{ss}{D2}{ss}{D3}"
                            return p
                        elif n == 5:
                            p=f"{f0o1}{ss}{f1o1}{ss}{f2o1}{ss}{f3o1}{ss}{f4o1}{nw}{f0o2}{ss}{f1o2}{ss}{f2o2}{ss}{f3o2}{ss}{f4o2}{nw}{D0}{ss}{D1}{ss}{D2}{ss}{D3}{ss}{D4}"
                            return p
                else:
                    return "Error: Numbers cannot be more than four digits."
            else:
                return "Error: Numbers must only contain digits."
        else:
            return "Error: Operator must be '+' or '-'."
    else:
        return"Error: Too many problems."
if __name__ == "__main__":
    print(arithmetic_arranger(['3 + 855','3801 - 2','45 + 43','123 + 49']))
    print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True))