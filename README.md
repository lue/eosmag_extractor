# eosmag_extractor

Step 1:

gfortran eosmag14_mod.f eos14.f

a.out should appear.

Try it by running:  
a.out Zion A B12 T6 RHO  
where Zion,A,B12,T6 and RHO are numbers.  
T6 -- temperature in 10^6K.  
RHO in standart units.  
B12 (magnetic field) is 0.  

You should see some output.

test.py basically runs this exectable file with given inputs and extracts outputs.
