


'''
Overview:
*input: 
*
'''

import sys, os
import numpy as np
from numpy.linalg import svd
import scipy.misc as sm
import pylab as pl
import sift
import random

import scipy.ndimage as nd

import time
import pdb


class Classifier:

	def __init__(self, baseDir=None):
	
		self.img = None
		
		if baseDir == None:
			self.baseDir = sys.argv[0][0:sys.argv[0].rfind('/')+1] + 'data/'

		self.all_features = []
		self.all_names = []
		
		self.walk_dirs()
		self.get_all_features()		
		
		
	def get_names(self):
		return self.all_names
			
			
	def run(self,img):
		self.img = img
		current_feat, current_locs = self.extract_features()
		scores, locs = self.match_all(current_feat, current_locs)
		
		return scores, locs
		


	def walk_dirs(self):

		dirs = os.walk(self.baseDir)

		root = []
		folders = []
		files = []
		self.sift_filenames = []

		for i in dirs:
			root.append(i[0])
			folders.append(i[1])
			files.append(i[2])

		for i in range(len(root)):
		#			for j in range(len(folders)):
#			if root[i].find("pointclouds_"):
			for j in range(len(files[i])):
				if files[i][j].find("_sift")>-1 and \
					 files[i][j].find('_tmp')<0 and \
					 files[i][j].find('img')<0 and \
					 files[i][j].find('~')<0 and \
					 files[i][j].find('current')<0:
					 
					self.sift_filenames.append(root[i]+'/'+files[i][j])	
					end_name_ind = files[i][j].rfind('_sift')
					self.all_names.append(files[i][j][:end_name_ind])
#					print files[i][j][:end_name_ind]

		self.fileCount = len(self.sift_filenames)

			
	def get_all_features(self):
#		pdb.set_trace()
		for i in range(self.fileCount):
			filename = self.sift_filenames[i]
			#read_features_from_file returns [locs,desciptors].Only look at descriptors
			self.all_features.append(sift.read_features_from_file(filename)[1])
		
		
		
			
			
	def extract_features(self):

		if self.img != None:
			im = sm.toimage(self.img)
			imageName = self.baseDir+'current_sift_img.pgm'
			im.save(imageName)
	#		im.save('sift/tmp_sift_img.pgm')		
			outputName = self.baseDir+'current_sift_all'
	#		outputName_tmp = baseDir+'current_sift_tmp'	
			os.system(self.baseDir+"../sift/sift <"+imageName+">"+outputName)
	#		sift.process_image(imagename, 'tmp_features')
	#		self.append_sift(outputName_tmp, outputName)

			current_desc = sift.read_features_from_file(outputName)
			current_locs = current_desc[0]
			current_features = current_desc[1]			

		else:
			print 'No image loaded into feature extractor!'
			current_features = []
					
		return current_features, current_locs

		
		
		
	def match_all(self,current_features, current_locs):
#		match = []
		locs = []
		match = np.zeros(self.fileCount)
#		pdb.set_trace()
		for i in range(self.fileCount):
			try:

				desc_prob = self.match_keys(current_features,self.all_features[i])
#				pdb.set_trace()
		# Find joint / exclusive
#				sum_tmp = np.sum(desc_prob > 0) #orig
				sum_tmp = np.sum(desc_prob)
				len_M = self.all_features[i].shape[0]
				len_S = current_features.shape[0]				
				match[i] = sum_tmp*1.0 / float(len_M+len_S-sum_tmp)
		# Find locations from nonzeros
				ind = np.nonzero(desc_prob)[0]
				xs = current_locs[ind,1]
				ys = current_locs[ind,0]
				pos = np.array([xs, ys], int).T
				locs.append(pos)
				
			except:
				match[i] = 0.0
			
		return match, locs
		
		
	def match_keys(self, sceneFeat, modelFeat):
#		pdb.set_trace()
		desc1=sceneFeat
		desc2=modelFeat
		
		dist_ratio=.6 #0.6
		desc1_shape = desc1.shape[0]
		
		matchscores=np.zeros(desc1_shape)
		
		dotProds = np.dot(desc1,desc2.T)
		dotProds *=.9999
		
		acos_dots= np.arccos(dotProds)
		indx = np.argsort(acos_dots,axis=1)
		
		range_ind = range(desc1_shape)
#		sig_keys = np.array(acos_dots[0,indx[:,0]] < dist_ratio * acos_dots[0,indx[:,1]])
		sig_keys = np.array(acos_dots[range_ind,indx[:,0]] < dist_ratio * acos_dots[range_ind,indx[:,1]])
		sig_keys_ind = np.nonzero(sig_keys)[0]
#		matchscores[sig_keys_ind] = indx[sig_keys_ind,0]*1.0 / modelFeat.shape[0] # this is done elsehere!
		matchscores[sig_keys_ind] = indx[sig_keys_ind,0] # original
#		pdb.set_trace()

		return matchscores		
		
		
		
		
		
		
	def match_files(self, sceneFile, modelFile):
		sceneFeat = sift.read_features_from_file(sceneFile)[1]
		
		try:
			modelFeat = sift.read_features_from_file(modelFile)[1]
		except:
			return
		
		desc1=sceneFeat
		desc2=modelFeat
		
#		pdb.set_trace()			
		
#		t1=time.time()
		dist_ratio=.6
		desc1_shape = desc1.shape[0]
		
		matchscores=np.zeros(desc1_shape)
		
		dotProds = np.dot(desc1,desc2.T)
		dotProds *=.9999
		
		acos_dots= np.arccos(dotProds)
		indx = np.argsort(acos_dots,axis=1)
		
		range_ind = range(desc1_shape)
#		sig_keys = np.array(acos_dots[0,indx[:,0]] < dist_ratio * acos_dots[0,indx[:,1]])
		sig_keys = np.array(acos_dots[range_ind,indx[:,0]] < dist_ratio * acos_dots[range_ind,indx[:,1]])
		sig_keys_ind = np.nonzero(sig_keys)[0]
		matchscores[sig_keys_ind] = indx[sig_keys_ind,0]
#		print 'T1:',time.time()-t1
#		t2=time.time()
#		other=sift.match(desc1,desc2)
#		print 'T2:',time.time()-t2		
#		pdb.set_trace()

		return matchscores
		
		
		
		
		
