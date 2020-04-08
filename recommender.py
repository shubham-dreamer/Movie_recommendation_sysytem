# For GUI
import recommenderGUI as gui
# For using DataFrames and importing CSV 
import pandas as pd
# Numerical python library for scikit learn
import numpy as np
# For creating numerical matrix for string feature
from sklearn.feature_extraction.text import CountVectorizer
# For finding the similarity index for each vector
from sklearn.metrics.pairwise import cosine_similarity



# Rest all will be step-by-step procedure ( Steps are indicated by S(Number) )-->

# S1 :: Reading the csv(comma seprated values) file containing the movie data
moviesData = pd.read_csv("movie_dataset.csv",  encoding= 'unicode_escape')
# Just to give sneak peak # print (data.columns)

# S2 :: Selecting features(categories) over which recomendation can be made
featuresSeclected = ['cast','keywords','genres','director','crew']

# S3 :: Creating a seprate column in moviesData for storing a combination of selected features
# Filling all the absent values with null string
for theme in featuresSeclected:
	moviesData[theme] = moviesData[theme].fillna('')

# S4 :: Combining all the features into single string value
def combine(row):
	try:
		return row['cast'] +" "+row['keywords']+" "+row["genres"]+" "+row["director"]
	except:
		print("There Is Occuring Some Error:", row)	

# S5 :: Adding combined features into newly created column
moviesData["combined_features"] = moviesData.apply(combine,axis=1)

# Another sneak peak # print "Features which get combined:", data["combined_features"].head()

# S6 :: Creating new instance for countVectorizer 
# Text to numeric conversion of all values in newly created column
featureMatrixEntity = CountVectorizer()

# S7 :: fitting all values in instance
numericMatrix = featureMatrixEntity.fit_transform(moviesData["combined_features"])

# S8 :: Finding similarity index for each vector in Matrix
similarityFinder = cosine_similarity(numericMatrix) 

# S9 :: Start binding with gui
# Add available list of movies
movieList = moviesData['original_title'].values
for name in movieList:
    gui.availList.insert(gui.tk.END,name)

# Adding event Handlers to gui list

selectValue = []
def onSelect(event):
    gui.inputBox.configure(state=gui.tk.NORMAL)
    gui.inputBox.delete(0,gui.tk.END)
    selectValue.append(event.widget.get(gui.tk.ANCHOR))
    gui.inputBox.insert(0, event.widget.get(gui.tk.ANCHOR))

# capture user input on pressing return key
def onPress(event):
		gui.inputBox.configure(state=gui.tk.DISABLED)
		gui.availList.unbind('<<ListboxSelect>>',id)

		# S11 :: Find index of the provided movie in moviesData
		movieIndex = moviesData[moviesData.title == selectValue[-1]]["index"].values[0]

		# S12 :: Get list of all the similar movies
		similarMovies =  list(enumerate(similarityFinder[movieIndex]))

		# S13 :: Sorting the list 
		sortedSimilarMovies = sorted(similarMovies, key=lambda x:x[1], reverse=True)

		# S14 :: Getting output
		getRecommendations(sortedSimilarMovies)

gui.availList.bind('<Return>', onPress)
id = gui.availList.bind('<<ListboxSelect>>', onSelect)


def getRecommendations(recMovies):
    i = 0
    for index in recMovies:
        name = moviesData[moviesData.index == index[0]]["original_title"].values[0]
        gui.outputList.insert(gui.tk.END,name)
        i += 1
        if i>50:
            break

# reset output
def reset():
    gui.inputBox.configure(state=gui.tk.NORMAL)
    id = gui.availList.bind('<<ListboxSelect>>', onSelect)
    gui.inputBox.delete(0,gui.tk.END)
    gui.outputList.delete(0,gui.tk.END)   

gui.filemenu.add_command(label='Reset', command=reset) 
gui.filemenu.add_command(label='Exit', command=gui.window.quit)

gui.window.mainloop()


