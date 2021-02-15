# QA Assignment submitted by **Saurabh Piyush**
This repo contains the UI as well as API automation cases that were developed as part of the assignment, to qualify for the post of Senior Automation Engineer at Sennder

## Index
1. [Framework](#Framework)
2. [Run the Automation Suite](#Run-the-Automation-Suite)
    1. [Method A Windows](#Method-A-Windows)
    2. [Method B Mac](#Method-B-Mac)
3. [API Automation](#---API-Automation)
4. [Framework Architecture](#Framework-Architecture)
5. [Why this framework?](#Why-this-framework?)
6. [Contact](#Contact)

## **Framework**
For this assignment, I have used pytest framework - a python-based test automation framework suite. It is a Test Driven Development (TDD) framework comprising of the following packages:
- **pytest** (for executing test plans in TDD format)
- **requests module** (to automate API)
- **selenium-webdriver** (to automate UI and saving failed scenarios screenshots)
- **pytest--html** (for reporting)
- **logging module** (for loggging - tracking events that occur while software runs)

### **Run the Automation Suite**
First you need to clone the repo to your local

- Clone with HTTPS:     
    `git clone https://github.com/saurabhpiyush1187/qaassigment.git`

Then you need to follow either of the below two methods
#### **Method A**: Windows
**Requirements** 
--python 3.7 and above

Open the command line and point it to the directory of the repo on your system. Switch to the virtual environment by executing "set_up.bat"
    
    C:\~\qaassigment> set_up.bat
That's it.
It will switch to virtual environment and install necessary modules. After executing above batch file, the user will enter the virtual environment. Execute another file to run all the api and ui cases

    (venv)C:\~\qaassigment> run.bat
This will start the execution of all the test cases

**View HTML Report**
The automation framework is created with the support of **pytest--html**.To view results after execution. Open

>reports/report.html
    

#### **Method B**: Mac

Requirements
–python 3.7 and above

Since virtual environments cannot be shared accross Operating systems, I have freezed the requirements to 

>./requirements.txt

Please follow the steps below:

1. **Open the command line and point it to the directory of the repo on your system**
    
2. **Execute the following commands**
 
    python -m venv env
    source env/bin/activate
    pip install -r requirements.txt

    This will install all the dependent libraries

3. **Run the script**

    Now, simply run the command
    
    python -m pytest -s -v -m "smoke" --html=./Reports/report.html --browser chrome

4. **Troubleshooting in Mac**
    
    If you have any issue with chromedriver, you can copy **./Browsers/chromedriver** to **/usr/local/bin**
    and edit the following code in **./testCases/conftest.py**

    Change this:
    
            elif platform =="darwin":
            driver=webdriver.Chrome(executable_path="."+os.sep +"Browsers"+os.sep +"chromedriver")   
            
    To this:
    
            elif platform =="darwin":
            driver=webdriver.Chrome()
    

## **API Automation**
I have also automate the cases through cases through api

If you want to run only API cases, simply run the command(Mac) or edit the same in **run.bat**(Windows):
    
    python -m pytest -s -v -m "api" --html=./Reports/report.html

If you want to run only UI cases, run the command:

    python -m pytest -s -v -m "ui" --html=./Reports/report.html --browser chrome



## **Contact**
Let me know if you would like to know more about the architecture or have any feedback. I would like to talk more about the framework suite and architecture in detail.

With best regards,

Saurabh

