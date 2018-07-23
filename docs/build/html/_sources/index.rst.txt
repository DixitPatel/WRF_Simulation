.. WRF Benchmarks documentation master file, created by
   sphinx-quickstart on Wed Jul 11 17:06:40 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

WRF Scaling Results
==========================================
.. Attention:: Under revision
.. contents:: Table of Contents

Below graph gives the summary for all simulations with various compilers and libraries.
The aim for these performance benchmarks can be summarized as :
 - "Is it possible to solve a problem with such-and-such resolution in a timely manner?"
 - "If I use more cores I will have the results more quickly, but with this resolution will my run be in the efficient strong-scaling regime, an intermediate one, or in the very inefficient one dominated by I/O and initialization instead of computing?"

Configurations::
	- Compilers : Intel, GNU
	- MPI  : mpt,mvapich
	- Cases : Katrina 1km, Katrina 3km

.. image:: ../../results/all_mpi.svg
    :width: 400px

Conclusion
-------------------
 - Intel 18.0.1 (latest) + MPT 2.18 gives the best performance.
 
`Yellowstone<https://www2.cisl.ucar.edu/software/community-models/wrf-scaling-and-timing>`
 - As you can see, there are three regimes:

     - large number of grid points per core - Total grid points / core > 104 (small core count)
     - intermediate number of grid points per core - 104 < Total grid points / core < 10^4 (intermediate core count)
     - small number of grid points per core - Total grid points / core < 104 (large core count)

 For a small number of cores, the WRF computation kernel is in a strong scaling regime. Increasing the core count will make the simulation go faster while it consumes approximately the same amount of core-hours (ignoring time spent in initialization and I/O). Time-to-solution will also depend on the wait in queue, which may be larger for larger jobs.

 For an intermediate number of cores, WRF scaling increasingly departs from linear strong scaling. Running the same simulation on larger core counts will require more core-hours even though it will still run faster (again, ignoring time spent in initialization, I/O, and wait in queue).

We do not recommend running WRF on extremely large core counts, because in this regime the speed benefits diminish, the time will be dominated by initialization and I/O (as well as wait in queue), and there will be larger core-hours charges for solving the same problem.

Hybrid Runs Summary
-------------------

