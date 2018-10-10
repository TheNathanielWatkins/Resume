'''
Note, I know this probably isn't the best way to generate a notebook that displays resume elements,
but I thought it'd be fun to do this with actual code.

This file of helper functions allows the notebook to be cleaner and allowed for me to have some fun with import statements.
'''


def display(type, plain_format=False):
    '''
    Returns a dict for work experience, education, or projects based on what type was requested.

    Change plain_format to True for the function to actually print the text.
    It's set to False by default so that I could display the text with some Markdown formatting instead of the plain print output.
    It's recommended to delete the duplicate Markdown cells if toggling this to True.
    '''
    work = {
        "Student Mentor  |  Udacity                                                                                                 Nov 17 -  Present":
        "\nMentoring Students through the Introduction to Programming Nanodegree by:                                                         Gig/Remote\
          * Perform code reviews of student projects with constructive feedback\
        \n* Send regular encouragement and check-ins to help students stay motivated\
        \n* Provide advice when students are feeling lost or don't know where to begin,\
        \n  and help students troubleshoot and/or debug any issues they're facing",

        "\nSoftware Development Student & Home Renovations Project Manager  |  Self                                                   July 16 - Present":
        "\nTook a career break to:                                                                                                          Seattle, WA\
          * Study Software Development fundamentals, then Statistics, Linear Algebra, Calculus; finally specializing in Machine Learning\
        \n* Perform major renovations on my home including restoring wood, removing walls, adding closets, and more\
        \n* Also, occasionally volunteer (e.g. Seattle Startup Week) or complete some contract IT work",

        "\nAssistant Property Manager (Office Manager/Bookkeeper)  |  Essex Property Trust                                            Mar 14 -  July 16":
        "\n#1 West Coast Focused Real Estate Investment Trust:                                                                              Seattle, WA\
          * Managed up to 7 people, onsite and semi-remote\
        \n* Drove rent growth while maintaining minimal resident turnover and increasing customer satisfaction\
        \n* Fostered trust between disparate departments and improved many processes/procedures\
        \n* Consistently turned negative customer experiences into an ultimate positive by listening,\
        \n  applying creative solutions, and ensuring that they felt and served",

        "\nProperty Manager (Business Manager)  |  Western National Group                                                              May 09 -  Feb 14":
        "\nPremier property management company setting high standards to be a cut above:                                              Orange County, CA\
          * Developed a strong reputation for customer service and mentoring new hires\
        \n* Redirected the NOI trends from -5% to +2% budget variance and reduced annual turnover from 71% to 29%, receiving industry awards",
        }

    education = {
        "Machine Learning Engineer Nanodegree  | Udacity                                                                             Jan 18 - Sept 18":
        "\nMastering Model Evaluation/Validation, Supervised Learning, Deep Learning, Unsupervised Learning, Reinforcement Learning through hands-on learning",

        "\nMachine Learning with Tensorflow on Google Cloud Platform  | Coursera                                                       July 18 - Aug 18":
        "\n5 course specialization by Google Cloud on how Google creates scalable and deployable Machine Learning models",

        "\nIntroduction to Programming Nanodegree  |  Udacity                                                                          Sept 16 - Jan 17":
        "\nStarted with learning web technologies then built a strong foundation for serious programming in Python and specialized in Data Analysis",

        "\nMechanical Engineering  |  University of California, Irvine                                                                Fall 06 - Fall 07":
        "\n46 Units towards a Bachelor’s of Science in Mechanical Engineering"
        }

    projects = {
        "NYC Taxi Fare Prediction - Capstone Project and Kaggle Competition  |  Udacity                                                       Sept 18":
        "\n* Created a production-ready Wide and Deep TensorFlow regressor deployed in Google Cloud ML Engine and trained on a massive dataset\
        \n* Placed within top third with 3.26 RMSE (less than 2 points away from the top score)",

        "\nReinforcement Learning Quadcopter  |  Udacity                                                                                         Apr 18":
        "\n* Trained a quadcopter simulation to fly using a Deep Deterministic Policy Gradients model",

        "\nCreating Customer Segments  |  Udacity                                                                                                Apr 18":
        "\n* Used unsupervised learning techniques to see if any similarities exist between a wholesale distributor's customers,\
        \n  and how to best segment customers into distinct categories",

        "\nDog Breed Classifier  |  Udacity                                                                                                      Apr 18":
        "\n* Given an image of a dog, my CNN identifies an estimate of the canine’s breed,\
        \n  but if supplied with an image of a human or other non-dog, the code identifies the resembling dog breed",

        "\nRecycle Bits  |  Hackathon                                                                                                            Feb 18":
        "\n* Earned 2nd place using Computer Vision to classify trash into distinct categories of Recyclable, Compostable or Refuse\
        \n* First implemented as a responsive web app for consumers, with a leaderboard system to encourage green behavior\
        \n* Also envisioned a business plan to create smart trash cans and automated industrial trash sorting"
        }

    if not plain_format:
        return
    elif plain_format:
        if type is 'Experience':
            for job, description in work.items():
                print(job, description)
        elif type is 'Education':
            for school, description in education.items():
                print(school, description)
        elif type is 'Projects':
            for project, description in projects.items():
                print(project, description)
        else:
            return "I'm not quite sure what you're asking to be displayed here, but I'd be happy to help however possible!  \
                    Please make sure the input variable matches either 'Experience', 'Education', or 'Projects'.  \
                    If none of those seems right, please contact me @theNathanielW"

class skills():
    '''
    Returns a list of skills that I'm comfortable with and familiar with, depending on which function is called.
    And yes, I know this is overkill for returning 2 lists.
    '''
    def __init__(self,
                 comfortable_with=['Python', 'Jupyter Notebooks', 'TensorFlow', 'Keras', 'scikit-learn', 'Anaconda', 'HTML & CSS'],
                 familiar_with = ['Git', 'JSON', 'SQL', 'C#', 'Javascript']):

        self.comfortable_with = comfortable_with
        self.familiar_with = familiar_with

    def comfortable(self):
        return self.comfortable_with

    def familiar(self):
        return self.familiar_with
