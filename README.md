# **OEDbot** - Oxford English Dictionary word looker-upper 


#### _SMS-based app that does only one thing, but does it well -> returns the OED definition of any English word texted to it_. 

### Application Flow
- Using the default SMS function on any phone, user texts a single English word to a US phone number 
- Within 2 seconds, user receives as response the OED's top definition of that word
- If the user texts a nonsense or non-English word, the response informs user that this word is not in the OED.
  
#### _Example 1_:
- User texts the word "oscillate" to +1 973 354 5746
- OEDbot sends back (within 2 seconds), the following response:
  - "'oscillate': move or swing back and forth at regular speed."    

#### _Example 2_:
- **_User_** -> "haptic"
- **_OEDbot_** ->  "'haptic': relating to the sense of touch, in particular relating to the perception and manipulation 
      of objects using the sense of touch and proprioception."

#### Example 3:
- **_User_** -> "xxffcdkjllc"
- **_OEDbot_** -> "'xxffcdkjllc': Sorry, the OED has no entry for that word."
    
#### Example 4:
- **_User_** -> "danke"
- **_OEDbot_** -> "'danke': Sorry, the OED has no entry for that word."



### Moving parts
- Python
- Flask
- Docker
- Heroku
- Twilio
- [ngrok](https://ngrok.com/) (for testing locally)  
- [Oxford English Dictionary API](https://developer.oxforddictionaries.com/documentation)

### Try a live version ->
##### Text any English word to the following number:
```
+1 973 354 5746
```

### Run the app ->

```
docker-compose up -d --build
```
