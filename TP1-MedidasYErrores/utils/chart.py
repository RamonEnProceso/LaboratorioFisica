import matplotlib.pyplot as plt

def chart (valorMax,valorMin, valorRepresentativo, v1, v2, nombreRecta, altura):
    
    plt.hlines(y=altura, xmin = valorMin-0.1, xmax = valorMax+0.1)
    plt.ylim(-1, 1)
    
    if(v1-v2 < (valorMax-valorMin)*0.3):
        plt.text(v1, altura, ")", color = 'red',fontsize=10,fontweight='bold',ha='center', va='center')
        plt.text(valorRepresentativo, altura, "|", color = 'red',fontsize=10,fontweight='bold',ha='center', va='center')
        plt.text(v2, altura, "(", color = 'red',fontsize=10,fontweight='bold',ha='center', va='center')
        plt.text(v2, altura -0.1, v2, color = 'red',fontsize=10,fontweight='bold',ha='right', va='center')
        plt.text(v1, altura-0.1, v1, color = 'red',fontsize=10,fontweight='bold',ha='left', va='center')
        plt.text(valorRepresentativo, altura +0.1, valorRepresentativo, color = 'red',fontsize=10,fontweight='bold',ha='center', va='center')
    else:
        plt.text(v1, altura, ")", color = 'red')
        plt.text(valorRepresentativo, altura, "|", color = 'red',fontsize=10,fontweight='bold',ha='center', va='center')
        plt.text(v2, altura, "(", color = 'red')
        plt.text(v2, altura -0.1, v2, color = 'red',fontsize=10,fontweight='bold',ha='center', va='center')
        plt.text(v1, altura-0.1, v1, color = 'red',fontsize=10,fontweight='bold',ha='center', va='center')
        plt.text(valorRepresentativo, altura -0.1, valorRepresentativo, color = 'red',fontsize=10,fontweight='bold',ha='center', va='center')
    
    plt.text(valorMax+0.01, altura+0.1, nombreRecta, fontweight='bold',ha='center', va='center')

    if (valorMax != v1 and valorMin != v2):
        plt.text(valorMin, altura -0.15, valorMin,fontsize=10,fontweight='bold',ha='center', va='center')
        plt.text(valorMax, altura -0.15, valorMax,fontsize=10,fontweight='bold',ha='center', va='center')
        plt.text(valorMax, altura, "|",fontsize=10,fontweight='bold',ha='center', va='center')
        plt.text(valorMin, altura, "|",fontsize=10,fontweight='bold',ha='center', va='center')

    plt.fill_between(x=[v2, v1],y1=altura-0.01,y2=altura+0.01,hatch='///',facecolor='none',edgecolor='red')

    plt.yticks([])
    
    
#chart(13, 11, 12 , 13, 11, "Dr(mm)", 0)
#chart(13, 11, 12.5, 12.52, 12.48, "Dc(mm)", 0.5)

#chart(51, 49, 50, 51, 49, "Hr(mm)", 0)
#chart(51, 49, 50.5, 50.52, 50.48, "Hc(mm)", 0.5)

#chart(7000, 5000, 6000, 7000, 5000, "Vr(mm)", 0)
#chart(7000, 5000, 6200, 6220, 6180, "Vc(mm)", 0.5)
