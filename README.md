retired - please have a look at my balena [IoT-Stack](https://github.com/holgerimbery/balena-labs)
![feeder_logo](https://github.com/holgerimbery/environment/raw/master/feeder_logo_small.jpg)

### feeder-button - das RaspberryMatic Addon für Feeder

Eine (vorhandene) Feeder Installation kann dazu genutzt werden neben anderen Aufgaben auch RaspberryMatic zu entlasten.
Hierbei werdenzusätzliche IoT Elemete auf mehrer RaspberryPis im Docker Swarm Modus ausgelagert.

[Feeder-stack](https://github.com/holgerimbery/feeder-stack) liefert diese Elemente mit einer einfachen graphischen Installationssroutine nach.
* influxdb (als timebased Datenbank)
* telegraf & kapacitor (für Alerts)
* chronograf (als Oberfläche für influxdb, kapacitor & telegraph)
* portainer als GUI für docker, templates für die Installation aller Komponenten sind in portainer integriert

Dieses Add-on integriert einen Button unter der Homematic UI (Einstellungen/Systemsteuerung), um leichter auf die feeder Installation zugreifen zu können.

[feeder-cluster](https://github.com/holgerimbery/feeder-cluster) schafft die Basis für diese Installation in Form eines Raspberry Pi Clusters das ohne SD-Cards auskommt. Der Master startet von SSD und stellt die Filesysteme aller Nodes via NFS zur Verfügung. Lediglich zur Installation wird eine SD-Card benötigt.
