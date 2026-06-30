# Text-based RPG (+ bonus multiplayer via sockets)

Een turn-based tekst-RPG in de terminal, gebouwd met OOP. De speler loopt door levels, vecht tegen vijanden, verzamelt en gebruikt items, en wint door alle vijanden te verslaan.

## Hoe start je hem? (singleplayer)

Vanuit de map `les23_rpg/`:

```
python main.py
```

Geef je personage een naam en speel met de volgende commando's:

| Commando | Werking |
|---|---|
| `look` | Toont de levelbeschrijving, vijanden, items en uitgangen |
| `fight` | Valt een vijand aan (vraagt om een keuze als er meerdere zijn) |
| `take <item>` | Pakt een item op uit het huidige level |
| `use <item>` | Gebruikt een item uit je inventory |
| `go <richting>` | Loopt naar een ander level (alleen als alle vijanden hier verslagen zijn) |
| `status` | Toont je HP, attack en inventory |
| `quit` | Stopt het spel |

## Projectstructuur

```
les23_rpg/
├── main.py                     # maakt player + levels, start de game
├── game.py                     # de Game engine (game-loop, command handling)
├── models/
│   ├── player.py                # Player class
│   ├── enemy.py                 # Enemy class
│   ├── item.py                  # Item class
│   └── level.py                 # Level class
└── bonus_multiplayer/
    ├── server.py                 # socket-server (single client)
    └── client.py                 # socket-client
```

## Spelmechanica

- **Player**: heeft hp, max_hp, attack_power en een inventory. Kan aanvallen, schade nemen, helen en items gebruiken.
- **Enemy**: heeft hp en attack_power. Valt automatisch terug aan tijdens `fight` zolang hij nog leeft.
- **Item**: heeft een type (`heal` of `attack_boost`) en een value. `apply(player)` voert het effect uit.
- **Level**: bevat een beschrijving, een lijst vijanden, een lijst items en een dict met uitgangen (richting → levelnaam). Je kunt een level pas verlaten als alle vijanden er verslagen zijn.
- **Game**: de engine die alles samenbrengt. `run()` bevat de game-loop: status tonen → input vragen → commando verwerken → win/lose checken → herhalen.

De meegeleverde wereld bestaat uit drie levels: **Forest** (met een Wolf en een Potion) → **Cave** (met een Goblin en een Sword) → **Boss Room** (met een Dragon). Je wint zodra alle vijanden in alle levels verslagen zijn.

## Bonus: Multiplayer via sockets

`bonus_multiplayer/` bevat een werkende client/server-opzet voor **één** speler over het netwerk (single-client). De server bewaart de echte game state; de client stuurt alleen tekstcommando's en toont het antwoord.

### Starten

Terminal 1 (server):
```
cd bonus_multiplayer
python server.py
```

Terminal 2 (client):
```
cd bonus_multiplayer
python client.py
```

### Protocol

- Client → server: tekstcommando's zoals `LOOK`, `FIGHT`, `TAKE potion`, `USE potion`, `GO east`, `STATUS`, `QUIT` (hoofdletterongevoelig).
- Server → client: tekstantwoord met de uitkomst van het commando.

### Wat is wel/niet geïmplementeerd

✅ Eén client kan volledig over het netwerk spelen (look, fight, take, use, go, status, quit).
✅ Server beheert de game state centraal; de client bevat zelf geen spellogica.
❌ Twee spelers tegelijk met beurten en broadcasting is **niet** geïmplementeerd — dat is een forse uitbreiding (turn-management, state per speler, broadcast naar meerdere sockets) die in de opdracht zelf ook als "uitdagend, prima als je tot 1 client komt" wordt aangemerkt.

## Wat heb ik geleerd?

- Een grotere game-engine bouwen met meerdere samenwerkende classes (Player, Enemy, Item, Level, Game) die elk hun eigen verantwoordelijkheid hebben.
- Werken met lijsten en dicts van objecten: een level houdt zijn vijanden en items bij in lijsten, en zijn uitgangen in een dict.
- Een turn-based combat-systeem bouwen waarbij de speler aanvalt en de vijand automatisch terugslaat.
- Een command-loop bouwen die tekstinvoer omzet naar acties (vergelijkbaar met een mini-parser).
- Basis netwerken met de `socket`-module: een server die luistert/accepteert, en een client die verbindt en commando's stuurt. Door de bestaande `Game`-class te hergebruiken (in plaats van alles opnieuw te bouwen) kon ik output afvangen met `contextlib.redirect_stdout` en als tekst over het netwerk versturen, zodat singleplayer- en multiplayer-logica niet dubbel hoefden te bestaan.
