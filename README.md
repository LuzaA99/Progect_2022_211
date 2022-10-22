### Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Contact](#contact)
* [Description of work](#description) 
### General info
This bot helps people find a movie or TV series for the evening to have a good time. 
### Technologies
* pyTelegramBotAPI==4.7.0
* telebot
### Contact
*  Akopova Elizaveta - @lizaakopova
*  Idaliya Gafarova - @idgafarova19
*  Mukimova Yasya - @mm_yas
### Description of work
1. We turn to the telebot library to enter the token of our bot with which we will interact
2. The first method tracks the "start" command. Next, we create a function that takes the "start" command as a parameter and creates another "markup" parameter, which creates a ReplyKeyboardMarkup type button. For convenience, we initialized two buttons via the variables "btn1" and "btn2". At the end, we again contact the bot via the send_message method, in which we specify which chat we are sending the message to, and then output a greeting and question line. We also give the user the opportunity to choose one of the two suggested options
3. We are creating a function that opens a file in the form of a list divided into lines and outputs a random value from this file that is in a range equal to the length of the file
4. the latter method takes as parameters the text values of the infotech conditions that if it is a text value it is a movie, then we create a variable that calls the previous function that accesses a file with movies in the CER format. The following three lines illustrate the principles of message output. At the end, we turn to the bot, which calls the method of sending a message in which we specify which chat we are sending the message to, and outputs a random movie to the user

### Tests
We have 6 tests, 3 each for TV series and movies. Two out of three give a positive value, 1 out of 3 is negative. The principle of operation of the tests is as follows:
* In the decorator, we run a function that checks whether the correct string is issued at the specified index of this string