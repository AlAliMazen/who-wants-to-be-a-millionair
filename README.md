

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

### Player

As the name implies the ***Player*** class is created to collect the player information like full name and country and it gives a default score of zero to the player object. The class has then the following properties:


**Properties**
- full name 1: is a {string} type like in John Smith. It can't have any special character.
- country 2: is a {string} it represents the country of the player and it also can't have any special character.
- score 3: is an integer type initialized with 0 as default type when an object of the Player class.

**Methods**
- **\_\_init\_\_**: Initialize method, it starts the class off a list which holds the values of full name and country.
- **get_player_details(self)**: It returns the details of the current player as a list (full name and country).
- **get_player_with_score(self)**: It returns the current player details with h/her score as a list.
- **increase_player_score(self, index)**: Based on the index of the question, the score is going to be increased be itself. In order to get the million after answering 15 questions, then two questions should be assigned by magic win values (Question 5 and question 12 for example).
- **update_safety_score(self)**: this method works as a safety limit when the player loses the round. If Player loses when s/he got more than 1000 $, it will return to 10000 . Likewise, when Player gets more than 32000 s/he get back to the 32000 . It returns the last valid score.

### Question

The second class used inside this version of the game is the question it self. This Class is used for each question shown. When the game starts, the play gets a complete list of 15 randomly selected questions and every question is an object of this class.

Questions are of three levels easy, medium and hard. Questions are going to be read from text files and uploaded to the google sheets. the question inside the file has a question and four options and the index of the right answer at the end.

**Properties**

- question: the question itself like in what's the smallest prime number.
- option a til d : the options of the shown question from a to b and will be shown as 1 to 4 .
- r_index: the right answer index : this index is used to check against the player's choice. 

It is worth mentioning that all the previous properties are used in the constructor to initialize the object. These properties are given as a list from the ***utilities*** Module.

**Methods**

- **check_usr_answer(self, usr_answer)**: It return True when the usr_answer parameter is the same as the r_index of the question object.
- **get_question_txt(self)**: When the question class is called, an object of this class is initialized and it makes it easier to control it. This method returns the question text itself. 
- **get_question_option(self, option)**: since the question is an object, this function will give a static index to this function and it returns the option of that question at this index. 

## Data Module

### utilities
This is the main python where the heavy load is executed. This file contains only functions and it is procedural; that is, it contains no class only objects of the previous two classes. Functions are as the following:

- **split_list(list, single_question)**: used to split the questions' list into separated single lists of questions. Thus, if the list contains 20 questions in one single list, it be returned as a list of 20 lists and each list represents one single question. 

- **read_file(file)**: used for reading the questions from text files line by line and collects the content in a list. It calls the split_list function to split the big list into single question.
- **print_game_title()**: used to print the Game title every time the game starts and a new question is printed.
- **print_game_menu()**: Called whenever the game starts or after the rules are shown. It shows the 4 options available for the player. It is worth mentioning that the two previous functions print the title, options and the question later on as formatted style; that is in the middle of the console with padding before and after the text. 
- **show_game_instructions()**: When player selects number 2, the rules and how-to play instructions are shown. 
- **get_user_choice()**: called after the instructions are shown and waits till player chooses either y for yes to go back to the main options or e for quitting the game.
- **clear_console()**: This function clears the console after player types h/his option. It makes use of the os and platform module to detect the operation system and give the corresponding command to the terminal either cls for Windows prompt and clear for macOS and Linux terminals. 

- **get_player_data()**: used when the player is asked to type his full name and country and makes use of input() function. It calls the validation function to check the player input.
- **validate_string_input(str_input, type)**: used to check if the player's full name has noc special character. It makes use of the regular expressions which accepts only small and capital letters with spaces.
- **validate_integer_input(usr_choice)**: used to check if the numeric user input whether it is from the main menu or the questions options. It checks that the input contains only options from 1 to 4 .

- **update_questions_worksheet(question_level,questions_list)**: after splitting the question list into mini lists of single questions, this function takes that lists and insert them into the google sheet. 

- **read_questions_txt_files()**: this function makes use of the os library and the function get current working directory getcwd() which ready the directory of the question files and then reads the question into variables. Then it calls the update_questions_worksheet().

- **get_random_question_index(question_list)**: this function is used to get five random questions from the given question list.

- **get_question_ready()**: it prepares a list of ordered 15 questions in a list. The first 5 questions are easy, then medium and the last 5 are hard questions. This functions makes a call to the google sheet to load all the questions in all levels in separated lists.

