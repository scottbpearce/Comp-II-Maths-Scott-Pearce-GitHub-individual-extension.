from matplotlib import pyplot as plt

def R(p):
    r = 4*p**2 - 4*p**3 + p**4
    return r


plst = [0.12,0.22,0.3,0.35,0.38,0.39,0.42,0.47,0.55,0.65,0.8,0.97]
n = 10
i = 0
j = 0
a = 0
ylst = []

while i < len(plst):
    ylst = [plst[i]]
    a = R(plst[i])
    j = 0
    
    while j < n:
        ylst.append(a)
        a = R(a)
        j = j+1
        
    plt.plot(range(n+1),ylst,)
    i = i+1
plt.xlabel("iterations ($n$)")
plt.ylabel("$R^{n}(p_0)$")
plt.grid(True)
plt.show()