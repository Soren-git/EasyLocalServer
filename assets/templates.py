resources = """
[cfx]
ensure mapmanager
ensure chat
ensure spawnmanager
ensure sessionmanager
ensure basic-gamemode
ensure hardcap
ensure rconlog
"""

server = """
endpoint_add_tcp "0.0.0.0:30120"
endpoint_add_udp "0.0.0.0:30120"

sv_scriptHookAllowed 0

#set rcon_password ""

sets tags {tags}
sets locale "fr-FR"
#sets banner_detail "https://url.to/image.png"
#sets banner_connecting "https://url.to/image.png"
sv_hostname {serverName}
sets sv_projectName {serverName}
sets sv_projectDesc {serverDescription}

#sv_enforceGameBuild 2802
exec resources.cfg

#load_server_icon myLogo.png

set temp_convar "hey world!"

#sv_master1 ""

add_ace group.admin command allow # allow all commands
add_ace group.admin command.quit deny # but don't allow quit
add_principal identifier.fivem:1 group.admin # add the admin to the group

set onesync on
sv_maxclients 48
#set steam_webApiKey ""
sv_licenseKey {serverPatreon}
"""