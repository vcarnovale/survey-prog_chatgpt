import makegraphs as mg
import questionClass as qc

# Generates the graphs we needed for the paper
if __name__ == '__main__':
    # Full list of questions
    dependantQuestions = [qc.previouslyQuestion, qc.plagiarismQuestion, qc.importantQuestion, qc.impactQuestion, qc.inappropriateQuestion,
                          qc.agreeDisagreeQuestion]
    
    while (True):
        graphIndenpendant = input('Choose; gender, age, occupation, degree, field, piegraphs, singlebar, custom, quit: ')
        # Independent graphs
        if (graphIndenpendant == 'gender'):
            mg.makeGraphs(qc.genderQuestion, dependantQuestions)
        elif (graphIndenpendant == 'age'):
            mg.makeGraphs(qc.ageRangeQuestion, dependantQuestions)
        elif(graphIndenpendant == 'occupation'):
            mg.makeGraphs(qc.statusQuestion, dependantQuestions)
        elif(graphIndenpendant == 'degree'):
            mg.makeGraphs(qc.educationQuestion, dependantQuestions)
        elif(graphIndenpendant == 'field'):
            mg.makeGraphs(qc.fieldStudyQuestion, dependantQuestions)
        elif(graphIndenpendant == 'piegraphs'):
        # Dependent graphs
            mg.makePieGraphs([qc.ageRangeQuestion, qc.genderQuestion, qc.fieldStudyQuestion, qc.educationQuestion, qc.statusQuestion])
        elif(graphIndenpendant == 'singlebar'):
            mg.multipleSingleBar(dependantQuestions)
        # Generates particular stylized graphs, not automated like the above graphs
        elif(graphIndenpendant == 'custom'):
            mg.barFilter(xValue=qc.previouslyQuestion.topics, topic=qc.previouslyQuestion.question, question=qc.plagiarismQuestion.question, 
                        categories=qc.plagiarismQuestion.topics, xaxisTitle=qc.previouslyQuestion.question, yaxisTitle="Number of Persons", mode='group',
                        title="People who used ChatGPT vs Thoughts on Rates of Plagiarism", legend="Do you think ChatGPT causes higher rates of Plagiarism")
            mg.barFilter(xValue=qc.agreeDisagreeQuestion.topics, topic=qc.agreeDisagreeQuestion.question, question=qc.importantQuestion.question, 
                        categories=qc.importantQuestion.topics, xaxisTitle=qc.agreeDisagreeQuestion.question, yaxisTitle="Number of Persons", mode='group',
                        title="The future of ChatGPT vs The Importance of ChatGPT", legend=qc.importantQuestion.question)
            mg.barFilter(xValue=qc.agreeDisagreeQuestion.topics, topic=qc.agreeDisagreeQuestion.question, question=qc.impactQuestion.question, 
                        categories=qc.impactQuestion.topics, xaxisTitle=qc.agreeDisagreeQuestion.question, yaxisTitle="Number of Persons", mode='group',
                        title="The future of ChatGPT vs How ChatGPT Impacts Students", legend=qc.impactQuestion.question)
            mg.barFilter(xValue=qc.agreeDisagreeQuestion.topics, topic=qc.agreeDisagreeQuestion.question, question=qc.plagiarismQuestion.question, 
                        categories=qc.plagiarismQuestion.topics, xaxisTitle=qc.agreeDisagreeQuestion.question, yaxisTitle="Number of Persons", mode='group',
                        title="Rates of Plagiarism vs Future student learning in ChatGPT", legend=qc.plagiarismQuestion.question)
            mg.barFilter(xValue=qc.inappropriateQuestion.topics, topic=qc.inappropriateQuestion.question, question=qc.plagiarismQuestion.question, 
                        categories=qc.plagiarismQuestion.topics, xaxisTitle=qc.inappropriateQuestion.question, yaxisTitle="Number of Persons", mode='group',
                        title="Rates of Plagiarism vs Inappropriate use of ChatGPT", legend=qc.plagiarismQuestion.question)
            mg.barFilter(xValue=qc.educationQuestion.topics, topic=qc.educationQuestion.question, question=qc.fieldStudyQuestion.question, 
                        categories=qc.fieldStudyQuestion.topics, xaxisTitle=qc.educationQuestion.question, yaxisTitle="Number of Persons", mode='group',
                        title="Education level vs Field of Study", legend=qc.fieldStudyQuestion.question)
        elif(graphIndenpendant == 'q' or graphIndenpendant == 'quit'):
            quit()
        else:
            print('Input error, try again')
