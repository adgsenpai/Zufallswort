## Generate random german words / Generiere zufällige deutsche Wörter

##### Pip install ready german word generator with a 300.000 word dictionary. 

<br> 


<p align="center">
    <a href="https://github.com/MaximilianFreitag/Zufallswort">
        <img src="https://github.com/MaximilianFreitag/Zufallswort/blob/main/image_gen.jpg">
    </a>
</p>


<!-- GETTING STARTED -->
## Getting Started


1. Pip install with
   ```sh
   pip install zufallsworte
   ```

2. Import the library with
   ```sh
   import zufallsworte as zufall
   ```

<br> 
______________________________________________________________________________________________
<br>  
 
   
<!-- How to use -->
## How to use
   
<br>
Return one random word

    zufall.zufallswoerter(1)
    
    --> Katze

<br> 

Return 5 random words 
 
    zufall.zufallswoerter(5)
    
    --> ['rot', 'Baum', 'Eichhörnchen', 'Brötchen', 'Auto']

<br> 

Return 3 random words that start with certain letters 

    zufall.anfangsbuchstaben('herum', 3)
    
    ['herumtragen', 'herumnörgeln', 'Herumtreiber']

<br> 

Return 3 random words that end with certain letters 

    zufall.endbuchstaben('legen', 2)
    
    --> ['anlegen', 'hinzulegen']


<br> 

Return 2 random words that contain the letters "ff"


    zufall.enthaelt_buchstaben('ff', 2)
    
    --> ['Schiff', 'Affinität']

<br> 

Return 3 random words that are exactly 7 characters long


    zufall.anzahl_buchstaben(7, 3)
    
    --> ['Biomüll', 'fließen', 'Rotwein']


<br />
<br />
<br />

<!-- Current bugs -->
## Current bugs

When you import the library you will see three words as an output. Just ignore them.


<br />
<br />
<br />
<br />

## Stargazers over time

[![Stargazers over time](https://starchart.cc/MaximilianFreitag/Zufallswort.svg)](https://starchart.cc/MaximilianFreitag/Zufallswort)





<br />
<br />
#Generator #Pip install #deutsch #zufällig #Wörter #duden 
<br />
<br />



## License
This project falls under the MIT license.




