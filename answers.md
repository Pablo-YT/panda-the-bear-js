1.var img = document.querySelector(".profile-image")
img.src = "https://wwwmpa.mpa-garching.mpg.de/galform/cr/GalsDist512.gif"

1.var skyPhoto = document.querySelector('#left-image.portfolio-image')
skyPhoto.src = "http://elrincondelgeek.files.wordpress.com/2011/04/google-chrome-logo-400x400.jpg"

2.var stuff = document.querySelector('h1')  
stuff.innerText = "Josh Date"
"Josh Date"


3.
var empoly = document.querySelector("div#employment.info-inner-container")
var title = document.querySelector('h3.info-title')
title.innerText = "Sweg"


4.var color = document.querySelector("body")
color.style.backgroundColor = "red"

5.
var highlight = document.querySelectorAll('.highlight')
for (let i = 0; i < highlight.length; i++) { 
    let item = highlight[i]; 
    item.style.color = 'tomato'; 
}

6.var stuff = document.querySelector("h1")
undefined
stuff.style.fontFamily = "monospace"
"monospace"

7.var icon = document.querySelector(".action-container")
var icons = document.querySelector(".action-icon-container")
icons.style.backgroundColor = 'red'

8.
var place = document.querySelector("form")
var place1 = document.querySelector("#name.contact-info")
place1.setAttribute("placeholder","Josh")



9.var place1 = document.querySelector("#form")
var place1 = document.querySelector("#message")
place1.setAttribute("placeholder","state your business")

10.
var place = document.querySelector("form")
var place1 = document.querySelector("#name.contact-info")
place1.setAttribute("value","your nemesis")


11.
var email = document.querySelector("form")
var email1 = document.querySelector(#email.contact-info)
email1.setAttribute("value", "koalathebear@gmail.com")

12.
var submit = document.querySelector("form")
var submit1 = document.querySelector(#submit)
submit1.setAttribute("value", "En garde")

13.
var disable = document.querySelector("#submit")
disable.setAttribute("type",disable)


14.
var disable = document.querySelector(".bio-info")
disable.style.display = "None"

Part 2 

1.
var remove = document.querySelector('#time-travel')
remove.style.display = "none"
# var div = document.querySelector('#time-travel'); var title = div.querySelector('.bar-title'); div.removeChild(title)

2.
var image = document.querySelector('.portfolio-image#right-image img')
nodeImage = image.cloneNode(true)
nodeImage.appendChild(image)

3.
let portfolioContainer = document.querySelector('.portfolio-container'); 
    let pikachuImage = document.querySelector('.portfolio-image#right-image img'); 
    for (let i = 1; i <= 10; i++) { let dupPikachuImage = pikachuImage.cloneNode(true); portfolioContainer.appendChild(dupPikachuImage); }

4. 
const listItem = document.createElement('li')
const leftspan = document.createElement('span')
var lastUpdated = document.createTextNode('Page last updated on');
leftspan.appendChild(lastUpdated)
listItem.appendChild(leftspan)
let bio = document.querySelector('ul.bio-info')
bio.appendChild(listItem)
var time = new Date()

const rightspan = document.createElement('span')
var timeText = document.createTextNode(time)
rightspan.appendChild(timeText)
listItem.appendChild(rightspan)