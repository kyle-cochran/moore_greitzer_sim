# grid info
numthetas = 7
numts = 201

# pull data files

#   ----------------------
#   0 th order derivatives
#   ----------------------
gData = list()
with open("gData.csv", 'r') as gf:
    for num in gf:
        gData.append(float(num.strip()))
gData = np.asarray(gData)
gData = np.reshape(gData,(numthetas,numts))

phiData = list()
with open("phiData.csv", 'r') as gf:
    for num in gf:
        phiData.append(float(num.strip()))
phiData = np.asarray(phiData)
phiData = np.reshape(phiData,(numthetas,numts))

psiData = list()
with open("psiData.csv", 'r') as gf:
    for num in gf:
        psiData.append(float(num.strip()))
psiData = np.asarray(psiData)
psiData = np.reshape(psiData,(numthetas,numts))


#   ----------------------
#   1 st order derivatives
#   ----------------------
gtData = list()
with open("gtData.csv", 'r') as gf:
    for num in gf:
        gtData.append(float(num.strip()))
gtData = np.asarray(gtData)
gtData = np.reshape(gtData,(numthetas,numts))

gthetaData = list()
with open("gthetaData.csv", 'r') as gf:
    for num in gf:
        gthetaData.append(float(num.strip()))
gthetaData = np.asarray(gthetaData)
gthetaData = np.reshape(gthetaData,(numthetas,numts))

phitData = list()
with open("phitData.csv", 'r') as gf:
    for num in gf:
        phitData.append(float(num.strip()))
phitData = np.asarray(phitData)
phitData = np.reshape(phitData,(numthetas,numts))

psitData = list()
with open("psitData.csv", 'r') as gf:
    for num in gf:
        psitData.append(float(num.strip()))
psitData = np.asarray(psitData)
psitData = np.reshape(psitData,(numthetas,numts))

#   ----------------------
#   2 nd order derivatives
#   ----------------------
gtheta2Data = list()
with open("gtheta2Data.csv", 'r') as gf:
    for num in gf:
        gtheta2Data.append(float(num.strip()))
gtheta2Data = np.asarray(gtheta2Data)
gtheta2Data = np.reshape(gtheta2Data,(numthetas,numts))

#format into numpy array

# Stack 3d data into 1d
U = stackdata(cov3d)
U.reshape((1, U.size))
U.shape += (1,)

Ux = stackdata(ddx)
Uy = stackdata(ddy)
Ut = stackdata(ddt)
Ux.shape += (1,)
Uy.shape += (1,)
Ut.shape += (1,)

derivs = np.hstack([np.ones((U.size, 1)), Ux, Uy])

dependentvars = ["U", "P"]
independentvars = ["x", "y", "t"]
deriv_descrip = ['', "Ux", "Uy"]

maxpolyorder = 3

Theta, description = pdef.build_Theta(U, derivs, deriv_descrip, maxpolyorder, data_description = ["U"])

print('Candidate terms for PDE')
print(['1']+description[1:])

lam = 10**-5
d_tol = 10
a,b = Theta.shape
c = pdef.TrainSTRidge(Theta,Ut,lam,d_tol, normalize=0)
