# feeder-button

### feeder-button das RaspberryMatic Addon für Feeder

Um RaspberryMatic zu entlasten können Elemete auf einen weiteren RaspberryPi mit Docker oder auf mehrer RaspberryPis im Docker Swarm Modus ausgelagert werden.
[Feeder](https://github.com/holgerimbery/feeder) liefert diese Elemente mit einer einfachen graphischen Installationsroutine nach.
* NODE-RED (als Logikschicht)
* influxdb (als timebased Datenbank)
* telegraf & kapacitor (für Alerts)
* chronograf (als Oberfläche für influxdb, kapacitor & telegraph)
* portainer als GUI für docker, templates für die Installation aller Komponenten sind in portainer integriert

Dieses Add-on integriert Buttons unter der Homematic UI (Einstellungen/Systemsteuerung), um leichter auf die feeder Installation zugreifen zu können.
