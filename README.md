<p align="center">
  <img src="https://github.com/Paxnar/EntralinkedRandomizer/assets/67262211/cb2a67a4-842c-4260-b436-cf02493c129c" alt="icon"/>
</p>
<h1 align="center">Entralinked Randomizer</h1>
<p align="center">
  <a href="https://github.com/Paxnar/EntralinkedRandomizer/releases/latest"><img src="https://img.shields.io/github/v/release/Paxnar/EntralinkedRandomizer?labelColor=30373D&label=Release&logoColor=959DA5&logo=github&filter=*" alt="release"/></a>
</p>

Entralinked Randomizer is a randomizer for kuroppoi's [Entralinked](https://github.com/kuroppoi/entralinked/) standalone Game Sync emulator developed for use with Pokémon Black & White and its sequels.\
It randomizes Items, Dream World areas, Pokemon, their moves, forms and more.

<!-- For users: [Quick Setup Guide](https://github.com/kuroppoi/entralinked/wiki/Setup) -->

## Building

#### Prerequisites

- python>=3.8.5
- requests>=2.26.0
- PyQt5>=5.15.4
- pyinstaller>=4.6

```
pyinstaller --onefile --noconsole main.py
```

## Usage

1. Run Entralinked.
1. Ensure you tucked in a Pokemon.
1. Run Entralinked Randomizer.
1. Select the game version you are playing (some encounters only appear when you're using a certain version of the games).
1. Input your Game Sync ID.
1. Select the number of pokemon you want to generate or click Random for a random amount.
1. Select the number of items you want to generate or click Random for a random amount.
1. Some pokemon and areas can only appear if you have a certain amount of points, if you want to use imaginary points, check the box that says Use Points? and input the amount of points you have. Not checking the box will ignore the points requirement for Pokemon and areas.
1. Areas that house a certain type have a higher chance of appearing if your sleeping Pokemon's type matches that type. If you want to use this feature, check the Use Pokemon's type? box and click Get.
1. Select the [areas](https://bulbapedia.bulbagarden.net/wiki/Pok%C3%A9mon_Dream_World#Areas) where you want to randomize Pokemon from or select none for a random location.
1. Click Roll to see what results you get.
1. Observe the results.
1. Click Reroll if you're not satisfied, or click Save if you are.
1. You can now either check you Entralinked dashboard to check if everything worked or wake up your Pokemon.
![image](https://github.com/Paxnar/EntralinkedRandomizer/assets/67262211/d7daf3c8-3404-4702-b1a9-66497047e7f5)
