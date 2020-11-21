import matplotlib
import matplotlib.pyplot as plt
def txs():
    # Data for plotting
    x=[]
    y=[]
    with open("log.txt") as f:
        ls=f.readlines()
        for l in ls:
            l=l.split(",")
            x.append(l[1])
            y.append(l[0])
    return x,y
x,y=txs()
# x=[1,2,3,100]
# y=[1,1,1,1000]
matplotlib.rcParams["ytick.color"] = 'white'
matplotlib.rcParams["xtick.color"] = 'white'
matplotlib.rcParams["text.color"] = 'green'
plt.ylim(ymin=0,ymax=100)
plt.plot(x,y,'r-o')
plt.savefig("111.png",bbox_inches='tight', transparent=True)
