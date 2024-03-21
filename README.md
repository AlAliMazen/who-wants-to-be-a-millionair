

# Who Wants to be a Millionaire ?
🚨**Required** 
"Who Want to be a Millionaire?" is a British television show first created by David Briggs, Steven Knight and Mike Whitehill for the ITV network in 1998. This application is just a clone of that concept. In simple words, a game in which the participant should answer 15 questions to get to the one million prize. 

The game is divided into 3 sections of questions 5 questions for each level(Easy, Medium and Hard). The game will be terminated whenever a player chooses a wrong option for the shown question. 

When the game starts there are 4 option to choose from. 1. Player can start the game. 2 Player can show the rules under How to play section. 3 Showing the scoring board sorted from the highest to the lowest. 4 Quitting the game. 

If a player chooses to start the game, s/he needs to type his full name and his country. Theses information will be saved in the scoring board.

## Flowchart of the Game:

In Software industry, it is extremely important to have a complete understanding of when the process starts and when it ends as well as what happens in between. Following flowchart shows how the play begins and when it ends.

![Flowchart](assets/README/who_wants_to_be_a_millionaire.png)

Following is a video about the end product:
https://github.com/AlAliMazen/who-wants-to-be-a-millionair/assets/153659892/0f9f22d2-5fa3-4aae-aa14-b2be744827a1




## Live Site
🚨**Required** 

