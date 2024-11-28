Lo svolgimento prevede la valutazione dei seguenti obiettivi:

1. mettere in comunicazione tra loro i diversi ambienti che il candidato troverà nei repository (✔)
    >> Aggiunto external network a tutti i docker-compose dei vari ambienti.

2. eseguire un test di connessione presente dall'app fastapi mediante apposito endpoint (allegare screenshot del risultato del test) (✔)
    >> Eseguito il curl dell'endpoint /health-db e riscontrata la connessione al database dall'app fastapi.

3. inizializzare il database con le migrazioni, secondo la guida elencata a seguito nello scenario
    >> Eseguito il comando { docker exec -it fastapi-application bash } per collegarmi alla bash del container;
    >> eseguito in bash il comando { alembic revision --autogenerate -m "create users table" } con riscontro di versione DB outdated;
    >> eseguito in bash il comando { alembic upgrade head } con riscontro positivo,
       il database ha creato la table "users" e la table "alembic_version".

4. eseguire almeno due inserimenti tramite endpoint (allegare screenshot del risultato della chiamata)
    >> Eseguito il curl di due inserimenti tramite /users endpoint.

5. eseguire qualche chiamata ai diversi endpoint
    >> Eseguito il curl tramite { curl http://localhost:8000/users/ } e { curl http://localhost:8000/users/iduser/ }.

6. procedere al test di carico mediante applicazione locust ed estrarne dati (allegare screenshot)
    >> Per il test di locust ho aggiunto un endpoint per l'id di Jane Doe.