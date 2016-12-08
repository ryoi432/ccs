import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font_scale=2)
# sns.set_style("white")
sns.set_style("ticks")

#------------------------------------------------
# Graph1
#------------------------------------------------
def graph1():
	print('graph1')
	plt.clf()
	x = np.arange(0, 5, 1)
	y = np.arange(0, 5, 1)
	plt.plot(x, y, linewidth=5)
	plt.xticks([0,2,3])
	plt.yticks([0,2,3])
	plt.text(-0.5, 4, r'$u(x)$', fontsize=25)
	plt.text(4, -0.3, r'$x$', fontsize=25)
	plt.annotate("",
		xy=(0, 2), xycoords='data',
		xytext=(2, 0), textcoords='data',
		arrowprops=dict(
			arrowstyle="-",
			connectionstyle="angle,angleA=90,angleB=0,rad=0",
			shrinkA=0, shrinkB=0,
			linestyle='--',
			linewidth=2,
		),
	)
	plt.annotate("",
		xy=(0, 3), xycoords='data',
		xytext=(3, 0), textcoords='data',
		arrowprops=dict(
			arrowstyle="-",
			connectionstyle="angle,angleA=90,angleB=0,rad=0",
			shrinkA=0, shrinkB=0,
			linestyle='--',
			linewidth=2,
		),
	)
	plt.annotate("",
		xy=(3, 3), xycoords='data',
		xytext=(2, 2), textcoords='data',
		arrowprops=dict(
			arrowstyle="->",
			connectionstyle="angle,angleA=0,angleB=90,rad=0",
			shrinkA=0, shrinkB=3,
			linewidth=2,
		),
	)
	plt.plot(2, 2, 'o', zorder=10, markersize=10, color='r')
	plt.text(1.7, 2.1, r'$M$', fontsize=22)
	plt.plot(3, 3, 'o', zorder=10, markersize=10, color='r')
	plt.text(2.7, 3.1, r"$M'$", fontsize=22)
	sns.despine()
	plt.savefig("graph1.png", transparent=True)

#------------------------------------------------
# Graph2
#------------------------------------------------
def graph2():
	print('graph2')
	plt.clf()
	x1 = np.linspace(0, 4, 10)
	y1 = np.linspace(0.5, 3.5, 10)
	plt.plot(x1, y1, linewidth=5)
	x2 = np.linspace(0, 4, 10)
	y2 = np.linspace(3.5, 0.5, 10)
	plt.plot(x2, y2, linewidth=5)
	plt.text(3.55, 0.4, r'$D$', fontsize=25)
	plt.text(3.55, 3.4, r'$S$', fontsize=25)
	plt.xlim(0, 4)
	plt.ylim(0, 4)
	plt.xticks([0,2], [0,r'$q$'])
	plt.yticks([0,2], [0,r'$p$'])
	plt.text(-0.2, 4, r'$P$', fontsize=25)
	plt.text(4, -0.3, r'$Q$', fontsize=25)
	plt.fill([0,2,0],[3.5,2,2],color="y",alpha=0.5)
	plt.text(0.5, 2.35, r'$CS$', fontsize=25)
	plt.axhline(y=2, xmin=0, xmax=0.5, color='k')
	plt.axvline(x=2, ymin=0, ymax=0.5, linestyle='--', color='k')
	sns.despine()
	plt.savefig("graph2.png", transparent=True)

#------------------------------------------------
# Graph3
#------------------------------------------------
def graph3():
	print('graph3')
	plt.clf()
	ax1 = plt.subplot(1,1,1)
	x1 = np.linspace(0.01, 5, 100)
	y1 = [4 / xi for xi in x1]
	ax1.plot(x1, y1, linewidth=5, c=sns.color_palette()[0])
	plt.text(3.6, 0.2, r'$U_1$', fontsize=25)
	x1 = np.linspace(0.01, 5, 100)
	y1 = [2 / xi for xi in x1]
	ax1.plot(x1, y1, linewidth=5, c=sns.color_palette()[0])
	plt.text(3.6, 0.7, r"$U'_1$", fontsize=25)
	plt.xlim(0, 4)
	plt.ylim(0, 4)
	plt.xticks([0,0.72,2], [0,r"$x_1$",r"$x'_1$"])
	plt.yticks([0,2,2.78], [0,r"$y'_1$",r"$y_1$"])
	plt.text(3.8, -0.38, r'$X_1$', fontsize=25)
	plt.text(-0.3, 3.8, r'$Y_1$', fontsize=25)
	ax2 = ax1.twinx().twiny()
	x2 = np.linspace(0.01, 5, 100)
	y2 = [4 / xi  for xi in x2]
	ax2.plot(x2, y2, linewidth=5, c=sns.color_palette()[1])
	plt.text(3.95, 0.9, r"$U_2$", fontsize=25)
	plt.xlim(0, 4)
	plt.ylim(0, 4)
	plt.xticks([0,2,3.28], [0,r"$x'_2$",r"$x_2$"])
	plt.yticks([0,1.22,2], [0,r"$y_2$",r"$y'_2$"])
	plt.text(4, -0.2, r'$X_2$', fontsize=25)
	plt.text(-0.08, 4, r'$Y_2$', fontsize=25)
	plt.gca().invert_xaxis()
	plt.gca().invert_yaxis()
	plt.axvline(x=2, zorder=9, linestyle='--', color='k')
	plt.axhline(y=2, zorder=9, linestyle='--', color='k')
	plt.axvline(x=3.28, zorder=9, linestyle='--', color='k')
	plt.axhline(y=1.22, zorder=9, linestyle='--', color='k')
	plt.plot(3.28, 1.22, 'o', zorder=10, markersize=10, color='r')
	plt.text(3.28, 1.13, r"$P$", fontsize=22)
	plt.plot(2, 2, 'o', zorder=10, markersize=10, color='r')
	plt.text(1.95, 1.95, r"$P'$", fontsize=22)
	plt.savefig("graph3.png", transparent=True)

# graph1()
# graph2()
graph3()
