# ---------------------------- #
# - Author : Clement Fontana - #
# ---------------------------- #

# No licence, free of use


# Load modules
# ------------
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


# Load color map
# -------------
cmap_name = matplotlib.cm.hsv
#cmap_name = matplotlib.cm.twilight

rgb=[]


for i in range(0,cmap_name.N):
  rgb.append(cmap_name(i))

rgb=np.array(rgb)
cmap=ListedColormap(rgb)



# Make color bar
# --------------
fig = plt.figure()
ax = plt.subplot(111, polar=True)


N = 480            # Number of lines to draw color bar
Ntick = 12         # Number of ticks ( 6 / 12 / 24 / 48 ....)
ymin = 0.75        # Lower boundary of cb
ymax = 0.95        # Upper boundary of cb
tick_size = 0.03   # Ticks size 


# Define angles
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)

# Plot colored lines
for i in range(0,N):
  col=cmap( i/N )
  plt.plot([theta[i],theta[i]],[ymin,ymax],color=col,linestyle='-',zorder=0)
  # ^^^^^ to improve => use bar to manage alpha value


# Plot frame
fmin=np.ones(N)*ymin  # Lower frame
fmax=np.ones(N)*ymax  # Upper frame

plt.plot(theta,fmin,color='k',linewidth=1,linestyle='-',zorder=0)
plt.plot(theta,fmax,color='k',linewidth=1,linestyle='-',zorder=0)


# Plot ticks
ticks=[]
for i in np.arange(0, N, int(N/Ntick)) :
  plt.plot([theta[i],theta[i]],[ymax-tick_size,ymax],'k-')
  plt.plot([theta[i],theta[i]],[ymin,ymin+tick_size],'k-')

  ticks.append( 2*np.pi*i/N      )

ax.xaxis.set_ticks(ticks)


# Tick labels
xlabels=range(0,Ntick)
xlabels=np.char.add('Tick ',np.array(xlabels,dtype=str))
ax.xaxis.set_ticklabels(xlabels)

# Plot parameters
pstr='Ntick = '+str(Ntick)+" | ymin = "+str(ymin)+' | ymax =  '+str(ymax)+' | tick_size = '+str(tick_size)

plt.title(pstr)


# Tune
plt.yticks([])
plt.ylim([0,1])

plt.box(on=None)
ax.grid(False)

# Plot
plt.show()
plt.close()









        