- [Who Wants to Be a Millionaire?](https://whowantstobeamillionaire24-bb20122b77fb.herokuapp.com/)

## Repository
🚨**Required** 

- A complete repository for the game is under [Who Wants to Be a Millionaire?](https://github.com/AlAliMazen/who-wants-to-be-a-millionair)

## Author
🚨**Required** 

Mazen Al Ali

## Table of Contents
🚀 **merit & beyond**

### Screenshots and Videos


# Table of Contents
🚀 **merit & beyond**

- [PROJECT NAME](#project-name)
  - [Live Site](#live-site)
  - [Repository](#repository)
  - [Author](#author)
  - [Table of Contents](#table-of-contents)
  - [How To Play/Use](#how-to-playuse)
  - [Features](#features)
    - [Implemented Features](#implemented-features)
    - [Future Features](#future-features)
  - [Flow Chart](#flow-chart)
  - [Data Model/ Classes](#data-model-classes)
    - [Class X](#class-x)
  - [Libraries used](#libraries-used)
  - [Testing](#testing)
    - [Validation Testing](#validation-testing)
    - [Manual Testing](#manual-testing)
    - [Defect Tracking](#defect-tracking)
    - [Defects of Note](#defects-of-note)
    - [Outstanding Defects](#outstanding-defects)
    - [Commenting Code](#commenting-code)
  - [Deployment](#deployment)
    - [Requirements](#requirements)
    - [Gitpod](#gitpod)
    - [Heroku](#heroku)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Acknowledgments](#acknowledgments)
    


====================================== The Sections you Fill in are below ==============================


## How To Play/Use
🚨**Required** 

When the Game starts it does execute the following steps before the player is able to type an choice. First of all it reads the questions text files and split them into lists preparing them for inserting in the Google drive sheets. Only if the google sheets allocated for the questions are empty, the population process will be executed. Each question sheet has 20 question. There are 3 types of questions (Easy, Medium and Hard)

How to play when game starts?

    1- Choose one of the options 1,2,3 or 4 
    2- To start the game choose 1 . This option will be forwarded to ask the player to type his name and his country and press enter key after each input.
    3- Console will be cleared and a line at the top of the console will be shown with player name, country, score and question level
    4- A question will be shown with 4 options 1 to 4 . Player can type his option by pressing keys of 1 to 4 .
    5- In case the option is the same as the right answer, the score will be incremented, console will be cleared and a new question will be shown.
    6- In case the option isn't right, the game will be terminated indicating the player loses the round and his current score. 
    7- If player chooses the second option, the rules and How-to instructions are going to be shown. Player can also either end the game by pressing e or going back to the menu by pressing y
    8- When the third option is clicked the scoring board will be loaded from the google sheet and it is sorted based on the score 
    9- If player chooses to quit the game, s/he should only choose number 4 and game will be terminated.

## Features
🚨**Required** 


### Implemented Features
🚨**Required** 

From a developer point of view this version of the game implements the concept of the OOP and makes use of the class concept. Player as well as Question both have their separated files and initialized in another procedural python file.

Another Feature is the validation process of user input, either whe Player still at the main menu of the game or when the question is displayed. The validation process makes use of the Regular Expressions.

Safety Score Calculation: when player loses the round a call to the player object and let it check the last score the player has got. If it is more than 1000 then 1000 will be his last score instead of 0. In the same manner when player loses the round and his is at questions more than 10, player will get back to 32000 instead of 0 or 1000 .

Last but not least, the game makes use of the live score tracking. In other words, whenever the player gets the right answer for the shown question, h/his score is going to be incremented (make use of the player object implemented methods) and shown right at the top of the game. 


### Future Features
🚀 **merit & beyond**

The possibility for the player to remove two wrong options will be a good future feature to implement later on. This feature will be available be the medium and hard questions and only to be used once in the whole round.


## Flow Chart
🚀 **merit & beyond**

The following flow chart shows how the game starts and what happen by choosing options 

![game Flow Chart](assets/README/who_wants_to_be_a_millionaire.png)

## Data Model/ Classes
🚨**Required** 

In this section write our your data model(s) or classes. 

You might want to include subsections that include how the data in the model is initialized and then the methods that you created to update it through the program.


You can create a table and take a screenshot, or you can write up subsections in markdown:

![image](https://user-images.githubusercontent.com/23039742/130148204-b56406bf-0fff-48f3-9dee-2f3cdbe67cc5.png)

### Class X
To better group the game as an object, I wrote a class representing its properties and had method functions to update those properties: 

**Properties**
- property 1: is a {string} it represents {something} 
- property 2: is a {string} it represents {something} 

**Methods**
- **\_\_init\_\_**: Initialize method, it starts the class off with default parameters as if a user just started to play a game.
- **\_\_str\_\_**: Returns a string representation of the class/object

## Libraries used
🚀 **merit & beyond**

List out the python libraries you purposefully used in your project and why. You can look at your requirements.txt file and go back to https://pypi.org/ to rediscover the purpose of a library if needed.

A bulleted list is a good presentation for this information.

## Testing
🚨**Required** 

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your features and ensure that they all work as intended in an easy and straightforward way for the users to achieve their goals.


### Validation Testing
🚨**Required** 

You should try to ensure you code is valid and follows proper indentation.  In this section you should write up any websites you used to validate your code. As your projects becomes more complex these tools may change.

For each python file in your project, paste it into [CI's pep8 tool](https://pep8ci.herokuapp.com/), and take a screenshot of the linter output showing NO ERRORS

![image](https://user-images.githubusercontent.com/23039742/212106175-36b2f18a-7c75-458d-94dd-9886e81c71f3.png)

Ideally you would have no errors remaining outside of line too long which you can fix by 

adding
```$python 
# noqa
```
There is a space before the # and after it to skip the quality assurance for that line.

Note any errors or warnings you are ignoring and why.

### Manual Testing
🚨**Required** 

Use Markdown to track how you tested each bit of user input for each valid option, various invalid entries and leading/trailing spaces

**Feature 1**
- [ ] invalid entry, says sorry and re-prompts
- [ ] no entry, says sorry and re-prompts
- [ ] alpha when numeric expected, sorry and re-prompts
- [ ] valid entry with leading spaces, trimmed and shows proper next stage
- [ ] valid entry with trailing spaces, trimmed and shows proper next stage

You should also call out how you tested any other features such as:
- Welcome Message, recaps username
- Score update shows current score
- color change for correct vs incorrect
- google sheet updated properly

If you prefer spreadsheets, create a google-sheet and link to it in this section, just make sure you update the permissions to allow anyone to view it. You can make a [COPY of this example](https://docs.google.com/spreadsheets/d/1w_JUmFfzHVtXdHse6ib82BGnRMPlPqufSOnAVN3bVl8/edit?usp=sharing) and update it as your own. Just make sure you share it to anyone with the link:
https://docs.google.com/spreadsheets/d/1w_JUmFfzHVtXdHse6ib82BGnRMPlPqufSOnAVN3bVl8/edit?usp=sharing

### Defect Tracking
🚨**Required** 

Try to create issues in real time as it better reflects the daily life of a developer.

The easiest way to track defects is by using GITHUB's Issues to track these as it's really easy to copy/paste screenshots in and then write up how you closed them. At this stage you don't need a custom template or labels, that comes in P4.

 Here's a [guide to GitHub Defects](Defects.md)

### Defects of Note
🚀 **merit & beyond**

Some defects are more pesky than others. Highlight 3-5 of the bugs that drove you the most nuts and link to them directly here.


### Outstanding Defects
🚨**Required** 

It's ok to not resolve all the defects you found as long as:
- it does not impact a user from completing a vital function on the website
- it only affects a very small subset of users
- is an extreme edge case that very few users would try
- there is an open issue against a framework, browser or technology used

If you know of something that isn't quite right, create an issue and link to it here and explain why you chose not to resolve it. 

Sometimes it's as simple, word wrapping issue that makes the site look odd at a certain screensize that you just didn't have time to fix due to the impending deadline it's best to mention it but note why you allowed it to go live: "Yes it looks odd, but it doesn't impact core functionality of the site." than to let the accessors think you didn't notice it. 

### Commenting Code
🚀 **merit & beyond**

Make sure you use triple double quotes to document functions and classes.
 Here'a  documentation worthy example:
```$python
def yes_no(question):
    """
    Function to ask a simple yes no question of the user.
    :param question: String displayed as the question
    :return: answer: String equal to "1" or "2" representing yes or no respectfully
    """
    print(question)
    print("yes = 1")
    print("no = 2")
    answer = input("enter your answer here \n").strip()
    while answer not in ("1", "2"):
        print("please choose 1 for yes and 2 for no")
        answer = input("enter your answer here \n").strip()
    return answer

```

## Deployment
🚨**Required** 

### Prerequisites
🚨**Required** 

If the user is required to have certain keys and credentials you should include this section with directions on how to get the necessary information.
ex)
1. **Google Account:** In order to have this program work, you need a google account. If you don't have one  [Create a google account](https://accounts.google.com/Signup)
2. **Google APIs**
    1. in a new incognito tab, log into your new google account.
    1. then update the url to be: https://console.cloud.google.com/getting-started?pli=1 
        
        **GOOGLE DRIVE API Access**
        1.  create a new project for this, call it XXXXXX (You might want to refer to what you see in this video: https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/071036790a5642f9a6f004f9888b6a45/ at the bottom of the screen to write out steps.)
        2. Then click on Add APIs and Services and select Libraries
        3. Search for Google Drive
        4. Click Enable
        5. Click Create Credentials
        6. Select Google Drive API from the drop down, Application Data, then no and click the Next Button
        7.  (https://developers.google.com/drive/api/v3/enable-drive-api) 
        8. for service account details fill in a service account name ex) xxx_API, then click Create and Continue
        9. For the Accoun acces, select Role: Basic/Editor then continue
        10. Then Click Done
        11. Now select the newly created service account
        12. Click on the KEYS Tab
        13. Click Add Key
        14. Select JSON type (right click to show in folder so you know where the file was saved.
        
        **GOOGLE SHEETS API Access**
        You may need to us the back button get to the APIS & SErvices section from where you were.
        1. click the Libray  Tab and serarch for Google Sheets
        2. click enable

3. The downloaded credentialsJSON file is basically your creds.json file that you need to put into your heroku settings or gitpod environment to access your google drive.

4. Google Sheet Template
  - If you had to create specific sheets for your project, instruct users to make their own copy of it from yours and rename it back to what the python project expects
  - And don't forget to share the spreadsheet in question with the client_email from the creds.json 

### Gitpod
🚀 **merit & beyond**

This section should describe the process someone would have to go through to get the local working in gitpod.  Such as install requirements.txt  and setting up a creds.json file that is in the gitignore and keeping their workspace.

If you have project settings required such as a creds.json file from the GOOGLE DRIVE API acess, please provide an example of that file in the writeup with the project key values:
```$python
{
    "type": "service_account",
    "project_id": "<YOUR_VALUE>",
    "private_key_id": "<YOUR_VALUE>",
    "private_key": "<YOUR_VALUE>",
    "client_email": "<YOUR_VALUE>",
    "client_id": "<YOUR_VALUE>",
    "auth_uri": "https://accoutns.google.com/0/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cer_url": "https://www.googleapis.com/oauth2/v1/certs",
    "clien_x509_cert_url": "<YOUR_VALUE>"
}
```

If you have any dependencies, you should instruct users to install them
```$python
pip3 install -r requirements.txt
```

### Heroku
🚨**Required** 

This section should describe the process you went through to deploy the project to Heroku. Include screenshots if you think they would make the process easier.

You may want to re-watch the [python essentials deployment video](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/e3b664e16366444c8d722c5d8340b340/?child=first) when writing up this section.


If you have project settings required for Heroku, provide a table of the keys and values.
Do not share your personal keys but either cut them out of the screen shot or say <YOUR_VALUE> and include links on how the user would obtain such values.

1. Fork the repository

Make a fork so you have a copy of the repository in your own git hub account: https://github.com/maliahavlicek/portfolio_project_03

![image](https://user-images.githubusercontent.com/23039742/132136504-eb79a6f3-0205-4c82-80c2-eef136ec7e4c.png)


2.  New Project
Log into Heroku and create a new project. Name it something like XXX_coders_bistro.


3.  Settings
On the settings tab you have to address two things:
A. **Config Vars**

  ![image](https://user-images.githubusercontent.com/23039742/132135869-215d2e0f-805d-40a8-a8c2-fb1098e2645d.png)

  At a bar minimum you should show the user that they need to add the PORT. 8000 key value pair.


B. **Build Packs**

  ![image](https://user-images.githubusercontent.com/23039742/132135918-28cac112-7766-4277-905c-4a4963d8442d.png)

  add Python Then Node.js


4. Deploy
A. Set up to github and select the correct repository:

  ![image](https://user-images.githubusercontent.com/23039742/132136113-c257c921-d10c-4ccc-af09-6a1d25136395.png)

B. Deploy either manual or automatic

![image](https://user-images.githubusercontent.com/23039742/132136241-9d76fabb-39f0-4696-bc5f-047398fdaf41.png) 



## Credits
🚨**Required** 

To avoid plagiarism amd copyright infringement, you should mention any other projects, stackoverflow, videos, blogs, etc that you used to gather imagery or ideas for your code even if you used it as a starting point and modified things. Giving credit to other people's efforts and ideas that saved you time acknowledges the hard work others did. 

-[Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

### Content
🚨**Required** 

Use bullet points to list out sites you copied text from and cross-reference where those show up on your site

### Media
🚨**Required** 

Make a list of sites you used images from. If you used several sites try to match up each image to the correct site. This includes attribution for icons if they came from font awesome or other sites, give them credit.

### Acknowledgments
🚨**Required** 

This is the section where you refer to code examples, mentors, blogs, stack overflow answers and videos that helped you accomplish your end project. Even if it's an idea that you updated you should note the site and why it was important to your completed project.

If you used a CodeInstitute Instructional project as a starting point. Make note of that here too.

