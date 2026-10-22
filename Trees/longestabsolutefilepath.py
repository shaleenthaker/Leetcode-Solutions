"""Suppose we have a file system that stores both files and directories. An example of one system is represented in the following picture:
Here, we have dir as the only directory in the root. 
dir contains two subdirectories, subdir1 and subdir2. subdir1 contains a file file1.ext and subdirectory subsubdir1. subdir2 contains a subdirectory subsubdir2, which contains a file file2.ext.
In text form, it looks like this (with ⟶ representing the tab character):
dir
⟶ subdir1
⟶ ⟶ file1.ext
⟶ ⟶ subsubdir1
⟶ subdir2
⟶ ⟶ subsubdir2
⟶ ⟶ ⟶ file2.ext
If we were to write this representation in code, it will look like this: "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext". Note that the '\n' and '\t' are the new-line and tab characters.
Every file and directory has a unique absolute path in the file system, which is the order of directories that must be opened to reach the file/directory itself, all concatenated by '/'s. 
Using the above example, the absolute path to file2.ext is "dir/subdir2/subsubdir2/file2.ext". 
Each directory name consists of letters, digits, and/or spaces. Each file name is of the form name.extension, where name and extension consist of letters, digits, and/or spaces.
Given a string input representing the file system in the explained format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
Note that the testcases are generated such that the file system is valid and no file or directory name has length 0.
"""

class Solution:
    def lengthLongestPath(self, input: str) -> int:
        longest = 0
        l = len(input)
        i = 0
        isFile = False
        lengths = []
        depth = 0
        length = 0
        while i < l:
            if input[i] == '\n':
                i += 1
            elif input[i] == '\t':
                while i < l and input[i] == '\t':
                        i += 1
                        depth += 1
            else:
                while i < l and input[i] != '\n' and input[i] != '\t':
                    if input[i] == '.':
                        isFile = True
                    length += 1
                    i += 1
                if isFile:
                    if depth == 0:
                        longest = max(longest, length)
                    else:
                        longest = max((lengths[depth-1] + 1 + length), longest)
                    isFile = False 
                else:
                    if depth == 0:
                        if lengths:
                            lengths[0] = length
                        else:
                            lengths.append(length)
                    elif depth >= len(lengths):
                        lengths.append(lengths[-1] + 1 + length)
                    else:
                        lengths[depth] = lengths[depth-1] + 1 + length
                depth = 0
                length = 0
        return longest