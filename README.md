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

---
## Try it live!
##### Text any English word to the following number:
```
+1 973 354 5746
```

-----
## Build and run your own version locally with DOCKER ->

```
docker-compose up -d --build
```
#### (_requires your own version of the following accounts_):
- Twilio messaging service
- OED API
- Heroku

---
## Use HEROKU and DOCKER to build and deploy your app ->
### Steps (overview):
- [Sign up](https://signup.heroku.com/) for a Heroku account
- Install the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- Create a new app
- Log in to the Heroku Container Registry
- Build the production image
- Push the image to the registry
- Release the image

### Steps (detail):

#### Create a new app
```
$  heroku create

Creating app... done, ⬢ tranquil-waters-49458
https://tranquil-waters-49458.herokuapp.com/ | https://git.heroku.com/tranquil-waters-49458.git
```

#### Log in to the [Heroku Container Registry](https://devcenter.heroku.com/articles/container-registry-and-runtime):
```

$  heroku container login

```

#### Build and tag it according to this format: 

```

registry.heroku.com/<app>/<process-type>

```

##### Make sure to replace `<app>` with the name of _your_ app, and `<process-type>` with `web` ->

```

$  docker build -f Dockerfile.prod -t registry.heroku.com/tranquil-waters-49458/web .

```

#### Push the image to the registry:
```

$  docker push registry.heroku.com/tranquil-waters-49458/web:latest

```
#### Release the image:
```
$  heroku container:release web --app tranquil-waters-49458
```

### That's it! 
