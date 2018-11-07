![feeder_logo](https://github.com/holgerimbery/environment/raw/master/feeder_logo_small.jpg)

### feeder-button - das RaspberryMatic Addon für Feeder

Um RaspberryMatic zu entlasten können Elemete auf mehrer RaspberryPis im Docker Swarm Modus ausgelagert werden.

[Feeder-IoT-stack](https://github.com/holgerimbery/feeder-stack) liefert diese Elemente mit einer einfachen graphischen Installationsroutine nach.
* influxdb (als timebased Datenbank)
* telegraf & kapacitor (für Alerts)
* chronograf (als Oberfläche für influxdb, kapacitor & telegraph)
* portainer als GUI für docker, templates für die Installation aller Komponenten sind in portainer integriert

Dieses Add-on integriert einen Button unter der Homematic UI (Einstellungen/Systemsteuerung), um leichter auf die feeder Installation zugreifen zu können.

[feeder-cluster](https://github.com/holgerimbery/feeder-stack) schafft die Basis für diese Installation in Form eines Raspberry Pi Clusters das ohne SD-Cards auskommt. Der Master startet von SSD und stellt sie Filesysteme aller Nodes via NFS zur Verfügung. Lediglich zur Installation wird eine SD-Card benötigt.
