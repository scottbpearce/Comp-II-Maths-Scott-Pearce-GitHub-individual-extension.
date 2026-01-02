from matplotlib import pyplot as plt

def R(p):
    r = p**2
    return r

xlst = [i/100 for i in range(101)]
ylst = [R(i) for i in xlst]

plt.plot(xlst,ylst,color = "red")
plt.plot(xlst,xlst,"--", label="$y=p$")

plt.xlabel("$p$")
plt.ylabel("$R(p)$")
plt.grid(True)
plt.legend()
plt.show()