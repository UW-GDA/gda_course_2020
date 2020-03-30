# Shell and Github: Exercises
UW Geospatial Data Analysis  
CEE498/CEWA599  
David Shean  

## Introduction

Let’s play around with some text files to explore the power of the command line and bash shell.  For the following instructions/questions, please document the command you ran, and the resulting output on the terminal. You can copy and paste these in a text file, or use whatever method is most efficient. If you would prefer to wrap everything into a single shell script, and submit that, go for it.

You will almost certainly need to search for tips on how to answer some of these questions. Please use these resources, but if you find an explicit solution, don't just copy and paste the code, review it and try to understand what is actually happening. Note that Stack Overflow and other forums will have excellent information (and probably a lot of advanced information that is over your head) - typically the answer you're looking for has the most "upvotes" (number to the left of the answer) or some kind of indication as the "accepted answer." 

OK, let's get started!

## Look it up in the dictionary

On your Unix/Linux filesystem, you typically have a dictionary of words (https://en.wikipedia.org/wiki/Words_(Unix)).  On OS X, this file is located in `/usr/share/dict/words`

This file is missing from our barebones JupyterHub Linux distribution, so I added one to the assignment git repo (2.4 MB).

### Inspect `words`
1. The `words` file has no extension. What type of file is this? (Hint: try `man file` to bring up man page on the `file` command)
2. Inspect the file `more words` (hit q to quit).  Should see one word per line.
3. How many words are in this file?
4. How many characters?
5. How big is the file size in bytes? 
6. How many bytes are required to store each character? Hopefully this provides some new insight into file size on your computer.
6. Print the first 3 words. Print the last 3 words (do this with a command, don’t just view or open in text editor and copy/paste)
7. Does `words` include the nickname for the UW mascot (if unfamiliar, ask your neighbor)? If so, what line number?

### Extra credit
8. How many characters are in the longest word?  Hint: should be simple one-liner, you don’t need `awk` for this.
9. How many words end in “ology”?
10. How many end in “ologist”?
11. How many have the same prefix?
    * Hint: replace "ologist" with "ology", then count number of duplicate lines.

## Inspect and manipulate tabular data

The text file `GLAH14_tllz_conus_lulcfilt_demfilt.csv` contains processed/filtered records from ICESat satellite laser altimetry measurements over the Western U.S. between 2003 and 2009. Don't worry about details for now, we will explore in the coming weeks. For now, pretend your advisor/boss just sent you this random file (with no metadata) and asked you to inspect and clean up for their old-school analysis tools.

1. Inspect the file on the command line. Use tab-completion after typing the first few letters of the filename. 
2. The extension suggests that this is comma-separated value (`.csv`) text file - verify this.
3. Fortunately, there is a header on the first line containing strings for each field (column) name. Some of these should sound familiar. How many fields are there? How many rows contain data (excluding the header)?
4. How many records are from 2005?
    * Utilities like `grep` and `sed` offer powerful functionality with "regular expressions" - one could spend weeks learning these. For now, I'll give you a hint, if you preceed your `grep` search string with a carat `^` (e.g., `^stringtofind`, it will only return records that begin with `stringtofind`, excluding any records with `stringtofind` elsewhere in the string.
    * You'll want to use a pipe `|` here to pass the output of `grep` to another command that can count the number of lines.
5. Create a new file with only the `lat` and `lon` fields, separated by a space, and sorted in ascending order by `lat` value.
    * This should be possible without any loops, just need to redirect the stream using pipes `|` and `>`. Let's break the problem down.
    * First, isolate the `lat` and `lon` fields - several ways to do this
    * Pipe that output to a command that will replace the `,` with a ` ` on all lines
    * Pipe that output to a command that will sort the numeric `lat` values
    * Redirect that output to a new file
    * Run a quick `head` and `tail` on the output file to verify

# Extra Credit: Shell script
Create and run a script to answer the following question:

*How many words begin with each letter of the alphabet (case-insensitive)?*

### Useful references for review
* [http://swcarpentry.github.io/shell-novice/06-script/index.html](http://swcarpentry.github.io/shell-novice/06-script/index.html)

### Requirements:
* Ignore case, so "A" and "a" are considered the same word
* Your script should accept the `words` text file as an input argument (assign to a variable named `fn`)
* Your script should create a new output file called `words_lettercount.txt`
    * Pro tip: You can use [variable parameter substitution](https://www.tldp.org/LDP/abs/html/parameter-substitution.html) to append strings to the input filename: `out_fn=${fn%.*}_lettercount.txt`
    * The `${fn}` construct is a less ambiguous variable reference.  Need this if you wanted to do something like print your filename and add extra characters `echo ${fn}:moretext` (try `echo $fn:moretext` for comparison)
    * The `%.*` can be used to get the first part of the filename string before any `.` extension ([see SO answer](https://stackoverflow.com/a/965072))
* The output file should include a letter and total count on each line (“a 17096”)

### Instructions:
1. Create a new shell script in your preferred text editor (nano, vim, emacs or Jupyterlab text editor): `nano myawesomescript.sh`
2. Write some code.
3. Save the script.
4. Make it executable: `chmod +x myawesomescript.sh`
5. Run it! `./myawesomescript.sh words`
6. Review the output `more words_lettercount.txt`

# Submission
*We will review this process during our first lab*
1. Use `git add` to stage each new file containing your answers/scripts
    * I recommend you start by adding files one at a time: `git add myawesomescript.sh`
    * For now, resist the temptation to `git add .` or `git commit -a`, as you will inevitably include files that don't belong in a git repo.
2. Use `git commit -m "I did it!"` to commit these changes, replacing "I did it" with an appropriate commit message.
3. Use `git push` to push your local changes to your remote repo origin on Github