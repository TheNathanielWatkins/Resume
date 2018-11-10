# Nathaniel Watkins Resume
> I previously decided to write my resume using Python (some Markdown) and a Jupyter Notebook!  Because, why not?
Well, it turned out that even a Jupyter-inspired resume is not very ATS friendly or easily scannable within the first 5-6 seconds that most people spend looking at a resume.  So, I've done a complete rewrite of my resume which can be viewed here: [Nathaniel Watkins Resume.pdf](https://github.com/TheNathanielWatkins/Resume/blob/master/Nathaniel%20Watkins%20Resume.pdf)

## Legacy Versions (aka actual resumes made from notebooks)
- All legacy versions of the resume will continue to live here in the [Legacy Version](https://github.com/TheNathanielWatkins/Resume/tree/master/Legacy%20Version) folder.
- All the legacy files will all contain "-v1.x" at the end of their file names,
 - except `Nathaniel_Watkins.py` as adding the version number would break compatibility.
- The 2 versions of legacy notebooks with `Nathaniel_Watkins.py` will be updated occasionally with wording from the current resume,
 - but the below steps to create a specifically formatted PDF with OCR'd text will not be followed.
- The hybrid resume [Nathaniel Watkins Resume-v1.5.pdf](https://github.com/TheNathanielWatkins/Resume/blob/master/Legacy%20Version/Nathaniel%20Watkins%20Resume-v1.5.pdf) will see even less frequent wording updates.

I still think this is a cool idea, but do recognize that it is the wrong strategy for the primary target audience.
> In what may be a first, this project created an _amazing_ resume from a Jupyter Notebook and a Python file.

## Features
- Communicates my unique strengths in a novel way
- Tells my background in a simple and familiar (to some) format
- Provides several ways for you to get a hold of me so we can further explore working together
- It's fun

## Getting Started

This notebook does not rely on any external packages except for the included `Nathaniel_Watkins.py` file, just make sure it's in the same folder as `Nathaniel_Watkins_Resume.ipynb`.

Open `Nathaniel_Watkins_Resume.ipynb` in Jupyter.

### To get the formatting the way I wanted, I had to perform the following tweaks
- Rotate my 1920 x 1080 monitor to portrait mode at 1080 x 1920 (allows the notebook to fill the screen better)
- Modify the `custom.css` file for my Jupyter installation to make the notebook fill the width to 97% of the browser window
  - By adding this line: `.container { width:97% !important; }`
  - See [Gerenuk's](https://stackoverflow.com/users/815443/gerenuk) answer here: [How do I increase the cell width of the Jupyter/ipython notebook in my browser?](https://stackoverflow.com/questions/21971449/how-do-i-increase-the-cell-width-of-the-jupyter-ipython-notebook-in-my-browser)
- Add an 85% zoom option to Chrome
  - See the 2nd part of [yurkennis'](https://superuser.com/users/53983/yurkennis) answer here: [How do I set a custom zoom in Chrome?](https://superuser.com/questions/463185/how-do-i-set-a-custom-zoom-in-chrome)
- Also, I had previously changed my default fonts in Chrome because I liked these better:
  - Sans-serif: `Calibri Light`
  - Fixed-width: `Consolas`

### Once I had a properly formatted screenshot, to create a linked and searchable PDF I did the following
1. _Print_ the screenshot as a PDF
2. OCR the PDF (I used Adobe Reader X's Recognize Text feature)
3. Fix the OCR's mistakes (I used Reader X's 'Find First Suspect' feature)
4. Add hyperlinks on top of the relevant sections of the PDF (again, using Reader's Add Link feature)

### Alternatively, you can just view the finished project in PDF format
- Open `Nathaniel_Watkins_Resume.pdf`
- Observe all of my abilites
- Consider how I would be a unique asset to your team.
- Contact me via email: [theNathanielWatkins@gmail.com](mailto:theNathanielWatkins@gmail.com), phone: 657.464.4005, or LinkedIn: [in/theNathanielWatkins](https://www.linkedin.com/in/thenathanielwatkins/)

## Contributing
> I'm open to any and all feedback!  Please contact me at the links above or create a pull request.
