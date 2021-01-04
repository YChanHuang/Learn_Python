# RegEx
##


```

compiled_re = re.compile('pattern')
complied_re.search(text)
```
## **[]** to Match
---
- `[A-Z]` : Capital A-Z
- `[a-z]` : Lower case a-z
- `[0-9]` : Numbers




## `\` To Match

### 1. Digits 
   - **\d** : digits(numbers)
   - **\D** : non-digits
  
### 2. Space
  - **\s** : space characters
  - **\S** : non-space characters
### 3. All 
  - **\w** : `[A-Za-z0-9_]`
  - **\W** : exclude `[A-Za-z0-9_]`
### 4.
- **\b**
- **\B**

## Symbols

- **^** : To begin with
- **-** : Consecutive
- **\\** : Using escape word to select the special character
- ****

- **?** :
- **+** : Appear at least **1** times or more times 
- **.** : Match anything apart from space 
- **\*** : Select 0 to many times 
- **[]** : select all elements in the brackets
- {2,10} : 2~10 times 

## Other syntax

- **M** : sample cold `(flags = re.M)` (**M** means multiple lines)
- **Group**: Match the pre-set patterns in a group
- **|** : (pt1|pt2) match pattern1 or pattern2


### RegEx cheatsheet
#### Chinese 
![Chinese](https://i.imgur.com/9KMdEGp.jpg)

#### English 
![](https://i.imgur.com/RElLaHH.jpg)

[Source From myinfographics.blogpost](https://myinfographics.blogspot.com/2011_02_06_archive.html)

### Python functions
```
re.find()     #find once

re.findall()  #find all matchings

re.sub()      #subsitute the pattern with the other 
string   

re.split()    #split

```