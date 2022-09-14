# Opdrachten

Voer de onderstaande opdrachten in volgorde uit. Deze opdrachten lopen in principe op in grootte en complexiteit.

Een deel van deze opdrachten wordt uitgevoerd in de terminal. Start deze alvast op en controleer of de docker engine
draait door het volgende commando uit te voeren:

```bash
docker ps
```

Output:

```bash
$ docker ps
CONTAINER ID   IMAGE                     COMMAND                  CREATED        STATUS      PORTS                    NAMES
```

## Opdracht 1: Pre-built container

Gebruik het Docker run commando om een NGiNX docker container te starten. Bind poort `80` van de container aan poort
`8080` van de host (of een andere als deze al in gebruik is).

Controleer dat de container goed gestart is door in een browser naar <http://localhost:8080> te navigeren.

Bekijk hiernaar de images en de containers die op jouw computer staan met de volgende commando's:

```bash
docker image ls
docker image history nginx
docker ps
docker ps -a # all, dus ook gestopte containers
docker container ls -a # Equivalent van docker ps -a
```

## Opdracht 2: Volume mounting

We willen nu dat de nginx container de website in de 'event' folder van deze repository gaat weergeven. Hiervoor kunnen
we deze folder mounten als volume. Op deze manier heeft de container er toegang tot. Als we deze folder mounten op de
folder `/usr/share/nginx/html` van de container wordt deze gelijk gehost.

Start dezelfde NGiNX container uit de vorige opdracht op, en mount de event folder op de aangegeven folder van de
container. Let op dat je `${PWD}` kan gebruiken om de current directory te krijgen.

Als je nu naar <http://localhost:8080> gaat, zou hier een scherm zichtbaar moeten zijn met NAVARA in beeld.

## Opdracht 3: NGiNX source code

De `Dockerfile`s ontwikkeld door Docker (met het label "Docker Official Image") zijn publiekelijk toegankelijk. Zoek op
[docker hub](https://hub.docker.com) de image voor NGiNX, vindt de GitHub repo, kijk naar de `Dockerfile` en probeer te
snappen hoe zij hun Dockerfile opgebouwd hebben. Let op de volgende zaken:

* Wat is de base image?
* Welke layers worden er gedefinieerd?
* Welke environment variables worden er gezet?
* Wat voor labels worden er gezet?

## Opdracht 4: Build docker container

Deze repository bevat 2 folders met zelf ontwikkelde code; frontend en backend. Voor beide applicaties moet een image
ontwikkeld worden. Het is aan jou de keuze welke van de 2 je ontwikkelt. De andere mag gekopieerd worden van de
antwoorden.

### Opdracht 4a: Backend

Deze applicatie is geschreven in Python en gebruikt Poetry als dependency manager. Poetry wordt niet standaard
meegeleverd dus moet eerst geinstalleerd worden in de image.

Om Poetry te installeren op een Linux omgeving  moet `/root/.local/bin` toegevoegd worden aan `PATH`. Dit kan je doen
met een environment variabele. Verder moeten de volgende commando's uitgevoerd worden:

```bash
curl -sSL https://install.python-poetry.org | python -
poetry config virtualenvs.create false
```

Logischerwijs moeten de dependencies ook geinstalleer worden. Dit gebeurt met `poetry install`.

Het commando dat uiteindelijk gebruikt moet worden om het proces te starten is `serve`. (N.B. dit is een alias voor een
entrypoint van het python programma)

### Opdracht 4b: Frontend

De frontend is geschreven in VueJS en gebruikt NPM voor het installeren van dependencies. Voor het installeren van de
dependencies kan het commando `npm ci` gebruikt worden.

Hou er rekening mee dat een image voor een frontend vaak een focus op het build proces heeft, en niet zozeer op het
continue draaien van software. Dit betekent dat de container eenmalig een commando uitvoert en daarna stop. Het commando
om uit te voeren tijdens runtime is dus ook `npm run build`. Dit levert een `dist` folder op in de huidige working
directory.

**Extra:** Om te testen dat de image gebouwd is zoals zou moeten, kan je met het `docker run` commando je `CMD`
overschrijven. Dit doe je door het commando als laatste argument toe te voegen (e.g. `docker run ... bash`). Draai het
commando `npm run dev` en zorg dat poort 3000 bereikbaar is op de host.

## Opdracht 5: Run multiple containers

Containers kunnen via de CLI gestart en handmatig gekoppeld worden met netwerken, maar dit is eenvoudiger te bereiken
met docker-compose files. Gebruik de `docker-compose.yaml` file in `docker/`.

In totaal gaan er 4 containers opgestart worden: NGiNX, frontend, backend en mongodb. De frontend container genereert de
source files die geserved moeten worden door NGiNX. De backend container draait een simpele python server, waarbij
gebruik gemaakt wordt van een Mongo NoSQL database.

De frontend/backend image kan automatisch worden gebouwd uit de lokale folders bij het draaien van docker compose up.
Hiervoor moet je bepaalde instellingen meegeven in de docker compose file. Voor de Dockerimage uit opdracht 4 die je
niet zelf geschreven hebt kan je `oschusler/kennisfestival-docker-backend` of `oschusler/kennisfestival-docker-frontend`
gebruiken.

* De frontend image moet de environment variabele `VITE_ROOT_API: http://localhost:5002` meekrijgen.
* De NGiNX container heeft een volume gemount, met daarin de `dist` folder uit frontend. Dit gebeurt standaard op
  `/usr/share/nginx/html/`
* De NGiNX container mount poort 80 op een poort op het host systeem (e.g. 5001).
* De mongo container wordt opgestart, en hoeft verder niks speciaals te doen. Note, de standaard poort is 27017.
* De backend image heeft de environment variabele `MONGO_CONNECTION_STRING: "mongodb://<db_service_name>:27017/"` en
  `BACKEND_CORS_ORIGINS: '["*"]'` nodig.

Hint: Gebruik de officiele documentatie voor het docker compose format
<https://docs.docker.com/compose/compose-file/compose-file-v3/>

## Opdracht 6: Run development in Docker containers

In de vorige opdracht heb je een docker compose file geschreven met daarin een NGiNX container die een frontend build
served. Veel frontend frameworks - inclusief Vue - hebben een ingebouwd development server. Bouw de docker compose file
om dat deze development server direct aangeroepen wordt in de frontend container (hint: NGiNX is niet meer nodig).

Aangezien het om een development omgeving gaat, moet je ook de code volume mounten. Dit betekent dat je een wijziging in
de code kan aanbrengen, en dit meteen in de browser terug ziet.

In dit geval moet niet alleen de server gestart worden met het `command`. Aangezien de hele source directory
overschreven wordt, moeten de dependencies ook geinstalleerd worden. Het `commando` is in dit geval
`sh -c "npm install && npm run dev"`.
