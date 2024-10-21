GLAgent CLI for WoT

# Description (en)

glAgent is a tool, developed in Python, for discovering WoT directories according to W3C recommendation and seeing/using Things connected to it.

First of all, you need to use my Thing Directory (project by Linksmart) repo fork and then turn DNS-SD on _wot._tcp.local.

After that, make sure to connect a Thing to it (it's preferable to it be a Server as well), and send it's Thing Description. On my Github there is a repo example using ESP32 under the name of <b>ESP32-TDD</b>.

All set? Then just use the commands below to use it.

# Description (pt)

O glAgent é uma ferramenta, desenvolvida em Python, para descoberta de diretórios de Web das Coisas de acordo com a W3C para usar ou ver Things conectadas a um diretório.

Primeiramente, use o meu fork do Thing Directory (projeto da Linksmart) e habilite DNS-SD para _wot._tcp.local.

Depois, conecte uma Thing ao repositório (de preferência que funcione como um Servidor também), e envie a sua Thing Description. No meu pergil tem um repositório de example, <b>ESP32-TDD</b>.

Tudo pronto? Então só use um dos comandos abaixo para usar.

# Commands

positional arguments:
  {discover,connect,list,endpoints}
    discover            Discover WoT directories
    connect             Connect to a WoT directory
    list                List all Things in the connected WoT directory
    endpoints           List all endpoints of a specific Thing

options:
  -h, --help            show this help message and exit