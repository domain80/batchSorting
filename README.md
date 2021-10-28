# Batch Sorting
Using python to generate a bat script of repetitive lines of code that differ in some way but can sort out a group of audio files according to their common names

## The problem was...
I had a bunch of files which after decompressing were not sorted in thier folders as i expected them to be  
I also could not create a folder for each group of audio files and move each group of files into thier respective  
folders...

## The approach...
1. I knew how to move one file using the command line
2. But I did not know how to fully use batch scripting to move all files at once. 
3. I also knew how to use python to generate any file I want as it  
is just a matter of using the right filename extension.
4. So, I worte a python script that generated a batch script that contained the  
commands needed to move all the files into their respective folder groups.

## What the script does...
1. the script generates a list of all the names of audio files I needed to sort
2. Then, for each filename the script attaches the batch command needed to:  
- first create a folder with the current filename and
- move all files with that name into the folder.

## Caveat:
The script generated is not generic and can not be used for other audio files


### [The python Script can be found here](https://github.com/David-Main/batchSorting/blob/main/BibleSort.py)

### Here's a quick demo of how it worked

https://user-images.githubusercontent.com/89542969/139326408-aa1d2e40-bfb9-47a8-9009-030e00cb81b0.mp4

