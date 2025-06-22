# YANI 
Your AI Navigator and Informant

## :rocket: Introduction
Yani is a simple chatbot that response to a user input. Currently, Yani is operating on command line by the use
of python. With further development, Yani will become a chatbot that can understand sentiments and context based
on user input.

## :sparkling_heart: Contributors
* Michael Alexis Ponce 
* Nicky Shane Villaruel 

## :pencil: Pre-requisites
* Python - `3.10.12`
* Windows Operating System - `10`
* Linux - `Ubuntu` (optional)

## :rocket: Usage 
Run the script `main.py` in the command line and you are good to go!

## :speech_balloon: For Developers
To add new set of trigger words and response of `YANI` kindly add it to the `.json` file. choose between `normal.json` and `genz.json`.
Kindly follow this format in adding a new set of trigger words and response.
```json
"<category name>": {
  "words": ["<insert trigger words here!>"],
  "response": ["<insert response here!>"]
}
```
Example in `genz.json`
```json
{
  "greetings": {
    "words": [
      "hi",
      "hello",
      "hey",
      "howdy",
      "what's up",
      "yo",
      "good morning",
      "good afternoon",
      "good evening"
    ],
    "response": [
      "Yo yo yo, what’s poppin’?",
      "Hey bestie, you made it!",
      "Ayooo, the vibes just got better",
      "What’s up, legend? Let’s get into it",
      "Hiiiii, missed you fr fr",
      "Okayyy, you pulled up, let’s slay this convo",
      "Hey hey! Big energy entering the chat",
      "Yo, you just passed the vibe check",
      "Hello hello, let’s make it a whole moment",
      "Wassup fam! You good?"
    ]
  },
}
```
Be creative on what do you want to trigger a response!
