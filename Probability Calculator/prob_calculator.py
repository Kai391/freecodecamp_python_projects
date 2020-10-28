import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**balls):
        self.contents=[]
        for i in balls.values():
            for j in range(i):
                for k in balls.keys():
                    if balls[k] == i:
                        self.contents.append(k)
    def show(self):
        return self.contents
    def draw(self,dbs):
        l1=[]
        if dbs <= self.contents.__len__():
            for i in range(dbs):
                rb=random.choice(self.contents)
                index=self.contents.index(rb)
                # print(index)
                self.contents.pop(index)
                l1.append(rb)
            # print(self.contents)
            return l1
        else:
            return self.contents
    def __str__(self):
        # h=''
        # for i in self.contents:
        #     h=h+i+' '
        # return h
        return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    ht=hat.__str__()
    ht1=ht.copy()
    Num=0
    for ne in range(num_experiments):
        hat.contents.clear()
        for i in ht1:
            hat.contents.append(i)
        # print(hat.contents)
        # print(hat.contents)
        drawn_balls_list=hat.draw(num_balls_drawn)
        # print(drawn_balls_list)
        D={}
        for i in drawn_balls_list:
            c=drawn_balls_list.count(i)
            D.update({i:c})
        # print('Ramdamlly out comes balls:',D)
        # print('desire balls:',expected_balls)
        h=''
        for i in expected_balls.keys():
            # print(i)
            if i in D:
                if expected_balls[i]<=D[i]:
                    v='yes'
                    h=h+v
                else:
                    v='no'
                    h=h+v            
            else:
                v='no'
                h=h+v  
        numberoftrue=0
        if 'no' not in h:
            numberoftrue+=1
            Num+=1
        # print(numberoftrue)
    # print('total no of probability of out come of desire balls=',Num)
    # print('num_experiment=',num_experiments)
    # probability=int((Num/num_experiments)*100)
    probability=Num/num_experiments
    # print('probability percentage=',str(probability)+'%')
    print('probability=',probability)
    return probability
        
if __name__ == "__main__":
    hat= Hat(blue=3,red=2,green=6)
    print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=10))
    # print(hat)