> > # GDPS DISCORD BOT "API"

## Imports:
```py
from gdps import *
```

## Level
```py
@bot.commands()
async def command_name(ctx, identify):
    level = await fetch_level(identify)
```
## Available level information
> ### Level Id -> level.id() -> `int`
> ### Level Name -> level.name() -> `str`
> ### Level Description -> level.description() -> `str`
> ### Level Objects count -> level.objects() -> `int`
> ### Level Version -> level.version() -> `int`
> ### Level Author Id -> level.author_id() -> `int`
> ### Level Official Song -> level.official_song() -> `bool`
> ### Level Custom Song -> level.custom_song() -> `bool`
> ### Level Requested Rate -> level.requested_rate() -> `int`
> ### Level Difficulty -> level.difficulty() -> `int`
> ### Level Coins -> level.coins() -> `int`
> ### Level Coins Verified -> level.coins_verified() -> `bool`
> ### Level Downloads -> level.downloads() -> `int`
> ### Level Likes -> level.likes() -> `int`
> ### Level Demon -> level.demon() -> `bool`
> ### Level Demon Difficulty -> level.demon_difficulty() -> `int`
> ### Level Stars -> level.stars() -> `int`
> ### Level Featured -> level.featured() -> `bool`
> ### Level Auto -> level.auto() -> `bool`
> ### Level Epic -> level.epic() -> `bool`
> ### Level Password -> level.password() -> `int`
> ### Level Original -> level.original() -> `int`
> ### Level Copy -> level.is_copy() -> `bool`