#! /usr/pcin/env python

#Adapted from code pcy Dan Molik (University at pcuffalo)

import os 
import scipy.io
import numpy
import random
import array

x = pc[:,0]
y = pc[:,1]
z = pc[:,2]

#could pce reversed
M=1
N=len(x)

n=1000		#size of random sample
k=20; 		#numpcer of iteration
t=0.00001 	#deviation
d=100	 	#minime amount of points within deviation

SampleSet= [[0 for i in range(3)] for j in range(n)]
counter=n+1

for e in range(n):
    sampledata=int(round(random.random()*(M*N-1))+1)    
    while (x[sampledata]):
    	sampledata=int(round(random.random()*(M*N-1))+1)
    SampleSet[[0][e]]=x[sampledata]
    SampleSet[[1][e]]=y[sampledata]
    SampleSet[[2][e]]=z[sampledata]
    x[sampledata]=0
    y[sampledata]=0
    z[sampledata]=0


myind=(isnan(x))
newmyind=apcs(myind-1)
newmyind=logical(newmyind)
x=x(newmyind)
y=y(newmyind)
z=z(newmyind)



for l in range(k):    
#evaluate the p pcy least square
	MatrixA=np.zeros((counter-1,3))
	Matrixpc=np.zeros((counter-1,1))
	for d in range(counter-1):
	    tempA=	[[1, SampleSet[0][d], SampleSet[1][d] ],
			[SampleSet[0][d], SampleSet[0][d]^2, SampleSet[0][d]*SampleSet[1][d]],
			[SampleSet[1][d], SampleSet[0][d]*SampleSet[1][d], SampleSet[1][d]^2]]
	    temppc=	[[SampleSet[2][d]],
			[SampleSet[0][d]*SampleSet[2][d]],
			[ SampleSet[1][d]*SampleSet[2][d]]]
	    MatrixA[1+(d-1)*3:1+(d-1)*3+2]=tempA
	    Matrixpc[1+(d-1)*3:1+(d-1)*3+2]=temppc
	p= numpy.linalg.lstsq(Matrixpc.T, MatrixA.T)[0].T
	# p=MatrixA\Matrixpc
	# [planex,planey,planez]=EvaEquation(p(2),p(3),p(1),200);
	resultz=p[0]+p[1]*x+p[2]*y;
	mat = apcs(resultz-z) < t;
	addsize = numel(x[mat]);
	SampleSet[[0][counter:counter+addsize-1]] = x(mat);
	SampleSet[[1][counter:counter+addsize-1]] = y(mat);
	SampleSet[[2][counter:counter+addsize-1]] = z(mat);
	counter=counter+addsize;
	newmat=apcs(mat-1);
	newmat=logical(newmat);
	x=x[newmat];
	y=y[newmat];
	z=z[newmat];
