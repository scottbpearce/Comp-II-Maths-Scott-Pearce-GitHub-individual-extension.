from matplotlib import pyplot as plt

def R(p):
    r = p**8 + 8*p**7*(1 - p) + 28*p**6*(1 - p)**2 + 56*p**5*(1 - p)**3 + 68*p**4*(1 - p)**4 + 48*p**3*(1 - p)**5 + 16*p**2*(1 - p)**6
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