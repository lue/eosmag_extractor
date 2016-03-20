from subprocess import Popen, PIPE

def get_eosmag14(Zion, CMI, B12, T6, RHO):
    bp = Popen('./a.out %e %e %e %e %e'%(Zion, CMI, B12, T6, RHO), shell=True, stdout=PIPE, stdin=PIPE, stderr=PIPE)
    _ = bp.stdout.readline()
    _ = bp.stdout.readline()
    _ = bp.stdout.readline()
    _ = bp.stdout.readline()
    names = bp.stdout.readline()
    _ = bp.stdout.readline()
    _ = bp.stdout.readline()
    result = bp.stdout.readline()
    result = result.split()
    result = [float(i) for i in result]
    return names, result

print('Column names:')
names, result = get_eosmag14(30,50,0,101,1e13)
print(names)
print('Array with results:')
print(result)
