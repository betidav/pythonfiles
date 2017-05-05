#Import modules to be used
import os,sys
import shutil
#Import image file, Background and plot them

class fileNamesInDirectory:
	def fileNames(self, path):
		files = os.listdir(path)
		"""
		This function returns an array of all the filenames in the specified path. Note that the 
		last element in the returned array maybe a 'Thumbs.db' file
		"""
		arrayOfNames = []
		for file in files:
			try:
				arrayOfNames.append(file)
			except:
				print 'error last file, # ', count, 'file', 'for more info....info@tanglatec.com'
		return arrayOfNames
		
	def folderNames(self, path):
		arrayOfNames = []
		"""
		This function returns all the foldernames in a given directory
		"""
		try:
			subdirectories = os.listdir(path)
			print subdirectories
			for i in range(0, len(subdirectories)):
				if os.path.isdir(path + subdirectories[i]):				
					arrayOfNames.append(subdirectories[i])
				else:
					print "done directoring!"
		except Exception, e:
			print "Error reading folder names ", e, 'for more info....info@tanglatec.com'
		return arrayOfNames
		
	def copyFilesFromA2B(self, source, destination):
		files = os.listdir(source)
		count = 1
		for file in files:
			try:		
				shutil.copy(source+str(file),destination+str(file))
				count+=1
			except Exception, e:
				print "Error reading file names: Check detination folder to see if all files have been copied", 
				e, 'for more info....info@tanglatec.com'

def func():
	A = fileNamesInDirectory()
	#name = A.folderNames(r"\\nt4\milab\WP3 LFI\photonics\SQUID-miLFI_01\sweep\03-05-2017\Set1/")
	name = A.copyFilesFromA2B(r"\\nt4\milab\WP1 COL\photonics\Setups overview/", r"\\nt4\milab\WP1 COL\photonics\Setups overview\rr/")
	print name
func()
