# Personnal PoC of vector Database (On Weaviate client)

## Main Goals

Here the main goal was purly educatif and to test a bit the newer technologies based on NLP semetic and vector DB

- Get a quick overview of the implementation of a Database vector
- Make a simple back-end application to retreive similars words

## Usage

Install the requirements.txt on your favorite env manager

Simply run the docker compose file
```
docker compose up
```
And then launch the set-up -- As there is no bulk here, the running time is a bit slow (average 8 minutes on M2 Max Mac)
```
python startup.py
```
And finnaly launch the web server
```
python main.py
```

Then make any call you what with a english word folling this endpoint
```
http://localhost:5050/similarity/<word>
```

## What Next?

**In the order of priority**

- Make real bulking adding
- Add more sofisticated Schemas with relationnel into (Dependance to others Schemas)
- Make usage of the ASK module (Weaviate special module)
- Get deepers understading on what is all about -- Try it for real case uses