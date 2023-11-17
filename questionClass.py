# question --> Python class based on our questions in the CSV and their answers
class question:
    def __init__(self, question, topics, title, legend):
        self.question = question
        self.topics = topics
        self.title = title
        self.legend = legend

# Independant Variable questions

genderQuestion = question(question='What is your gender', topics=['Male', 'Female', 'Non-binary', 'Prefer not to say'], title='Gender', legend = None)

ageRangeQuestion = question(question='Select the age range that best suits you', topics=['Under 18', '18-24', '25-32', '32-40', '40-50', '50-64', '65+'], title= 'Age', legend = None)

educationQuestion = question(question='What is your current level of education?', topics= ['Undergraduate', 'Graduate Student', 'Masters Degree', 'PhD','College Diploma'],
                            title='Education ', legend = None)

statusQuestion = question(question='What is your current employment status?', topics=['Part-time student', 'Full-time Student', 'Professor / Faculty'],
                          title='Occupation', legend = None)

fieldStudyQuestion = question(question='What is your field of study?', topics=['Arts', 'Communication Services', 'Engineering and Archiecture', 'Sciences', 'Business', 'Other'],
                            title='Field of Study', legend = None)


# Dependant variable questions

previouslyQuestion = question(question='Have you previously used ChatGPT?', topics=['Yes', 'No', 'Experimented with Different AI tools'],
                                title='Experimented with', legend='Have you previously used ChatGPT')

plagiarismQuestion = question(question='Do you think that the use of ChatGPT causes the rates of plagiarism for students to be higher?',
                                 topics=['Yes', 'No'], title='Plagiarism with', legend='Increased Rates of Plagiarism Answers')

agreeDisagreeQuestion = question(question='Do you think it will be important for current and future students to learn to utilize AI software like ChatGPT to further their education and learning?',
                                 topics=['Strongly agree', 'Agree', 'Neutral', 'Disagree', 'Strongly Disagree'], title='Future skills using',
                                 legend='Importance of Utilized Skills Answers')

inappropriateQuestion = question(question='Suppose you use ChatGPT for the following. Select the one(s) you consider to be inappropriate use of ChatGPT.',
                                 topics=['Answers for homework/lab assignments', "Summarizing/helping you understand your professor’s lectures", 'Study preparations for test/exam', 'Personal reasons/experimentation', 'Your job'],
                                 title='Inappropriate use of', legend='Inappropriate use of ChatGPT Answers')

importantQuestion = question(question='If you agree, why is it important?', topics= ['Future job prospects will require the use of AI like ChatGPT', 'Research in academia may become heavily reliant on the quick information provided by the AI','Other reason', "Not applicable"],
                                 title='Future Education with', legend='Importance Answers')

impactQuestion = question(question="How do you think ChatGPT could impact students' learning?", 
                                 topics=['Less creativity and weaker critical thinking skills', 'Students will use it along with human taught lessons to create a more reliable learning environment', 'Some students will abuse it, like all tools, but it will be overall beneficial', 'Other Reasons'],
                                 title= 'Impact of', legend='Student Impact Answers')
