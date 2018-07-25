import os # operating system interface
import glob # access the global directory
import numpy as np # work with arrays, list, list images as arrays, etc.
import csv # read csv files
import time # call the kernel to sleep using time.sleep
from Dashboard import dashboard # data analysis dashboard function
import sys

sys.path.append('../DataAnalysis') # creates a folder called DataAnalysis in the current directory

<<<<<<< HEAD
def gettimestamp():
    """ 
    Obtain list of images captured.
    
    Returns:
    lst_of_TS: array | list of timestamps from the directory; compare these to check if new files were added      
    """ 
    lst_of_TS = []
	for file in glob.glob("*.npy"): # access every .npy file in the current directory
		name = file.split('.') 
        timestamp_str = name[0] # grab the timestamp portion 
        timestamp_int = int(timestamp_str) # convert the timestamp string into an integer
        lst_of_TS.append(timestamp_int) # append to list of timestamps
	lst_of_TS.sort() # sort the list of timestamps in increasing order
	return lst_of_TS
""" 
    Functionality 
    ---------------------------------------------------------
    i) Asks user for reaction ID (corresponds to input to Webcam Interface)
    ii) Changes working directory 
    iii) initializes variables of means and variances 
    iv) While loop is for continuous checking for new images
    

    Vars
    ---------------------------------------------------------
    path             |   user path
    reaction_id      |   reaction id for different reactions
    csvpath          |   path to csv statistics file 

    Returns
    ---------------------------------------------------------
   

i) make class
ii) initialize
iii) run
iv) class functions
"""
class CommunicationManager:


    def __init__(self):
        



    def initialize(self, path, reaction_id ):
        """ 
        Functionality 
        ---------------------------------------------------------
        i) Asks user for reaction ID (corresponds to input to Webcam Interface)
        ii) Changes working directory 
        iii) initializes variables of means and variances 
        iv) While loop is for continuous checking for new images
        

        Vars
        ---------------------------------------------------------
        path             |   user path
        reaction_id      |   reaction id for different reactions
        csvpath          |   path to csv statistics file 

        Returns
        ---------------------------------------------------------
       """

        self.path=path
        self.reaction_id=reaction_id
        # Change to directory
        path = input("Input the path to the image directory: ")
        # by default, user input is a string
        reaction_id  = input("Input the reaction ID: ")

        dirpath = os.getcwd()

        print("Current working directory: %s" % dirpath)

        os.chdir(path)
        # Check current working directory.

        dirpath = os.getcwd()


        csvname = str('summary_' +  str(reaction_id) + ".csv")
        # create path to access csv for specific reaction
        csvpath = os.path.join(dirpath, csvname) 
        # list of indices that have been worked with/sent to Data Analysis team
        self.lst_current_indices = [0] 


        # list of R,G,B means
        self.means = [] 
        # list of R,G,B variances
        self.variances = []



    def run(self):

        wait_once = 1
        
        i = 0
        
        while i==0:

           try:
                last_img_index, tempMean, tempVar = self.stats()

                self.means.append(mean_array)
                self.variances.append(var_array)

                print('means_temp:', tempMean)
                # plot the information on the dashboard
                dashboard(tempMean, tempVar, image_array) 
               
                lst_current_indices.append(last_img_index+1) 

                # Data analysis plot function(output) updates the dashboard
                time.sleep(2.)

        except IndexError:

                # Data analysis plot function(output) updates the dashboard
                time.sleep(2.)
            
            except IndexError:

                if wait_once:
                
                    time.sleep(5)
                
                    wait_once = 0
               
                else:
                    # HACK TO NOT HAVE JOB TERMINATE
                    time.sleep(5)
                
                    pass
                    # print("No more images are being added. Terminating job.")
                    # exit()

            # exit()

            # # Testing by Tim - JUST PAUSES PROCESSOR FOR 20s
            # time.sleep(20)
            # break


    def stats():

        # dashboard() - initialize dashboard
        lst_of_TS = self.gettimestamp()            
        last_img_index = lst_current_indices[-1]
        image_array = np.load(str(lst_of_TS[last_img_index])+ '.npy')
        csvfile = open(csvpath, 'r')
        reader = csv.reader(csvfile)
        my_csv_data = list(reader)
        data = my_csv_data[last_img_index] # grabs the mean & variance data of the current image        
        csvfile.close()

        mean_array = [float(data[1]), float(data[2]), float(data[3])] # create array of mean RGB values
        var_array = [float(data[4]), float(data[5]), float(data[6])]  # create array of variance of RGB values

        return last_img_index, mean_array, var_array
        # Format data for Data Analysis dashboard function 


    def gettimestamp(self):
        """ 
        Functionality 
        ---------------------------------------------------------
        gets list of images captured
        
        Returns
        ---------------------------------------------------------
        lst_of_TS  |    obtains list of timestamps from the directory, commpares to see if new files were added      
        """ 
    	
        lst_of_TS = []

    	for file in glob.glob("*.npy"): # "for every .npy file in the current directory "

    		name = file.split('.') 
    		# grab the timestamp portion 
            timestamp_str = name[0] 
    		# convert the timestamp string into an integer
            timestamp_int = int(timestamp_str) 
            # append to list of timestamps
            lst_of_TS.append(timestamp_int) 
        # sorts the list of timestamps in increasing order
    	
        lst_of_TS.sort() 

    	return lst_of_TS

