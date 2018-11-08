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
        "Student Mentor  |  Udacity                                                                                            11/2011 -  Present":
        "\nMentoring Students through the Introduction to Programming Nanodegree by:                                                     Gig/Remote\
          * Perform code reviews with constructive feedback\
        \n* Motivate & Advise students\
        \n* Consistent 5-star ratings",

        "\nSoftware Development Student  |  Self                                                                               07/2016 - Present":
        "\nExecuting a career change via Full-Time Learning:                                                                               Seattle\
          * Study Computer Science fundamentals, then Statistics, Linear Algebra, Calculus; finally specializing in Machine Learning\
        \n* Also, renovate my home and occasionally volunteer (e.g. Seattle Startup Week) or complete some contract IT work",

        "\nProperty Management  |  Essex & W.N.G.                                                                             05/2009 -  07/2016":
        "\nRoles equivelent to business manager, bookkeeper or office manager:                                         Seattle & Orange County, CA\
          * Managed up to 7 people, onsite and semi-remote\
        \n* Grew business 7%\
        \n* Awarded for customer satisfaction\
        \n* Reduced turnover by 42%"
        }

    education = {
        "Machine Learning Engineer Nanodegree  | Udacity                                                                       01/2018 - 09/2018":
        "\nMastering Model Evaluation/Validation, Supervised Learning, Deep Learning, Unsupervised Learning, Reinforcement Learning through hands-on learning",

        "\nMachine Learning with Tensorflow on Google Cloud Platform  | Coursera                                               07/2018 - 08/2018":
        "\n5 course specialization by Google Cloud on how Google creates scalable and deployable Machine Learning models",

        "\nIntroduction to Programming Nanodegree  |  Udacity                                                                  09/2016 - 01/2017":
        "\nStarted with learning web technologies then built a strong foundation for serious programming in Python and specialized in Data Analysis",
        }

    projects = {
        "NYC Taxi Fare Prediction - Capstone Project and Kaggle Competition  |  Udacity                                                  09/2018":
        "\n* Successfully deployed a state-of-the-art Wide and Deep TensorFlow regressor\
        \n* Production-ready and scalable in Cloud ML Engine\
        \n* Explored & cleaned 55 million row dataset\
        \n* Placed within top third on the leaderboard with 3.26 RMSE (within 2 points of the top score)",

        "\nReinforcement Learning Quadcopter  |  Udacity                                                                                 04/2018":
        "\n* Trained a quadcopter simulation to maintain stable flight within 300 episodes\
        \n* Implemented a Deep Deterministic Policy Gradients (DDPG) Actor/Critic model",

        "\nCreating Customer Segments  |  Udacity                                                                                        04/2018":
        "\n* Used unsupervised learning techniques to see if any similarities exist between a wholesale distributor's customers,\
        \n  and how to best segment customers into distinct categories",

        "\nDog Breed Classifier  |  Udacity                                                                                              04/2018":
        "\n* Given an image of a dog, my DCN identifies an estimate of the canine’s breed,\
        \n  but if supplied with an image of a human or other non-dog, the code identifies the resembling dog breed",

        "\nRecycle Bits  |  Hackathon                                                                                                    02/2018":
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
                 comfortable_with=['Python', 'Data Analysis', 'Machine Learning' 'TensorFlow', 'Keras', 'scikit-learn', 'HTML & CSS', 'Google Cloud (GCP)'],
                 familiar_with = ['Git', 'JSON', 'SQL', 'C#', 'Javascript']):

        self.comfortable_with = comfortable_with
        self.familiar_with = familiar_with

    def comfortable(self):
        return self.comfortable_with

    def familiar(self):
        return self.familiar_with
