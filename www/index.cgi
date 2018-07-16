#!/bin/tclsh

set FILENAME "/usr/local/addons/feeder-button/host.conf"

set host 192.168.001.100

array set args { command INV host 192.168.001.100 }

proc parseQuery { } {
	global args env
	
	set query [array names env]
	if { [info exists env(QUERY_STRING)] } {
		set query $env(QUERY_STRING)
	}
	
	foreach item [split $query &] {
		if { [regexp {([^=]+)=(.+)} $item dummy key value] } {
			set args($key) $value
		}
	}
}


proc loadFile { fileName } {
	set content ""
	set fd -1
	
	set fd [ open $fileName r]
	if { $fd > -1 } {
		set content [read $fd]
		close $fd
	}
	
	return $content
}

proc loadConfigFile { } {
	global FILENAME host
	
	array set content {HOST 127.0.0.1}
	catch { array set content [loadFile $FILENAME] }
	
	set host $content(HOST)


}

proc saveConfigFile { } {
	global FILENAME args
	
	array set content {}
	set content(HOST) $args(host)

	
	set fd [open $FILENAME w]
	puts $fd [array get content]
	close $fd
}

parseQuery
if { $args(command) == "save" } {
	saveConfigFile
	catch { close [open "|/usr/local/addons/feeder-button/update_cfg > /usr/local/addons/feeder-button/feeder-button.log"] }
} 

loadConfigFile


set content [loadFile index.template.html]
regsub -all {<%host%>} $content $host content



puts $content
