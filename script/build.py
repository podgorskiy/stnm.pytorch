import os
import torch
from torch.utils.ffi import create_extension

#this_file = os.path.dirname(__file__)

sources = ['src/stnm.c']
headers = ['src/stnm.h']
defines = []
with_cuda = False

if torch.cuda.is_available():
    print('Including CUDA code.')
    sources += ['src/stnm_cuda.cpp']
    headers += ['src/stnm_cuda.h']
    defines += [('WITH_CUDA', None)]
    with_cuda = True

this_file = os.path.dirname(os.path.realpath(__file__))
print(this_file)
extra_objects = ['src/stnm_cuda_kernel.cu.o']
extra_objects = [os.path.join(this_file, fname) for fname in extra_objects]

ffi = create_extension(
    '_ext.stnm',
    headers=headers,
    sources=sources,
    define_macros=defines,
    relative_to=__file__,
    with_cuda=with_cuda,
    extra_objects=extra_objects,
    extra_compile_args=["-std=c99"],
    libraries=['cudart_static', '_C', 'caffe2_gpu', 'caffe2']
)

if __name__ == '__main__':
    ffi.build()
