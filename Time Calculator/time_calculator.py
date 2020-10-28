def add_time(start, duration,*w):
    s=start
    d=duration
    if 'AM' in s:
        r=s.replace(" AM","")
    else:
        r=s.replace(" PM","")
    ls=r.split(":")
    ld=d.split(":")
    som=int(ls[1])+int(ld[1])
    soh=int(ls[0])+int(ld[0])
    nod=0
    if soh > 24:
        soh=soh-24
        nod+=1
        while soh > 24:
            soh-=24
            nod+=1
    if som > 59:
        min=som-60
        min=str(min)
        if len(min) < 2:
            min='0'+min
        soh+=1
    else:
        min=str(som)
        if len(min) < 2:
            min='0'+min
    h=0.0
    if soh >= 12:
        if "PM" in s:
            nod+=1
        if soh > 12:
            hr=soh-12
            h+=0.5
            while hr > 12:
                hr-=12
                h+=0.5
        else:
            hr=str(soh)
            h+=0.5
    else:
        hr=str(soh)

    h=str(h)
    if '.5' in h:
        if 'AM' in s:
            ts='PM'
        else:
            ts='AM'
    elif '.0' in h:
        if 'AM' in s:
            ts='AM'
        else:
            ts='PM'
    if nod > 1:
        Nod=str(nod)+" days later"
    elif nod == 1:
        Nod='next day'
    try:
        W=w[0]
        low=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
        lowf=['Monday','Tuesday','Wednesday','Thusday','Friday','Saturday','Sunday']
        N=0
        while N<1:
            for i in low:
                if i in W:
                    wv=low.index(i)
                    N+=1
                    break
                else:
                    W=W.capitalize()
                    pass
        sw=wv+nod
        if sw > 7:
            sw=sw-7
            while sw > 7:
                sw-=7
            sw-=7
        nw=lowf[sw]
        nw=lowf[sw]
    except:
        pass
    try:
        if nw:
            try:
                return f"{hr}:{min} {ts}, {nw} ({Nod})"
            except:
                return f"{hr}:{min} {ts}, {nw}"
    except:
        try:
            return f"{hr}:{min} {ts} ({Nod})"
        except:
            return f"{hr}:{min} {ts}"
if __name__ == "__main__":
    
    print(add_time("11:43 PM", "24:20", "tueSday"))