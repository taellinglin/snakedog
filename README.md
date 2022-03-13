# For our new developers in snake dawg

Here is how to set up venv and install dependencies:

	$ python -m venv .venv
	$ source .venv/bin/activate

It should say (venv) in front of cmd line.

	$ pip install -r requirements.txt

## Before working on the code, make sure to pull

    $ git pull

## If it errors, do this

    $ git reset origin/HEAD --hard

## If the above command errors, please dm in group chat

## To commit all of your changes, do

    $ git commit --all -m "Your commit message"

## To go back a commit, do

    $ git reset 'HEAD@{1}'

# Before pushing, make sure to lint

    $ python -m black .

## To push your code, do

    $ git push

## If it errors, just leave it like that and wait until Tael or nope is online (fixing this can be quite messy)
