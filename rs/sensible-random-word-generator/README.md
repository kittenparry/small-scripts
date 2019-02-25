## Somewhat Sensible Random Word Generator

Generates random words based on given length and given repetition value as arguments.

`cargo run` prints out a random word with the length of 10. Ex. output:  
`Xopznepaov`

`cargo run 25` prints a word with the length of 25. If no argument is provided default length of 10 will be used. Ex. output:  
`Mojbfuhgakditeodbeqwdojum`

`cargo run 20 5` prints out 5 words with the lengths of 20. If no second argument is given the default value 1 will be used for repetition. Ex. output:  
```
Yucadiwiukyurgoowocz
Muxzbezoihvonuiacadn
Ziwipipytdhatkiagesa
Jufvvemahihaskvoyozv
Reyisofeoxsosieokuki
```
"Sensible" because appends a vowel for the 2nd character and every 2nd or 3rd after that while the rest of the word is composed of consonants to give an illusion of a structure with syllables. Also "somewhat" because the words look real ugly so maybe not so sensible.

#### Dependencies
* `rand` is used to get the random characters from arrays and also decide whether a vowel should be placed at the 2nd or 3rd next* place.
* `Inflector` is used to capitalise the first letter of the word. Could be dropped if a fully capitalised array of consonants provided for the first letter.
