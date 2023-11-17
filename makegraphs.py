import pandas as pd
import numpy as np
import plotly.express as px
import questionClass as qc

# Pandas dataframe based on our survey responses exported to a CSV
#   All our graphs are built on this dataframe so its used as a global variable
df = pd.read_csv('chatgpt.csv')

# -------- Full Colour Palette --------
# Bar colours '#FF595E', '#FFCA3A', '#8AC926', '#1982C4', '#6A4C93'
# Font colours "#E5E4E2"
# Background colour #2d3035

# Colour palette global variables for ease of access, explained above, palette colours made on open source colour 
#   forming websites then put into hexcode as needed by Plotly library
defaultHeight = 600
lineColour = ['#FF595E', '#FFCA3A', '#8AC926', '#1982C4', '#6A4C93']
fontColour = "#E5E4E2"
backColour = '#2d3035'


# barFilter --> Is the main graphing and organization function, it takes two questions and compares them by their answers
#   topic, xValue: The first question and its answers (xaxis)
#   question, categories: The second question and its answers (bars)
def barFilter(topic, xValue, question, categories, title, xaxisTitle, yaxisTitle, mode, legend):

    # Create a new numpy array to act as our dataframe, size is based on the two question variables sizes
    newTotal = [[0]*len(categories)]*len(xValue)
    newTotal = np.array(newTotal)
    
    # Based on the catgories , we sort and check what each answer in the first questions corresponds to an answer
    #   in the second question
    for currTotal, currCategory in enumerate(categories):
        for xVal, currVal in enumerate(xValue):

            # Strip the dataframe by the first question answer, then the second question answer, then set the 
            #   corresponding numpy array index for that specific (first question + second question) pair
            #   ex; newTotal[0][1] --> Corresponds to Gender = Male, Question = Yes
            #   we find the amount of Male that answered Yes and put it in that index
            num = (df.loc[(df[topic] == currVal)].loc[(df[question].str.contains(currCategory))]).shape[0]
            newTotal[xVal][currTotal] = num


    # Create a new dataframe based on the answers above
    newdf = pd.DataFrame(newTotal, columns= categories)
    newdf.index = xValue

    # Generate a bar graph based on that dataframe and answers
    newBar = px.histogram(newdf, x = xValue, y = categories, barmode=mode, title = title, color_discrete_sequence=lineColour)

    # Customize the graph
    newBar.update_yaxes(showgrid=False)
    newBar.update_xaxes(categoryorder = 'total descending')
    newBar.update_traces(hovertemplate = None)
    newBar.update_layout(hovermode = 'x unified', xaxis_title = xaxisTitle, yaxis_title = yaxisTitle,
                    xaxis_tickangle = 360, paper_bgcolor = backColour, plot_bgcolor = backColour, title_font = dict(size=25, color = fontColour, family = "Mult, sans-serif"),
                    font = dict(color = fontColour), legend = dict(orientation = 'v', y = 1.02, yanchor = 'bottom', xanchor = 'right'),
                    margin =dict(t=100, b=0, l=70, r=40), legend_title = legend)
    
    # Show the bar graph
    newBar.show()



# makeGraphs --> Produces general bar graphs for different independant variable questions
#   more custom graphs can be made from the functions directly
def makeGraphs(question: qc.question, questionLs: list[qc.question]):
     # Loop through each depedant for a given independant and graph it, heavily reliant on the questionClass
     for currQuestion in questionLs:
            barFilter(xValue=question.topics, categories= currQuestion.topics, question=currQuestion.question, topic = question.question,
                xaxisTitle=question.title, yaxisTitle='Number of Persons', title= currQuestion.title + ' ChatGPT by ' + question.title, mode='group', legend=currQuestion.legend)



# makePie --> Makes a pie graph for a single variable / questions
def makePie(question, categories, title):

    # Make numpy array for based on the amount of answers to the question
    total = [0]*len(categories)
    total = np.array(total)

    # Loop through and add each answer
    for pos, currCategory in enumerate(categories):
        # Strips the dataframe based on the question answers and takes the total
        total[pos] = df.loc[df[question] == currCategory].shape[0]
    
    # Create piechart based on the numpyarray
    fig = px.pie(values=total, names=categories, title=title, color_discrete_sequence=lineColour)

    # Customize the way the piechart it looks
    fig.update_traces(sort=False)
    fig.update_layout(autosize = True, paper_bgcolor = backColour, plot_bgcolor = backColour, title_font = dict(size=25, color = fontColour, family = "Mult, sans-serif"),
                    font = dict(color = fontColour), legend_title = 'Categories', legend_font = dict(color = fontColour), 
                    legend = dict(orientation = 'v', y = 0.95, yanchor = 'top', xanchor = 'right'))
    
    # Show the piechart
    fig.show()
    


# makePieGraphs --> Generates pie graphs based on a list of questions
def makePieGraphs(questionLs: list[qc.question]):
    for qs in questionLs:
        makePie(question=qs.question, categories=qs.topics, title= 'Percent of people based on ' + qs.title)


# makeSingleVarBar --> Generates a bar graph with a single question/variable columns
def makeSingleVarBar(question, categories, title, xaxisTitle):
    # Make numpy array for based on the amount of answers to the question
    total = [0]*len(categories)
    total = np.array(total)

    # Loop through and add each answer
    for pos, currCategory in enumerate(categories):
        # Strips the dataframe based on the question answers and takes the total
        total[pos] = df.loc[df[question].str.contains(currCategory)].shape[0]

    # Create dataframe for better data manipulation
    data = {xaxisTitle : categories,
            'Number of persons' : total}
    newdf = pd.DataFrame(data)
    newdf['Categories']= categories


    # Make graph
    newBar = px.bar(newdf, y = 'Number of persons', x=xaxisTitle, color = 'Categories', 
                    title = title + " ChatGPT totals", color_discrete_sequence=lineColour)

    # Customize the graph
    newBar.update_yaxes(showgrid=False)
    newBar.update_traces(hovertemplate = None)
    newBar.update_layout(autosize = True, hovermode = 'x unified', xaxis_title = '', yaxis_title = "Number of Persons",
                    xaxis_tickangle = 360, paper_bgcolor = backColour, plot_bgcolor = backColour, title_font = dict(size=25, color = fontColour, family = "Mult, sans-serif"),
                    font = dict(color = fontColour), margin =dict(t=100, b=50, l=70, r=100), legend = dict(orientation = 'v', y = 0.95,  yanchor = 'bottom', xanchor = 'right'))
    newBar.update_xaxes(showticklabels = False)
    
    # Show graph
    newBar.show()


# multipleSingleBar --> Has the same function as makePieGraphs, but for bargraphs, automates the process of single variable bar graphing!
def multipleSingleBar(questionLs: list[qc.question]):
    for currQuestion in questionLs:
        makeSingleVarBar(question=currQuestion.question, categories=currQuestion.topics, title=currQuestion.title, xaxisTitle=currQuestion.title)
