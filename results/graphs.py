from matplotlib import pyplot as plt


avg_sec_30_intel = [0.0515935, 0.0323609,0.020941,0.0159831,0.0139029,0.0152944,0.0199186]
ncpus_30_intel = [ 36, 72, 144, 288, 576, 1152,2304 ]

points_intel=98*70

avg_sec_30_gnu = [0.0795511,0.0473708,0.0260591,0.0252874,0.0317881,0.0941324,0.457513]
ncpus_30_gnu   = [ 36, 72, 144, 288, 576, 1152,2304 ]
points_gnu=98*70

avg_step_30_intel = [1/k for k in avg_sec_30_intel]
avg_step_30_gnu = [1/k for k in avg_sec_30_gnu]

x_30_intel = []
x_30_gnu=[]

for i,k in enumerate(ncpus_30_intel):
    x_30_intel.append(points_intel/k)
for i,k in enumerate(ncpus_30_gnu):
    x_30_gnu.append(points_gnu/k)

plt.margins(0.08)
plt.ylabel('Time steps/s')
plt.xlabel('Total grid points/core')
plt.title('Katrina 30km : 98 x 70')
plt.plot(x_30_intel,avg_step_30_intel,'--x',label='Intel MPT')
plt.plot(x_30_gnu,avg_step_30_gnu,'--o',label='GNU MVAPICH')
plt.legend(loc='best')
plt.savefig('katrina30km_cmp.png')


plt.yscale('log')
plt.xscale('log')
plt.ylabel('Time steps/s')
plt.xlabel('Total grid points/core')
plt.title('Katrina 30km : 98 x 70')
plt.plot(x_30_intel,avg_step_30_intel,'--x',label='Intel MPT')
plt.plot(x_30_gnu,avg_step_30_gnu,'--o',label='GNU MVAPICH')
plt.legend(loc='best')
plt.savefig('katrina30km_cmp_log.png')
