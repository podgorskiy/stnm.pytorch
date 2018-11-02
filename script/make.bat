call "%VS140COMNTOOLS%\VsDevCmd.bat"
set VS90COMNTOOLS=%VS140COMNTOOLS%

nvcc -c -o src/stnm_cuda_kernel.cu.o src/stnm_cuda_kernel.cu -x cu -Xcompiler "/MD" -v -gencode arch=compute_61,code=sm_61 -use_fast_math 
