# CID

## Description
MogamBro's brother was murdered by a relative of his. MogamBro approached the CID (Crime Investigation Department), who carried out a thorough investigation. But they were not able to figure out who the murderer was. We snuck into CID's computers and got this confidential investigation report. Your job is to figure out the identity of the murderer.

The flag format is BITSCTF{FirstNameOfTheMurderer}

## Solution
We are provided with a GEDCOM file which we can open using any genealogy software like MyHeritage Family Tree Builder. <br>
We observe that all the people have notes some of which contain certain clues. When we inspect MogamBro's notes, it tells us to ask the Russians.
So now we check the notes of all the people who are born in Russia. These notes will give us more clues on whom should we investigate.

#### How do we find the people using the clues?
If the notes give us information about the name, date or place of birth or death, etc. we can use the search feature of the genealogy software itself.

But if clue is of the format <#> number of <wifes/children/daughters> we may need to write a python script to look for such people in the GEDCOM file.
The file [finder.py](finder.py) has these scripts which make use of the gedcompy library.

Following the clues we find a clue telling that the murderer is a great-grand child of George II Hanover. <br>
While investigating, along with clues that give us leads of investigating other people, we also come across clues that 
eliminate the possibility of certain people being the murder. Using these elimination conditions, we can eliminate 28 out of 
29 great-grand children of George II Hanover. This only leaves Henriette. Hence, we conclude that Henriette is the killer.

The complete map of the clues is given in [blueprint.md](blueprint.md)

## Flag
Since, Henriette is the killer, the flag is:
```BITSCTF{Henriette}```

## Author
[Pamdi](https://github.com/pamdi8888)
