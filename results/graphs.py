from matplotlib import pyplot as plt


avg_sec_30_intel = [0.0515935, 0.0323609,0.020941,0.0159831,0.0139029,0.0152944,0.0199186]
ncpus_30_intel = [ 36, 72, 144, 288, 576, 1152, 2304 ]

avg_sec_1_gnu = [ 1.11442,0.0622363,0.143558,0.0781376,0.2634571]
ncpus_1_gnu = [  72, 144, 576, 1152,2304 ]

avg_sec_1_intel = [1.43894, 0.366497,0.155412,0.0926461,0.0501186]
ncpus_1_intel = [  36, 144, 288, 576, 1152 ]

avg_sec_30_gnu = [0.0795511,0.0473708,0.0260591,0.0252874,0.0317881,0.0941324,0.457513]
ncpus_30_gnu   = [ 36, 72, 144, 288, 576, 1152,2304 ]

points_30=98*70
points_1=512*512

avg_step_30_intel = [1/k for k in avg_sec_30_intel]
avg_step_30_gnu = [1/k for k in avg_sec_30_gnu]
avg_step_1_gnu = [1/k for k in avg_sec_1_gnu]
avg_step_1_intel = [1/k for k in avg_sec_1_intel]


def ppc(cpus,points):
    arr = []
    for i,k in enumerate(cpus):
        arr.append(points/k)
    return arr

x_30_gnu = ppc(ncpus_30_gnu,points_30)
x_30_intel = ppc(ncpus_30_intel,points_30)
x_1_gnu = ppc(ncpus_1_gnu,points_1)
x_1_intel = ppc(ncpus_1_intel,points_1)

def plot(title,x,y,labels,savename):
    plt.margins(0.08)
    plt.ylabel('Time steps/s')
    plt.xlabel('Total grid points/core')
    plt.title(title)
    plt.plot(x[0],y[0],'--x',label=labels[0])
    plt.plot(x[1],y[1],'--o',label=labels[1])
    plt.legend(loc='best')
    plt.savefig(savename+'.png')
   
    plt.gcf().clear()
    plt.yscale('log')
    plt.xscale('log')
    plt.ylabel('Time steps/s')
    plt.xlabel('Total grid points/core')
    plt.title(title)
    plt.plot(x[0],y[0],'--x',label=labels[0])
    plt.plot(x[1],y[1],'--o',label=labels[1])
    plt.legend(loc='lower right')
    plt.savefig(savename+'_log.png')
    plt.gcf().clear()


plot('Katrina 30km : 98 x 70',[x_30_intel,x_30_gnu],[avg_step_30_intel,avg_step_30_gnu],['Intel 17.0.1 MPT 2.18','GNU 6.3.0 MVAPICH 2.2'],'katrina30km')
plot('Katrina 1km : 512 x 512',[x_1_intel,x_1_gnu],[avg_step_1_intel,avg_step_1_gnu],['Intel 17.0.1 MPT 2.18','GNU 6.3.0 MVAPICH 2.2'],'katrina1km')
