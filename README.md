# pywords
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

`pywords` is a lightweight program which computes all possible permutations of an input string which are also valid English words.  

 To run, simply clone the repo and make `words.py` exec:
 ```{bash}
 git clone www.github.com/ifrit98/pywords.git
 cd pywords && chmod +x pywords.py
```

Usage:
```{bash}
./pywords.py
>> Enter letters:
>>   dad
>> array(['dad', 'add', 'add', 'dad'], dtype='<U3')
>> Enter letters:
>> q
>> Exiting...

```
  
  - Only valid alphanumeric string literals are accepted as input
  - Enter the chr `'q'` as input to exit the program 
  - The dictionary file `words.txt` can be modified or replaced as needed
  - This repo uses `itertools.permutations()` to compute the results of each substring
 
 
License
----
MIT
**Free Software, Hell Yeah!**