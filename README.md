# LAB - Class 42
## Project: Pythonisms
### Author: Brendon Hampton
### Links and Resources
- [back-end server url](#) (when applicable)
- [front-end application](#) (when applicable)
### Setup
`.env` requirements (where applicable)

**i.e.**

- `PORT` - Port Number
- `DATABASE_URL` - URL to the running Postgres instance/db
#### How to initialize/run your application (where applicable)
- e.g. `python main.py`

## Findings
- this is a modification to stack class, this adds a method that will reverse a string, after doing the code challenge the other day, I thought a built in method to reverse a string using a stack would make python life simpler. this method takes in a string, pushes each item in the string onto a stack and then pops it into a new string and returns the new reversed string.


## UPDATE
- I modified my Class, I completely removed it and changed it to an inventory system that stores items. T=I used a method decorator that can apply a tax based on if you pass in a boolean to apply the tax or not. I also initialized the item objects and the inventory shelf, so instead of creating a method that prints out the shelp, you simply print the inventory class and it will show all the items in the shelf so you do not need to have any special method to see the inventory (utilized dunder methods for both item object and inventory storage object)

#### How to use your library (where applicable)
#### Tests
- How do you run tests?
- Any tests of note?
- Describe any tests that you did not complete, skipped, etc
