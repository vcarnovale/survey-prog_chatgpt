============= General Overview =============

The purpose of this program, makegraphs is to create graphs based on a CSV generated from google forms

There are three 5 files including this one, and 1 folder in the .zip, they are 
  * The CSV renamed to chatgpt.csv for convience based on the results of our google forms
  * The main graphing class makegraphs.py, which contains the formatting and methods for making the graphs, and automating making graphs
  * questionClass.py, holds the data for questions and their answers in a class format for easy importing
  * The run function that was used for generating our graphs, that is generategraphs.py
  * A folder containing all of the graphs generated as pngs


== Libraries ==

We use 3 main external libraries, all available through pip/pip3
  * plotly, specifically plotly.express to create the graphs
  * pandas, to make our CSV into a manipulateable dataframe in python
  * numpy, for nice arrays :)


Note on Plotly: We decided on the use of plotly due to its generally more friendly layout manipulation, matplotlib was also considered
        but we found Plotlys library, namely plotly.express, to be a generally better library for our purposes



============= Programs =============

Two files are of note that we wanted to explain a little more deeply here.

== generateGraphs.py ==

The first is more simple, the run function generategraphs.py, this file was used for generating the graphs we specifically used
  the basic formatting is explained within the file, this file *DOES NOT* generate every possible graph based on our data, just the
  ones requested for the paper, extra graphs generated that are not included in the paper itself are within an attached folder.

  generateGraphs has seperate possible answers in the run, a lot of them are pretty self explanatory, the weirded one being custom
    these are custom functions we made that weren't automated, automation of these functions would lead to some weird looking graphs,
    so we decided that for those few graphs we could customize the way they look and act using the direct graph creation functions in
    makegraph.py explained below


== makeGraphs.py ==

The second is slightly more complicated in form, makegraphs.py, this file generates graphs using functions which separate data,
  and graphs them, but it also contains functions that automate the process of graphing specific sets of data that are similar
  in nature

  The graph creation functions, namely barFilter, makePie, makeSingleVar, are all useable as individual functions and are more
    customizable when used alone.

  The automation functions makeGraphs, makePieGraphs, multipleSingleBar, just automate the process of this for specific purposes
    the titles and axis are generic and dependent on the questionClass, namely questionClass.title for each question answer
