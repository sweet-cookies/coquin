# Coquin card game

Le jeu de carte coquin: [https://coquin.art](https://coquin.art)

# Regenerate all cards

```
# https://developers.google.com/sheets/api/quickstart/python
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
python extra/generate.py
```

# Build and push of the docker image

```
sudo docker build  -f Dockerfile -t coquin/coquin .
sudo docker push coquin/coquin
```

# Develop

  * Source of all cards and decks https://docs.google.com/spreadsheets/d/17A_U8v6_rBv9a2ZGaV3P913XCINzKRm5XE2wx40sRqU/edit?usp=sharing

```
sudo docker build  -f Dockerfile.dev -t coquin .

# Run dev mode
sudo docker run -it -p 9999:8080 -p 8000:8000 -v $PWD:/coquin coquin -c "cd coquin && yarn serve"

# Run using ui
sudo docker run -it -p 9999:8080 -p 8000:8000 -v $PWD:/coquin coquin -c "cd coquin && vue ui -H 0.0.0.0"

```

Random commands used to bootstrap this project

```bash
# How the project have been initialized https://vuetifyjs.com/en/getting-started/quick-start
sudo docker run -it -p 9999:8080 -p 8000:8000 -v $PWD:/coquin coquin
vue create coquin
cd coquin
vue add vuetify
vue add vuex
# Got an error, had to do if from vue ui
vue add @vue/devtools
vue add vue-router
vue ui -H 0.0.0.0
# npm install --no-progress
```