- Hybrid runs perform better than pure MPI runs if there is good load balancing across cores.
- The below run shows 4 or 6 MPI tasks works best.( Total 72 CPU's were used)
- There are two options available to user to compile WRF with Intel (./configure):
  1. Option 15/16 : This is a normal option without any optimization flags
  2. Option 66/67. This uses several optimization flags, a summary of which is listed below.

**Configuration**

	Run : WRFV4 Katrina 3km
	NCPUS : 72
	
- **WRFV4 Intel 18.0.1 MPT 2.18 OpenMP/MPI Speedup Comparision.** ::

  	Note : 36mpi means no openmp threads.
	As we can see, hybrid mpi with 4 MPI tasks and 9 OpenMP threads performs the best. From the last two bars, Option 66 gives better speedup than option 15. 

.. image:: ../../results/hybrid_mpi_speedup.svg
    :width: 400px

- **WRFV4 Intel 18.0.1 MPT 2.18 OpenMP Comparisions.**

.. image:: ../../results/intel18_openmp_67_speed.svg
    :width: 400px

- **Option 67 gives slightly better simulation speed.**

.. image:: ../../results/Intel17_16vs67.svg
    :width: 400px

- **Option 15 vs Option 66 MPI only comparision**

.. image:: ../../results/15_vs_66.svg
    :width: 400px


Compiler Option 67 flags
------------------------
**Flags** : -xHost -fp-model fast=2 -no-heap-arrays -no-prec-div -no-prec-sqrt -fno-common -xCORE-AVX2

**xHost** : Tells the compiler to generate instructions for the highest instruction set available on the compilation host processor.

**fp-model fast = 2** : Controls the semantics of floating-point calculations. Enables more aggressive optimizations on floating-point data.

**-no-heap-arrays**  :  The compiler puts automatic arrays and temporary arrays in the stack storage area.

**no-prec-div** :  Improves precision of floating-point divides.  (No) : it enables optimizations that give slightly less precise results than full IEEE division.

**no-prec-sqrt** :  The compiler uses a faster but less precise implementation of square root.

**no-common** : Option -fno-common tells the compiler to treat common symbols as global definitions. When using this option, you can only have a common variable declared in one module; otherwise, a link time error will occur for multiple defined symbols.

**CORE-AVX2** :  expansion of most vector integer SSE and AVX instructions to 256 bits. `NASA` <https://www.nas.nasa.gov/hecc/support/kb/haswell-processors_492.html>


HyperThreading Results
==========================================
**Configuration** : WRFV4. Katrina 3km 800x900

Hyperthreading on cheyenne lowers the model performance. Below are a few comparisions with hyperthreading. Some examples of PBS scripts can be found here : [Cheyenne](https://www2.cisl.ucar.edu/resources/computational-systems/cheyenne/running-jobs/hyper-threading-cheyenne)

.. Hint:: 
		In-case your run requires hyperthreading, it is recommended to specify ncpus = 36 and mpiprocs = 72
			For e.g in PBS script 
				- #PBS -l select=2:ncpus=36:mpiprocs=72	
  		Observation :  
			wrf_stats output shows different result based on how the cores & mpi tasks were specified in the script. 
	 		Eg :
			  	1. #PBS -l select=2:ncpus=72:mpiprocs=72 =>  XxY = 12x12	& CPU's = 144
			  	2. #PBS -l select=2:ncpus=36:mpiprocs=72 =>  XxY = 16x18 & CPU's = 288
		        Note: *XxY & CPUs are columns taken from wrf_stats output by running the following command : ./wrf_stats -t -H -d .*

- **Following are speedup comparisions when specifying:** ::
	
	PBS -l select=2:ncpus=72:mpiprocs=72
	
- **Intel 18.0.1 + MPT 2.18.**

.. image:: ../../results/new_htt_mpt.svg
    :width: 400px

- **GNU 8.1.0 + Mvapich2.2.**

.. image:: ../../results/new_htt_mvapich.svg
    :width: 400px
	
- **Intel 18.0.1 + GNU 8.1.0.**

.. Tip:: This is not an apples to apples comparision. But the scaling results above suggests GNU with MPT would do better over GNU with MVAPICH for this case.
 
.. image:: ../../results/new_htt_mvapich_mpt.svg
    :width: 400px

	
- **Following are speedup comparisions when specifying:** ::

	PBS -l select=2:ncpus=36:mpiprocs=72

- **Intel 18.0.1 MPT 2.18 NCPUS = 36**

.. image:: ../../results/new_htt_mpt_36.svg
    :width: 400px
	


Mvapich
------------------------
Mvapich provides several runtime options to optimize performance. It interfaces with [hwloc](https://www.open-mpi.org/projects/hwloc/) software package to provide various thread bindings.
Below are some comparisions done using various settings
TODO 





Misc Hybrid Runs
-------------------
Below are some other hybrid run graphs with computation times, different thread binding strategies, etc. Using omplace gives the best performance. Use dplace if you want to manually specify cpu sets.

- Intel 18.0.1 Total Computation Time

.. image:: https://raw.githubusercontent.com/DixitPatel/WRF_Simulation/master/results/intel18_openmp_67_comp.png
    :width: 400px

.. image:: https://raw.githubusercontent.com/DixitPatel/WRF_Simulation/master/results/intel17_openmp_16_comp.png
    :width: 400px

- Intel 17.0.1 Option 16 Simulation Time

.. image:: https://raw.githubusercontent.com/DixitPatel/WRF_Simulation/master/results/intel17_openmp_16_speed.png
    :width: 400px

- Intel 17.0.1 Option 67 Total Computation time and Simulation Time.

.. image:: https://raw.githubusercontent.com/DixitPatel/WRF_Simulation/master/results/intel17_openmp_67_comp.png
    :width: 300px

.. image:: https://raw.githubusercontent.com/DixitPatel/WRF_Simulation/master/results/intel17_openmp_67_speed.png
    :width: 300px
