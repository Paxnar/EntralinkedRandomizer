import pandas as pd
import re
import random
PleasantForest = [{'name': 'Rattata', 'move': ['Quick Attack', 'Me First', 'Iron Tail'], 'ver': 'none', 'points': 'Default'}, {'name': 'Nidoran♀', 'move': ['Scratch', 'Sucker Punch', 'Super Fang'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Nidoran♂', 'move': ['Peck', 'Counter', 'Super Fang'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Oddish', 'move': ['Sweet Scent', 'Teeter Dance', 'Giga Drain'], 'ver': 'none', 'points': 'Default'}, {'name': 'Bellsprout', 'move': ['Vine Whip', 'Synthesis', 'Seed Bomb'], 'ver': 'none', 'points': 'Default'}, {'name': 'Ponyta', 'move': ['Tackle', 'Thrash', 'Heat Wave'], 'ver': 'none', 'points': 'Default'}, {'name': "Farfetch'd", 'move': ['Fury Cutter', 'Roost', 'Leaf Blade'], 'ver': 'none', 'points': 'Default'}, {'name': 'Doduo', 'move': ['Growl', 'Flail', 'Roost'], 'ver': 'none', 'points': 'Default'}, {'name': 'Exeggcute', 'move': ['Barrage', 'Synthesis', 'Giga Drain'], 'ver': 'none', 'points': 'Default'}, {'name': 'Lickitung', 'move': ['Lick', 'Sleep Talk', 'Rock Climb'], 'ver': 'none', 'points': 'Default'}, {'name': 'Tangela', 'move': ['Sleep Powder', 'Leech Seed', 'Seed Bomb'], 'ver': 'none', 'points': 'Default'}, {'name': 'Kangaskhan', 'move': ['Fake Out', 'Counter', 'Drain Punch'], 'ver': 'none', 'points': 'Default'}, {'name': 'Sentret', 'move': ['Scratch', 'Endure', 'Covet'], 'ver': 'none', 'points': 'Default'}, {'name': 'Igglybuff', 'move': ['Sing', 'Fake Tears', 'Helping Hand'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Mareep', 'move': ['ThunderShock', 'Reflect', 'Shock Wave'], 'ver': 'none', 'points': 'Default'}, {'name': 'Hoppip', 'move': ['Synthesis', 'Helping Hand', 'Bullet Seed'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Sunkern', 'move': ['Mega Drain', 'Sweet Scent', 'Earth Power'], 'ver': 'none', 'points': 'Default'}, {'name': 'Stantler', 'move': ['Tackle', 'Disable', 'Skill Swap'], 'ver': 'none', 'points': 'Default'}, {'name': 'Poochyena', 'move': ['Howl', 'Poison Fang', 'Dark Pulse'], 'ver': 'none', 'points': 'Default'}, {'name': 'Lotad', 'move': ['Absorb', 'Leech Seed', 'Water Pulse'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Taillow', 'move': ['Peck', 'Mirror Move', 'Tailwind'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Surskit', 'move': ['Bubble', 'Hydro Pump', 'Giga Drain'], 'ver': 'none', 'points': 'Default'}, {'name': 'Bidoof', 'move': ['Tackle', 'Aqua Tail', 'Secret Power'], 'ver': 'none', 'points': 'Default'}, {'name': 'Shinx', 'move': ['Charge', 'Magnet Rise', 'Night Slash'], 'ver': 'none', 'points': 'Default'}, {'name': 'Tympole', 'move': ['Round', 'Earth Power', 'Water Pulse'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Cottonee', 'move': ['Leech Seed', 'Encore', 'Worry Seed'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Petilil', 'move': ['Sleep Powder', 'Charm', 'Sweet Scent'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Karrablast', 'move': ['Endure', 'Megahorn', 'Bug Bite'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Shelmet', 'move': ['Acid', 'Baton Pass', 'Encore'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Glameow', 'move': ['Fake Out', 'Assurance', 'Secret Power'], 'ver': 'none', 'points': 5000}, {'name': 'Scolipede', 'move': ['Poison Tail', 'Toxic Spikes', 'Superpower'], 'ver': 'B2W2', 'points': 5000}, {'name': 'Psyduck', 'move': ['Water Sport', 'Encore', 'Brine'], 'ver': 'none', 'points': 7500}, {'name': 'Growlithe', 'move': ['Bite', 'Body Slam', 'Endure'], 'ver': 'none', 'points': 7500}, {'name': 'Scyther', 'move': ['Quick Attack', 'Baton Pass', 'Tailwind'], 'ver': 'none', 'points': 7500}, {'name': 'Tauros', 'move': ['Rage', 'Iron Tail', 'Rock Climb'], 'ver': 'none', 'points': 7500}, {'name': 'Marill', 'move': ['Defense Curl', 'Aqua Jet', 'Ice Punch'], 'ver': 'none', 'points': 7500}, {'name': 'Sudowoodo', 'move': ['Flail', 'Rollout', 'Role Play'], 'ver': 'none', 'points': 7500}, {'name': 'Girafarig', 'move': ['Confusion', 'Mirror Coat', 'Skill Swap'], 'ver': 'none', 'points': 7500}, {'name': 'Miltank', 'move': ['Defense Curl', 'Curse', 'Iron Tail'], 'ver': 'none', 'points': 7500}, {'name': 'Zigzagoon', 'move': ['Tackle', 'Trick', 'Last Resort'], 'ver': 'none', 'points': 7500}, {'name': 'Electrike', 'move': ['Thunder Wave', 'Ice Fang', 'Signal Beam'], 'ver': 'BW', 'points': 7500}, {'name': 'Castform', 'move': ['Ember', 'Ominous Wind', 'Water Pulse'], 'ver': 'BW', 'points': 7500}, {'name': 'Pachirisu', 'move': ['Quick Attack', 'Covet', 'Shock Wave'], 'ver': 'BW', 'points': 7500}, {'name': 'Buneary', 'move': ['Foresight', 'Fake Out', 'Drain Punch'], 'ver': 'none', 'points': 7500}, {'name': 'Vulpix', 'move': ['Roar', 'Heat Wave', 'Dark Pulse'], 'ver': 'none', 'points': 10000}, {'name': 'Poliwag', 'move': ['Hypnosis', 'Mist', 'Sleep Talk'], 'ver': 'none', 'points': 10000}, {'name': 'Natu', 'move': ['Night Shade', 'FeatherDance', 'Giga Drain'], 'ver': 'none', 'points': 10000}, {'name': 'Elekid', 'move': ['ThunderShock', 'Cross Chop', 'Magnet Rise'], 'ver': 'none', 'points': 10000}, {'name': 'Skitty', 'move': ['Foresight', 'Tickle', 'Captivate'], 'ver': 'none', 'points': 10000}]
WindsweptSky = [{'name': 'Butterfree', 'move': ['Confusion', 'Roost', 'Air Cutter'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Pidgey', 'move': ['Gust', 'Steel Wing', 'Secret Power'], 'ver': 'none', 'points': 'Default'}, {'name': 'Spearow', 'move': ['Peck', 'Faint Attack', 'Steel Wing'], 'ver': 'none', 'points': 'Default'}, {'name': 'Zubat', 'move': ['Supersonic', 'Hypnosis', 'Super Fang'], 'ver': 'none', 'points': 'Default'}, {'name': 'Aerodactyl', 'move': ['Bite', 'Assurance', 'Stealth Rock'], 'ver': 'none', 'points': 'Default'}, {'name': 'Hoothoot', 'move': ['Foresight', 'Night Shade', 'Recycle'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Ledyba', 'move': ['Comet Punch', 'Bug Bite', 'ThunderPunch'], 'ver': 'none', 'points': 'Default'}, {'name': 'Hoppip', 'move': ['Synthesis', 'Encore', 'Bounce'], 'ver': 'none', 'points': 'Default'}, {'name': 'Yanma', 'move': ['Quick Attack', 'Feint', 'Giga Drain'], 'ver': 'none', 'points': 'Default'}, {'name': 'Murkrow', 'move': ['Peck', 'Confuse Ray', 'Roost'], 'ver': 'none', 'points': 'Default'}, {'name': 'Gligar', 'move': ['Sand-Attack', 'Feint', 'Tailwind'], 'ver': 'none', 'points': 'Default'}, {'name': 'Delibird', 'move': ['Present', 'Ice Shard', 'Focus Punch'], 'ver': 'none', 'points': 'Default'}, {'name': 'Taillow', 'move': ['Peck', 'Endure', 'Brave Bird'], 'ver': 'none', 'points': 'Default'}, {'name': 'Wingull', 'move': ['Water Gun', 'Twister', 'Shock Wave'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Swablu', 'move': ['Peck', 'FeatherDance', 'Roost'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Staravia', 'move': ['Wing Attack', 'FeatherDance', 'Tailwind'], 'ver': 'none', 'points': 'Default'}, {'name': 'Pidove', 'move': ['Gust', 'Hypnosis', 'Morning Sun'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Sigilyph', 'move': ['Hypnosis', 'Stored Power', 'Heat Wave'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Ducklett', 'move': ['Defog', 'Brine', 'Me First'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Emolga', 'move': ['Quick Attack', 'Air Slash', 'Charm'], 'ver': 'B2W2', 'points': 5000}, {'name': 'Skarmory', 'move': ['Peck', 'Drill Peck', 'Roost'], 'ver': 'none', 'points': 7500}, {'name': 'Tropius', 'move': ['Gust', 'Leech Seed', 'Silver Wind'], 'ver': 'none', 'points': 7500}, {'name': 'Drifloon', 'move': ['Minimize', 'Hypnosis', 'Skill Swap'], 'ver': 'BW', 'points': 7500}, {'name': 'Chatot', 'move': ['Mirror Move', 'Nasty Plot', 'Role Play'], 'ver': 'BW', 'points': 7500}]
SparklingSea = [{'name': 'Slowpoke', 'move': ['Yawn', 'Block', 'Brine'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Seel', 'move': ['Headbutt', 'Icicle Spear', 'Sleep Talk'], 'ver': 'none', 'points': 'Default'}, {'name': 'Shellder', 'move': ['Withdraw', 'Barrier', 'Icy Wind'], 'ver': 'none', 'points': 'Default'}, {'name': 'Krabby', 'move': ['ViceGrip', 'Amnesia', 'Secret Power'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Horsea', 'move': ['Bubble', 'Octazooka', 'Brine'], 'ver': 'none', 'points': 'Default'}, {'name': 'Goldeen', 'move': ['Peck', 'Psybeam', 'Water Pulse'], 'ver': 'none', 'points': 'Default'}, {'name': 'Seaking', 'move': ['Water Pulse', 'Sleep Talk', 'Endure'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Staryu', 'move': ['Water Gun', 'Recycle', 'Icy Wind'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Magikarp', 'move': ['Splash', 'Flail', 'Bounce'], 'ver': 'none', 'points': 'Default'}, {'name': 'Omanyte', 'move': ['Bite', 'Muddy Water', 'Icy Wind'], 'ver': 'none', 'points': 'Default'}, {'name': 'Kabuto', 'move': ['Absorb', 'Flail', 'Stealth Rock'], 'ver': 'none', 'points': 'Default'}, {'name': 'Chinchou', 'move': ['Thunder Wave', 'Amnesia', 'Shock Wave'], 'ver': 'none', 'points': 'Default'}, {'name': 'Wooper', 'move': ['Water Gun', 'Body Slam', 'Aqua Tail'], 'ver': 'none', 'points': 'Default'}, {'name': 'Qwilfish', 'move': ['Poison Sting', 'Aqua Jet', 'Secret Power'], 'ver': 'none', 'points': 'Default'}, {'name': 'Corsola', 'move': ['Bubble', 'Confuse Ray', 'Stealth Rock'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Remoraid', 'move': ['Lock-On', 'Rock Blast', 'Brine'], 'ver': 'none', 'points': 'Default'}, {'name': 'Mantine', 'move': ['Supersonic', 'Mirror Coat', 'Air Cutter'], 'ver': 'none', 'points': 'Default'}, {'name': 'Wailmer', 'move': ['Water Gun', 'Sleep Talk', 'Bounce'], 'ver': 'none', 'points': 'Default'}, {'name': 'Barboach', 'move': ['Mud-Slap', 'Sleep Talk', 'Spark'], 'ver': 'none', 'points': 'Default'}, {'name': 'Clamperl', 'move': ['Whirlpool', 'Captivate', 'Aqua Ring'], 'ver': 'none', 'points': 'Default'}, {'name': 'Relicanth', 'move': ['Water Gun', 'Sleep Talk', 'Earth Power'], 'ver': 'none', 'points': 'Default'}, {'name': 'Luvdisc', 'move': ['Charm', 'Mud Sport', 'Icy Wind'], 'ver': 'none', 'points': 'Default'}, {'name': 'Buizel', 'move': ['Water Sport', 'Slash', 'Water Pulse'], 'ver': 'none', 'points': 'Default'}, {'name': 'Finneon', 'move': ['Attract', 'Sweet Kiss', 'Water Pulse'], 'ver': 'none', 'points': 'Default'}, {'name': 'Basculin', 'move': ['Headbutt', 'Agility', 'Zen Headbutt'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Basculin', 'move': ['Headbutt', 'Agility', 'Zen Headbutt'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Alomomola', 'move': ['Aqua Ring', 'Mirror Coat', 'Pain Split'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Stunfisk', 'move': ['Mud-Slap', 'Curse', 'Yawn'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Tirtouga', 'move': ['Rollout', 'Flail', 'Iron Defense'], 'ver': 'B2W2', 'points': 5000}, {'name': 'Tentacool', 'move': ['Supersonic', 'Acupressure', 'Giga Drain'], 'ver': 'none', 'points': 7500}, {'name': 'Carvanha', 'move': ['Bite', 'Thrash', 'Dark Pulse'], 'ver': 'none', 'points': 7500}, {'name': 'Corphish', 'move': ['Harden', 'Metal Claw', 'Endeavor'], 'ver': 'none', 'points': 7500}, {'name': 'Lileep', 'move': ['Acid', 'Mirror Coat', 'Giga Drain'], 'ver': 'none', 'points': 7500}, {'name': 'Anorith', 'move': ['Scratch', 'Stealth Rock', 'Cross Poison'], 'ver': 'none', 'points': 7500}, {'name': 'Feebas', 'move': ['Splash', 'Captivate', 'Mirror Coat'], 'ver': 'none', 'points': 7500}, {'name': 'Shellos', 'move': ['Mud-Slap', 'Yawn', 'Secret Power'], 'ver': 'BW', 'points': 7500}, {'name': 'Shellos', 'move': ['Mud-Slap', 'Yawn', 'Secret Power'], 'ver': 'BW', 'points': 7500}, {'name': 'Lapras', 'move': ['Confuse Ray', 'Horn Drill', 'Icy Wind'], 'ver': 'none', 'points': 10000}, {'name': 'Dratini', 'move': ['Thunder Wave', 'Water Pulse', 'DragonBreath'], 'ver': 'none', 'points': 10000}]
SpookyManor = [{'name': 'Gastly', 'move': ['Hypnosis', 'Disable', 'Sludge Wave'], 'ver': 'none', 'points': 'Default'}, {'name': 'Drowzee', 'move': ['Hypnosis', 'Psycho Cut', 'Drain Punch'], 'ver': 'none', 'points': 'Default'}, {'name': 'Mr. Mime', 'move': ['Barrier', 'Teeter Dance', 'Skill Swap'], 'ver': 'none', 'points': 'Default'}, {'name': 'Spinarak', 'move': ['Poison Sting', 'Electroweb', 'Bug Bite'], 'ver': 'none', 'points': 'Default'}, {'name': 'Misdreavus', 'move': ['Psywave', 'Destiny Bond', 'Inferno'], 'ver': 'none', 'points': 'Default'}, {'name': 'Wobbuffet', 'move': ['Mirror Coat', 'Charm', 'Encore'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Houndour', 'move': ['Howl', 'Feint', 'Dark Pulse'], 'ver': 'none', 'points': 'Default'}, {'name': 'Smoochum', 'move': ['Sweet Kiss', 'Captivate', 'Skill Swap'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Mawile', 'move': ['Fake Tears', 'Fire Fang', 'Ice Punch'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Meditite', 'move': ['Meditate', 'Drain Punch', 'Endure'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Spoink', 'move': ['Psywave', 'Skill Swap', 'Recycle'], 'ver': 'none', 'points': 'Default'}, {'name': 'Shuppet', 'move': ['Night Shade', 'Destiny Bond', 'Pain Split'], 'ver': 'none', 'points': 'Default'}, {'name': 'Duskull', 'move': ['Disable', 'Pain Split', 'Trick'], 'ver': 'none', 'points': 'Default'}, {'name': 'Chimecho', 'move': ['Wrap', 'Hypnosis', 'Hyper Voice'], 'ver': 'none', 'points': 'Default'}, {'name': 'Stunky', 'move': ['Screech', 'Foul Play', 'Sucker Punch'], 'ver': 'none', 'points': 'Default'}, {'name': 'Bronzor', 'move': ['Hypnosis', 'Skill Swap', 'Gravity'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Elgyem', 'move': ['Heal Block', 'Barrier', 'Nasty Plot'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Pawniard', 'move': ['Fury Cutter', 'Psycho Cut', 'Sucker Punch'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Galvantula', 'move': ['Electro Ball', 'Disable', 'Pursuit'], 'ver': 'B2W2', 'points': 5000}, {'name': 'Meowth', 'move': ['Scratch', 'Hypnosis', 'Secret Power'], 'ver': 'BW', 'points': 7500}, {'name': 'Snubbull', 'move': ['Charm', 'Close Combat', 'Double-Edge'], 'ver': 'none', 'points': 7500}, {'name': 'Smeargle', 'move': ['Sketch', 'Captivate', 'Sleep Talk'], 'ver': 'none', 'points': 7500}, {'name': 'Volbeat', 'move': ['Flash', 'Trick', 'Tailwind'], 'ver': 'none', 'points': 7500}, {'name': 'Illumise', 'move': ['Charm', 'Fake Tears', 'Tailwind'], 'ver': 'none', 'points': 7500}, {'name': 'Rotom', 'move': ['Thunder Wave', 'Shock Wave', 'Signal Beam'], 'ver': 'BW', 'points': 7500}, {'name': 'Abra', 'move': ['Teleport', 'Skill Swap', 'Gravity'], 'ver': 'none', 'points': 10000}, {'name': 'Ralts', 'move': ['Confusion', 'Destiny Bond', 'Helping Hand'], 'ver': 'BW', 'points': 10000}, {'name': 'Sableye', 'move': ['Foresight', 'Sucker Punch', 'Spite'], 'ver': 'BW', 'points': 10000}, {'name': 'Spiritomb', 'move': ['Spite', 'Pain Split', 'Icy Wind'], 'ver': 'BW', 'points': 10000}, {'name': 'Duosion', 'move': ['Recover', 'Imprison', 'Trick'], 'ver': 'B2W2', 'points': 10000}, {'name': 'Golett', 'move': ['Rollout', 'Fire Punch', 'ThunderPunch'], 'ver': 'B2W2', 'points': 10000}]
RuggedMountain = [{'name': 'Mankey', 'move': ['Low Kick', 'Reversal', 'ThunderPunch'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Machop', 'move': ['Low Kick', 'Bullet Punch', 'Helping Hand'], 'ver': 'none', 'points': 'Default'}, {'name': 'Magnemite', 'move': ['Metal Sound', 'Recycle', 'Gravity'], 'ver': 'none', 'points': 'Default'}, {'name': 'Koffing', 'move': ['Smog', 'Dark Pulse', 'Sludge Wave'], 'ver': 'none', 'points': 'Default'}, {'name': 'Rhyhorn', 'move': ['Horn Attack', 'Counter', 'Double-Edge'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Slugma', 'move': ['Ember', 'Inferno', 'Heat Wave'], 'ver': 'none', 'points': 'Default'}, {'name': 'Phanpy', 'move': ['Flail', 'Heavy Slam', 'Seed Bomb'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Larvitar', 'move': ['Bite', 'Dark Pulse', 'Stealth Rock'], 'ver': 'none', 'points': 'Default'}, {'name': 'Torkoal', 'move': ['Ember', 'Fissure', 'Stealth Rock'], 'ver': 'none', 'points': 'Default'}, {'name': 'Trapinch', 'move': ['Bite', 'Signal Beam', 'Giga Drain'], 'ver': 'none', 'points': 'Default'}, {'name': 'Cacnea', 'move': ['Absorb', 'Teeter Dance', 'ThunderPunch'], 'ver': 'none', 'points': 'Default'}, {'name': 'Burmy', 'move': ['Protect', 'Bug Bite', 'Snore'], 'ver': 'none', 'points': 'Default'}, {'name': 'Hippopotas', 'move': ['Bite', 'Stockpile', 'Superpower'], 'ver': 'none', 'points': 'Default'}, {'name': 'Skorupi', 'move': ['Bite', 'Agility', 'Aqua Tail'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Heatmor', 'move': ['Incinerate', 'Heat Wave', 'Giga Drain'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Durant', 'move': ['Fury Cutter', 'Endure', 'Thunder Fang'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Maractus', 'move': ['Pin Missile', 'Leech Seed', 'Spikes'], 'ver': 'B2W2', 'points': 5000}, {'name': 'Crustle', 'move': ['Rock Slide', 'Counter', 'Night Slash'], 'ver': 'B2W2', 'points': 5000}, {'name': 'Magby', 'move': ['Ember', 'ThunderPunch', 'Heat Wave'], 'ver': 'none', 'points': 5000}, {'name': 'Teddiursa', 'move': ['Fake Tears', 'Crunch', 'Focus Punch'], 'ver': 'BW', 'points': 7500}, {'name': 'Makuhita', 'move': ['Arm Thrust', 'Helping Hand', 'Ice Punch'], 'ver': 'BW', 'points': 7500}, {'name': 'Numel', 'move': ['Ember', 'Body Slam', 'Heat Wave'], 'ver': 'none', 'points': 7500}, {'name': 'Spinda', 'move': ['Copycat', 'Fake Out', 'Superpower'], 'ver': 'BW', 'points': 7500}, {'name': 'Absol', 'move': ['Feint', 'Megahorn', 'Superpower'], 'ver': 'none', 'points': 7500}, {'name': 'Beldum', 'move': ['Take Down', 'Zen Headbutt', 'Iron Head'], 'ver': 'BW', 'points': 7500}, {'name': 'Croagunk', 'move': ['Poison Sting', 'Drain Punch', 'Gunk Shot'], 'ver': 'none', 'points': 7500}, {'name': 'Tyrogue', 'move': ['Fake Out', 'Feint', 'Mach Punch'], 'ver': 'none', 'points': 10000}, {'name': 'Bagon', 'move': ['Bite', 'Dragon Dance', 'Outrage'], 'ver': 'none', 'points': 10000}, {'name': 'Krookodile', 'move': ['Crunch', 'Counter', 'Mean Look'], 'ver': 'B2W2', 'points': 10000}, {'name': 'Riolu', 'move': ['Endure', 'Bullet Punch', 'Focus Punch'], 'ver': 'BW', 'points': 10000}]
IcyCave = [{'name': 'Sandshrew', 'move': ['Sand-Attack', 'Counter', 'Super Fang'], 'ver': 'none', 'points': 'Default'}, {'name': 'Geodude', 'move': ['Defense Curl', 'Stealth Rock', 'Rock Climb'], 'ver': 'none', 'points': 'Default'}, {'name': 'Onix', 'move': ['Bind', 'Stealth Rock', 'Rock Climb'], 'ver': 'none', 'points': 'Default'}, {'name': 'Voltorb', 'move': ['Charge', 'Signal Beam', 'Natural Gift'], 'ver': 'none', 'points': 'Default'}, {'name': 'Cubone', 'move': ['Bone Club', 'Perish Song', 'Low Kick'], 'ver': 'none', 'points': 'Default'}, {'name': 'Cleffa', 'move': ['Encore', 'Aromatherapy', 'Sleep Talk'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Shuckle', 'move': ['Encore', 'Helping Hand', 'Shell Smash'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Whismur', 'move': ['Uproar', 'Endeavor', 'Zen Headbutt'], 'ver': 'none', 'points': 'Default'}, {'name': 'Nosepass', 'move': ['Tackle', 'Stealth Rock', 'AncientPower'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Aron', 'move': ['Harden', 'Endeavor', 'Head Smash'], 'ver': 'none', 'points': 'Default'}, {'name': 'Lunatone', 'move': ['Confusion', 'Earth Power', 'Moonlight'], 'ver': 'none', 'points': 'Default'}, {'name': 'Solrock', 'move': ['Confusion', 'Zen Headbutt', 'Morning Sun'], 'ver': 'none', 'points': 'Default'}, {'name': 'Baltoy', 'move': ['Rapid Spin', 'Gravity', 'Zen Headbutt'], 'ver': 'none', 'points': 'Default'}, {'name': 'Spheal', 'move': ['Powder Snow', 'Fissure', 'Aqua Tail'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Cranidos', 'move': ['Headbutt', 'Iron Head', 'Fire Punch'], 'ver': 'BW', 'points': 'Default'}, {'name': 'Snover', 'move': ['Razor Leaf', 'Avalanche', 'Giga Drain'], 'ver': 'none', 'points': 'Default'}, {'name': 'Drilbur', 'move': ['Rapid Spin', 'Metal Sound', 'Rock Climb'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Druddigon', 'move': ['Bite', 'Fire Fang', 'Sucker Punch'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Diglett', 'move': ['Sand-Attack', 'Beat Up', 'Stealth Rock'], 'ver': 'none', 'points': 5000}, {'name': 'Dunsparce', 'move': ['Defense Curl', 'Magic Coat', 'Stealth Rock'], 'ver': 'BW', 'points': 5000}, {'name': 'Boldore', 'move': ['Smack Down', 'Curse', 'Heavy Slam'], 'ver': 'B2W2', 'points': 5000}, {'name': 'Vanillish', 'move': ['Mirror Shot', 'Ice Shard', 'Imprison'], 'ver': 'B2W2', 'points': 5000}, {'name': 'Klang', 'move': ['Charge Beam', 'Gravity', 'Magnet Rise'], 'ver': 'B2W2', 'points': 5000}, {'name': 'Sneasel', 'move': ['Taunt', 'Ice Punch', 'Low Kick'], 'ver': 'none', 'points': 5000}, {'name': 'Snorunt', 'move': ['Powder Snow', 'Weather Ball', 'Water Pulse'], 'ver': 'none', 'points': 7500}, {'name': 'Shieldon', 'move': ['Protect', 'Counter', 'Fissure'], 'ver': 'BW', 'points': 7500}, {'name': 'Swinub', 'move': ['Odor Sleuth', 'AncientPower', 'Icicle Spear'], 'ver': 'none', 'points': 10000}, {'name': 'Gible', 'move': ['Dragon Rage', 'Outrage', 'Endure'], 'ver': 'none', 'points': 10000}, {'name': 'Axew', 'move': ['Dragon Rage', 'Counter', 'Night Slash'], 'ver': 'B2W2', 'points': 10000}]
DreamPark = [{'name': 'Paras', 'move': ['Stun Spore', 'Cross Poison', 'Synthesis'], 'ver': 'none', 'points': 'Default'}, {'name': 'Pineco', 'move': ['Selfdestruct', 'Toxic Spikes', 'Gravity'], 'ver': 'none', 'points': 'Default'}, {'name': 'Wurmple', 'move': ['Poison Sting', 'Bug Bite', 'Snore'], 'ver': 'none', 'points': 'Default'}, {'name': 'Seedot', 'move': ['Growth', 'Bullet Seed', 'Foul Play'], 'ver': 'none', 'points': 'Default'}, {'name': 'Slakoth', 'move': ['Yawn', 'Night Slash', 'Sucker Punch'], 'ver': 'none', 'points': 'Default'}, {'name': 'Nincada', 'move': ['Leech Life', 'Endure', 'Night Slash'], 'ver': 'none', 'points': 'Default'}, {'name': 'Plusle', 'move': ['Thunder Wave', 'Discharge', 'Signal Beam'], 'ver': 'none', 'points': 'Default'}, {'name': 'Minun', 'move': ['Thunder Wave', 'Discharge', 'Signal Beam'], 'ver': 'none', 'points': 'Default'}, {'name': 'Gulpin', 'move': ['Poison Gas', 'Acid Armor', 'Giga Drain'], 'ver': 'none', 'points': 'Default'}, {'name': 'Kecleon', 'move': ['Faint Attack', 'Skill Swap', 'Reflect Type'], 'ver': 'none', 'points': 'Default'}, {'name': 'Kricketot', 'move': ['Struggle Bug', 'Endeavor', 'Uproar'], 'ver': 'none', 'points': 'Default'}, {'name': 'Cherubi', 'move': ['Leech Seed', 'Heal Pulse', 'Bullet Seed'], 'ver': 'none', 'points': 'Default'}, {'name': 'Carnivine', 'move': ['Bite', 'Rage Powder', 'Gastro Acid'], 'ver': 'none', 'points': 'Default'}, {'name': 'Audino', 'move': ['Helping Hand', 'Encore', 'Yawn'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Throh', 'move': ['Bind', 'Ice Punch', 'Superpower'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Sawk', 'move': ['Rock Smash', 'ThunderPunch', 'Dual Chop'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Scraggy', 'move': ['Low Kick', 'Fake Out', 'Drain Punch'], 'ver': 'B2W2', 'points': 'Default'}, {'name': 'Venonat', 'move': ['Disable', 'Baton Pass', 'Skill Swap'], 'ver': 'BW', 'points': 1500}, {'name': 'Grimer', 'move': ['Poison Gas', 'Haze', 'Shadow Sneak'], 'ver': 'BW', 'points': 1500}, {'name': 'Combee', 'move': ['Gust', 'Tailwind', 'Air Cutter'], 'ver': 'BW', 'points': 1500}, {'name': 'Beedrill', 'move': ['Fury Attack', 'Air Cutter', 'Fury Cutter'], 'ver': 'BW', 'points': 1500}, {'name': 'Ekans', 'move': ['Poison Sting', 'Beat Up', 'Dark Pulse'], 'ver': 'none', 'points': 5000}, {'name': 'Togepi', 'move': ['Metronome', 'Lucky Chant', 'Uproar'], 'ver': 'none', 'points': 5000}, {'name': 'Aipom', 'move': ['Scratch', 'Fake Out', 'Fire Punch'], 'ver': 'none', 'points': 5000}, {'name': 'Shroomish', 'move': ['Stun Spore', 'Bullet Seed', 'Focus Punch'], 'ver': 'none', 'points': 5000}, {'name': 'Gurdurr', 'move': ['Low Kick', 'Mach Punch', 'Drain Punch'], 'ver': 'B2W2', 'points': 5000}, {'name': 'Roselia', 'move': ['Growth', 'Sleep Powder', 'Swift'], 'ver': 'none', 'points': 7500}, {'name': 'Zangoose', 'move': ['Quick Attack', 'Double Hit', 'Low Kick'], 'ver': 'BW', 'points': 7500}, {'name': 'Seviper', 'move': ['Bite', 'Body Slam', 'Aqua Tail'], 'ver': 'BW', 'points': 7500}, {'name': 'Chansey', 'move': ['Growl', 'Counter', 'Helping Hand'], 'ver': 'none', 'points': 10000}, {'name': 'Pinsir', 'move': ['ViceGrip', 'Close Combat', 'Me First'], 'ver': 'none', 'points': 10000}, {'name': 'Eevee', 'move': ['Sand-Attack', 'Charm', 'Swift'], 'ver': 'none', 'points': 10000}, {'name': 'Snorlax', 'move': ['Amnesia', 'Fire Punch', 'Recycle'], 'ver': 'none', 'points': 10000}, {'name': 'Heracross', 'move': ['Horn Attack', 'Flail', 'Focus Punch'], 'ver': 'none', 'points': 10000}]
CafeForest = [{'name': 'Poliwhirl', 'move': ['Rain Dance', 'Haze', 'Water Pulse'], 'ver': 'none', 'points': 'Default'}, {'name': 'Eevee', 'move': ['Helping Hand', 'Charm', 'Swift'], 'ver': 'none', 'points': 'Default'}, {'name': 'Smeargle', 'move': ['Sketch', 'Captivate', 'Sleep Talk'], 'ver': 'none', 'points': 'Default'}, {'name': 'Burmy', 'move': ['Protect', 'Bug Bite', 'Snore'], 'ver': 'none', 'points': 'Default'}]

locations = [PleasantForest, WindsweptSky, SparklingSea, SpookyManor, RuggedMountain, IcyCave, DreamPark, CafeForest]
# url = ''''''
# items = ''''''
# tables = pd.read_html(url)[0]
# itemstables = pd.read_html(items)


# ['Pokémon', 'Pokémon.1', 'Level', 'Availability', 'Ability',
#        'Featured moves', 'Featured moves.1', 'Featured moves.2', 'Mini-games',
#        'Mini-games.1', 'Mini-games.2', 'Mini-games.3']

# ['Item', 'Item.1', 'Availability']


# place = []
# for i in range(0, len(tables['Pokémon.1']) - 1, 3):
#     place.append({'name': tables['Pokémon.1'][i][:-2] if tables['Pokémon.1'][i][-2:] == 'BW' else
#     (tables['Pokémon.1'][i][:-4] if tables['Pokémon.1'][i][-4:] == 'B2W2' else tables['Pokémon.1'][i]),
#                     'move': [tables['Featured moves.1'][i + o] for o in range(3)],
#                     'ver': 'BW' if 'BW' in tables['Pokémon.1'][i] else
#                     'B2W2' if 'B2W2' in tables['Pokémon.1'][i] else 'none',
#                     'points': int(re.findall('\\d+', tables['Availability'][i])[0]) if 'Default' not in tables['Availability'][i]
#                     else 'Default'})
# print(place)
