## Lupin got a bot.

I wanted to mess around with heroku and python so I decided to make a stupid bot that poorly translates tweets by subbing out words for dog sounds. 

![Screenshot 2022-09-09 at 4 31 28 PM](https://user-images.githubusercontent.com/25188844/189438482-5cc9061d-78c2-40c3-a974-8ef4e3109dc9.png)

### So what is this?

I built a web scraper using the beautiful-soup library that sources quotes from GoodReads and saves the quotes in a json file. Once the quotes were saved and structured in the proper format, a random quote object would be selected and ran through a function that swaps out selected words (sourced from a list) and then replaces them with a dog sound (also sourced from a seperate list in said function). The final tweet is formed of the translated quote, author and an uncertain phrase that is placed at the end of the tweet.

### What's next?

Right now it just tweets at the top of the hour but I plan on adding :
<ul>
<li> Having the bot reply to DM's </li>
<li> Replying to messages and hashtags</li>
<li> Liking and retweeting certain tweets</li>
<li> Expanding the array of things the bot can tweet </li>
</ul>
