'''
Note, I know this probably isn't the best way to generate a notebook that displays resume elements,
but I thought it'd be fun to do this with actual code.
'''


def display(type, print_format=False):
    '''
    Returns a dict for work experience, education, or projects based on what type was requested.
    '''
    work = {
        "Student Mentor  |  Udacity                                                                                                 Nov 17 -  Present":
        "\nMentoring Students through the Introduction to Programming Nanodegree by:                                                         Gig/Remote\
    * Perform code reviews of student projects\
        \n    * Send regular encouragement and check-ins to help students stay motivated\
        \n    * Be available to answer questions at all hours, day or night\
        \n    * Provide advice when students are feeling lost or don't know where to begin\
        \n    * Help students troubleshoot and/or debug any issues they're running into",

        "\nSoftware Development Student & Home Renovations Project Manager  |  Self                                                   July 16 - Present":
        "\nTook a career break to:                                                                                                          Seattle, WA\
    * Study Software Development fundamentals, then specializing in Machine Learning\
        \n    * Perform major renovations on my home including restoring wood, removing walls, adding closets, and more\
        \n    * Also, occasionally volunteer or complete some contract work",

        "\nAssistant Property Manager (Office Manager/Bookkeeper)  |  Essex Property Trust                                            Mar 14 -  July 16":
        "\n#1 West Coast Focused Real Estate Investment Trust:                                                                              Seattle, WA\
    * Managed up to 7 people, onsite and semi-remote\
        \n    * Drove rent growth while maintaining minimal resident turnover and increasing satisfaction\
        \n    * Improved many processes/procedures and resolved decades-old discrepancies in the books\
        \n    * Fostered trust between disparate departments through shared goals and open communication\
        \n    * Consistently turned negative customer experiences into an ultimate positive by listening,\
        \n      applying creative solutions and going the extra mile to ensure that they felt cared for and served",

        "\nProperty Manager (Business Manager)  |  Western National Group                                                              May 09 -  Feb 14":
        "\nPremier property management company setting high standards to be a cut above:                                              Orange County, CA\
    * Developed a strong customer service reputation\
        \n    * Redirected the NOI trends from -5% to +2% budget variance\
        \n    * Reduced annual turnover from 71% to 29%, receiving industry awards for these accomplishments",
        }

    education = {
        "Machine Learning Engineer Nanodegree  | Udacity                                           Jan 18 - Current (anticipated graduation: June 18)":
        "\n* Mastering Model Evaluation/Validation, Supervised Learning, Deep Learning, Unsupervised Learning, Reinforcement Learning\
        \n* Building effective ML models and learning to solve real-world problems across a wide array of fields",

        "\nIntroduction to Programming Nanodegree  |  Udacity                                                                          Sept 16 - Jan 17":
        "\n* Started with learning web technologies then built a strong foundation for serious programming in Python\
        \n* Specialized in Data Analysis due to its relation to Machine Learning\
        \n* Further prepared for Machine Learning by taking courses in Linear Algebra, Statistics, and other related subjects",

        "\nMechanical Engineering  |  University of California, Irvine                                                                Fall 06 - Fall 07":
        "\n* 46 Units towards a Bachelor’s of Science in Mechanical Engineering"
        }

    projects = {
        "Creating Customer Segments  |  Udacity                                                                                                Apr 18":
        "\n* Used unsupervised learning techniques to see if any similarities exist between a wholesale distributor's customers,\
        \n  and how to best segment customers into distinct categories",

        "\nDog Breed Classifier  |  Udacity                                                                                                      Apr 18":
        "\n* Given an image of a dog, my algorithm identifies an estimate of the canine’s breed,\
        \n  but if supplied with an image of a human or other non-dog, the code identifies the resembling dog breed",

        "\nRecycle Bits  |  Hackathon                                                                                                            Feb 18":
        "\n* Earned 2nd place using Computer Vision to classify trash into distinct categories of Recyclable, Compostable or Refuse\
        \n* First implemented as a responsive web app for consumers, with a leaderboard system to encourage green behavior\
        \n* Also envisioned a business plan to create smart trash cans that tell people which bin to put their trash into,\
        \n  and industrial applications to create automated sorting for trash companies"
        }

    if not print_format:
        return
    elif print_format:
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
