

# WRFV4.0
## Hybrid Run Summary

#### Compiler Option : 67
**Flags** : -xHost -fp-model fast=2 -no-heap-arrays -no-prec-div -no-prec-sqrt -fno-common -xCORE-AVX2<br>
**xHost** : Tells the compiler to generate instructions for the highest instruction set available on the compilation host processor.<br>
**fp-model fast = 2** : Controls the semantics of floating-point calculations. Enables more aggressive optimizations on floating-point data.<br>
**-no-heap-arrays**  :  The compiler puts automatic arrays and temporary arrays in the stack storage area.<br>
**no-prec-div** :  Improves precision of floating-point divides.  (No) : it enables optimizations that give slightly less precise results than full IEEE division.<br>
**no-prec-sqrt** :  The compiler uses a faster but less precise implementation of square root.<br>
**no-common** : Option -fno-common tells the compiler to treat common symbols as global definitions. When using this option, you can only have a common variable declared in one module; otherwise, a link time error will occur for multiple defined symbols.<br>
**CORE-AVX2** :  expansion of most vector integer SSE and AVX instructions to 256 bits. ![NASA](https://www.nas.nasa.gov/hecc/support/kb/haswell-processors_492.html)<br>

![sim_speed](https://github.com/DixitPatel/WRF_Simulation/blob/master/results/Hybrid_sim_speed.png)
![comp_time](https://github.com/DixitPatel/WRF_Simulation/blob/master/results/Hybrid_comp_time.png)

# WRF 3.9.1

## Scalability Test Summary
### Simulation Speed
![katrina](https://github.com/DixitPatel/WRF_Simulation/blob/master/results/Scalability_Speed.png)
### Total Computation Time
![katrina](https://github.com/DixitPatel/WRF_Simulation/blob/master/results/Scalability_ComputationTime.png)



## TODO
### Katrina 1km : Intel 17.0.1+MPT2.18 and GNU 6.3.0+MVAPICH 2.2

![1km](https://github.com/DixitPatel/WRF_Simulation/blob/master/results/katrina1km.png)

### log-log

![1km-log](https://github.com/DixitPatel/WRF_Simulation/blob/master/results/katrina1km_log.png)



## Katrina 30km : Intel+MPT2.18 and GNU 6.3.0+MVAPICH 2.2
![30km](https://github.com/DixitPatel/WRF_Simulation/blob/master/results/katrina30km.png)

### log-log

![30km-log](https://github.com/DixitPatel/WRF_Simulation/blob/master/results/katrina30km_log.png)





