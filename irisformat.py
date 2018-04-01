# Wayne Reilly 31/03/2018
# Formatting the Iris Flower Dataset https://archive.ics.uci.edu/ml/datasets/iris
# Dataset introduced by Ronald Fisher in 1936 https://en.wikipedia.org/wiki/Iris_flower_data_set
# Help with formatting https://stackoverflow.com/questions/10623727/python-spacing-and-aligning-strings

headers = 'Sepal Length / Sepal Width / Petal Length / Petal Width / Species'#variable containing the headings for each column of iris data

with open("data/iris.csv") as f:# opens the iris.csv file. Using the "with" command means I don't have to use the close command at the end
  print(headers.upper())# prints the varible headers, all in uppercase
  for line in f:# starts a for loop
    print(line[0:3].rjust(7),line[4:7].rjust(14),line[8:11].rjust(13),line[12:15].rjust(14),line[16:-1].rjust(17))
  # I know this is a 'clunky' way to format the data, but it's the best I can do for now
  # It also took some trial and error to get the aligment correct