- **get_question(index)**: this is where a question object is created and the index is going to be from the UI interface in a loop fo 15 indexes. The list which is created in the previous function is used to be iterated and the index is the list which is used to initialized the question object.

- **print_question_with_choices(question, index)**: prints the question object with its choices as formatted text with padding and the question is printed underlined. 

- **print_player_info(player, q_index)**: When the game starts the player object is used in this function to print a line at the top of the console to show the current player name, country, score and level. the second parameter q_index is used to detect the question level. 

- **update_scoring_sheet(player, index)**: 
used to update the google sheet when the player wins or loses the round. It makes a call to update the scoring sheet with player info and h/his score with the date.

- **print_winner_info(player, index)**:gets called when the player only wins the game to print a text indicating that the game is over and player has won the prize.

- **get_scoring_board()**: When a player chooses number 3 right from the beginning to see the scoring board, this function is called to print sorted results of the player who participate in the game with their details (full name, country, score, level of question reached and date).


## Libraries used
🚀 **merit & beyond**

| Library                    | Usage                                                                                                                                                                                                                                                                                           |
|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cachetools 5.3.3           | This module provides various memoizing collections and decorators, including variants of the Python Standard Library                                                                                                                                                                            |
| certifi 2024.2.2           | Certifi provides Mozilla’s carefully curated collection of Root Certificates for validating the trustworthiness of SSL certificates while verifying the identity of TLS hosts. It has been extracted from the Requests project.                                                                 |
| charset-normalizer 3.3.2   | A library that helps you read text from an unknown charset encoding.                                                                                                                                                                                                                            |
| google-auth 2.29.0         | This library simplifies using Google’s various server-to-server authentication mechanisms to access Google APIs.                                                                                                                                                                                |
| google-auth-oauthlib 1.2.0 | This library provides oauthlib integration with google-auth.                                                                                                                                                                                                                                    |
| gspread 6.0.2              | Simple interface for working with Google Sheets.                                                                                                                                                                                                                                                |
|                            | Features:                                                                                                                                                                                                                                                                                       |
|                            |  - Open a spreadsheet by title, key or URL.                                                                                                                                                                                                                                                     |
|                            |  - Read, write, and format cell ranges.                                                                                                                                                                                                                                                         |
|                            |  - Sharing and access control.                                                                                                                                                                                                                                                                  |
|                            |  - Batching updates                                                                                                                                                                                                                                                                             |
| idna 3.6                   | Support for the Internationalized Domain Names in Applications (IDNA) protocol as specified in RFC 5891. This is the latest version of the protocol and is sometimes referred to as “IDNA 2008”.                                                                                                |
|                            | This library also provides support for Unicode Technical Standard 46, Unicode IDNA Compatibility Processing.                                                                                                                                                                                    |
| oauthlib 3.2.2             | OAuthLib is a framework which implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework. Use it to graft OAuth client support onto your favorite HTTP library, or provide support onto your favourite web framework.                            |
| pyasn 1.6.2                | pyasn is a Python extension module that enables very fast IP address to Autonomous System Number lookups. Current state and Historical lookups can be done, based on the MRT/RIB BGP archive used as input.                                                                                     |
| pyasn1-modules 0.3.0       | The pyasn1-modules package contains a collection of ASN.1 data structures expressed as Python classes based on pyasn1 data model.                                                                                                                                                               |
| requests 2.31.0            | Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings  to your URLs, or to form-encode your PUT & POST data — but nowadays, just use the json method!                                                                                   |
| requests-oauthlib 2.0.0    | OAuth 1 can seem overly complicated and it sure has its quirks. Luckily, requests_oauthlib hides most of these and let you focus at the task at hand.                                                                                                                                           |
| rsa 4.9                    | Python-RSA is a pure-Python RSA implementation. It supports encryption and decryption, signing and verifying signatures, and key generation according to PKCS#1 version 1.5. It can be used as a Python library as well as on the commandline. The code was mostly written by Sybren A. Stüvel. |
| StrEnum 0.4.15             | StrEnum is a Python enum.Enum that inherits from str to complement enum.IntEnum in the standard library. Supports python 3.7+.                                                                                                                                                                  |
| urllib3 2.2.1              | urllib3 is a powerful, user-friendly HTTP client for Python. Much of the Python ecosystem already uses urllib3 and you should too.                                                                                                                                                              |

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

