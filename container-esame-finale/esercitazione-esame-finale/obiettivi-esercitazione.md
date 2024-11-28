# Obiettivi esercitazione
L'esercitazione proposta verrà valutata con un massimo di 7 punti dei 30 previsti per la verifica finale.

La scadenza fissata per eventuali domande di chiarimento è mercoledì alle ore 10.
La scadenza per la consegna é venerdì 29 alle ore 16.

La consegna dovrà avvenire mezzo piattaforma FAD, allegando uno zip che contenga tutti i file scaricati dai relativi repository, non saranno ammesse consegne in formato diverso.


I repository di partenza sono i seguenti:
- https://github.com/CSP2325-containers/esercitazione-esame-finale-db.git
- https://github.com/CSP2325-containers/esercitazione-esame-finale.git
- https://github.com/CSP2325-containers/esercitazione-esame-finale-load-test.git

Lo svolgimento prevede la valutazione dei seguenti obiettivi:
1. mettere in comunicazione tra loro i diversi ambienti che il candidato troverà nei repository
2. eseguire un test di connessione presente dall'app fastapi mediante apposito endpoint (allegare screenshot del risultato del test)
3. inizializzare il database con le migrazioni, secondo la guida elencata a seguito nello scenario
4. eseguire almeno due inserimenti tramite endpoint (allegare screenshot del risultato della chiamata)
5. eseguire qualche chiamata ai diversi endpoint
6. procedere al test di carico mediante applicazione locust ed estrarne dati (allegare screenshot)

Scenario

Nel repository esercitazione-esame-finale é stata terminata una applicazione, un microservizio che prevede lútilizzo di un database già esistente e che venga testato con un minimo di traffico.
Per fare questo é stato predisposto un repository con un database simile a quello in produzione che deve essere avviato e aggiornato, eseguendo le migrazioni che creano le tabelle richieste.
Avendo in esecuzione i file docker compose presenti in ogni repository, é possibile simulare l'infrastruttura in produzione e procedere ai test.

Nel repository esercitazione-esame-finale-db é presente il file docker compose che avvia il database e un tool di gestione per verificare se le migrazioni siano state completate e se i dati siano stati inseriti.

Dopo aver avviato l'applicativo oggetto del test è possibile verificare la corretta connessione al database attraverso l'endpoint "/health-db".

Se il DB risulta raggiungibile allora si devono eseguire i seguenti comandi collegandosi direttamente al container in esecuzione tramite riga di comando

Il seguente per creare una versione di migrazione
alembic revision --autogenerate -m "create users table"
il seguente per eseguire la mighrazione e creare la tabella users
alembic upgrade head

Avendo a disposizione l'applicativo Fastapi funzionante, si può procedere all'inserimento di qualche utente tramite richiesta Curl o postman,
le api si apettano aun richiesta POST con il seguente payload (di esempio) in formato JSON
{"name": "John Doe 2", "email": "john.doe2@example.com"}

Una volta avviato e configurato anche l'applicativo "locust" presente nel repository esercitazione-esame-finale-load-test è possibile visitare il sito di gestione http://localhost:8089/ e lanciare un test di carico, da evitare configurazioni troppo onerose e regolarsi sulla macchina host a disposizione.

Effettuati gli screenshot richiesti, racchiudere tutto il materiale in una zip e consegnarlo sulla piattaforma FAD per la valutazione.


