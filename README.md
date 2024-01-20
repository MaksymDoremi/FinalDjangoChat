# FinalDjangoChat

## Úvod
FinalDjangoChat je aplikace na bázi Django, Channels a Websocketu.

## Features
- User authentication
- Chat rooms
- Creating chat rooms
- Channels, Websocket
- SQLite
- API

## Endpointy
`login/`  
Login na stránku, používa username a password

`logout/`  
Logout ze stránky, vymaže session

`registration/`  
Registrace na stránku pomocí username, password1, password2

`rooms/`  
Zobrazení všech chatovacíh roomek

`room/room_name/`  
Při kliknuti na room přesměruje do samotné roomky s chatem

## API
`api/messages/`  
vratí všechny zprávy ze všech roomek a od všech uživatelů  

`api/messages/username/<str:username>`  
vratí všechny zprávy od zadaného uživatele  

`api/messages/room/<str:room_name>`  
vratí všechny zprávy z roomky  

`api/messages/contains/<str:word>`  
vratí všechny zprávy obsahující zadané slovo, case insensitive  

`api/create_room/`    
vytvoří novou roomku    

Project Link: [https://github.com/MaksymDoremi/FinalDjangoChat](https://github.com/MaksymDoremi/)
