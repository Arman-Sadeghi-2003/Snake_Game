# 🐍 Snake Master - Enhanced Edition with Power-ups & Multiplayer

A modern, feature-rich implementation of the classic Snake game built with Python and Turtle graphics. Experience smooth gameplay, beautiful visuals, power-ups, multiplayer battles, and enhanced features that bring this timeless game to life!

![Snake Game Demo](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)
![Players](https://img.shields.io/badge/Players-1--2-orange.svg)

## ✨ Features

### 🎮 **Enhanced Gameplay**
- **Smooth Controls**: WASD movement with responsive input
- **Progressive Difficulty**: Speed increases as you grow longer
- **Smart Collision**: Precise collision detection system
- **Pause Function**: Take a break anytime with SPACE
- **Instant Restart**: Press R to start fresh immediately
- **🆕 Multiplayer Mode**: Challenge your friends in head-to-head battles!
- **🆕 Power-up System**: Collect special items for strategic advantages

### 🎨 **Beautiful UI Design**
- **Modern Color Scheme**: Eye-friendly dark theme with vibrant accents
- **Gradient Snake Body**: Different shades create visual depth
- **Professional Border**: Sleek rounded border design
- **Real-time Stats**: Live display of score, length, speed, and active power-ups
- **Visual Feedback**: Smooth animations and color transitions
- **Dynamic Status Display**: Shows current game mode and player information

### 🏆 **Special Features**
- **Golden Food**: Rare special food worth 50 points
- **High Score Persistence**: Your best scores are saved automatically
- **Game Over Animation**: Satisfying visual feedback
- **Smart Food Spawning**: Food never spawns inside snakes
- **Wrap Mode**: Optional wall wrap-around (configurable)

### ⚡ **NEW: Power-up System**
- **🚀 Speed Boost** (Purple Triangle): Doubles your speed for 5 seconds
- **🛡️ Shield** (Green Square): Protects from collisions for 10 seconds
  - Bounce off walls instead of dying
  - Immunity to self-collision and opponent attacks
  - Visual indicator with enlarged head
- **📉 Shrink** (Pink Circle): Removes up to 3 segments from your snake
- **Smart Spawning**: Power-ups appear randomly with clear visual timers
- **Strategic Gameplay**: Risk vs reward mechanics

### 👥 **NEW: Multiplayer Mode**
- **Competitive Battles**: Two players on the same screen
- **Unique Controls**: Player 1 (WASD) vs Player 2 (Arrow Keys)
- **Cross-Collision**: Players can eliminate each other
- **Separate Scoring**: Individual score tracking
- **Win Conditions**: First to die loses, or mutual elimination
- **Dynamic UI**: Shows both players' stats and power-up status

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Turtle graphics (included with Python)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Arman-Sadeghi-2003/Snake_Game.git
   cd Snake_Game
   ```

2. **Run the game**
   ```bash
   python snake_game.py
   ```

That's it! No additional dependencies required. 🎉

## 🕹️ How to Play

### Single Player Controls
| Key | Action |
|-----|--------|
| `W` | Move Up |
| `S` | Move Down |
| `A` | Move Left |
| `D` | Move Right |
| `SPACE` | Pause/Resume |
| `R` | Restart Game |
| `M` | Toggle Multiplayer Mode |

### Multiplayer Controls
| Player | Up | Down | Left | Right |
|--------|-----|------|------|-------|
| **Player 1** (Green) | `W` | `S` | `A` | `D` |
| **Player 2** (Red) | `↑` | `↓` | `←` | `→` |

### Objective
- **Eat the red food** to grow your snake and increase your score (+10 points)
- **Catch golden food** when it appears for bonus points (+50 points)
- **🆕 Collect power-ups** for strategic advantages
- **🆕 In multiplayer**: Outlast your opponent while growing your snake
- **Avoid hitting** walls, your own tail, and your opponent
- **Beat your high score** and become the Snake Master!

### Power-up Guide 💡

#### 🚀 Speed Boost (Purple Triangle)
- **Effect**: Doubles movement speed
- **Duration**: 5 seconds
- **Strategy**: Great for quick escapes or aggressive plays

#### 🛡️ Shield (Green Square)
- **Effect**: Complete collision immunity
- **Duration**: 10 seconds
- **Strategy**: Take risks, go through opponents, bounce off walls

#### 📉 Shrink (Pink Circle)
- **Effect**: Removes up to 3 body segments
- **Strategy**: Use when trapped or to increase maneuverability

### Pro Tips 💡
- Golden food appears randomly and disappears after a few seconds
- The game speeds up as your snake grows longer
- Plan your moves ahead to avoid getting trapped
- Use the pause feature to strategize your next move
- **🆕 Power-ups spawn every ~15 moves** - position yourself strategically
- **🆕 In multiplayer**: Use power-ups defensively and offensively
- **🆕 Shield timing**: Save shields for dangerous situations
- **🆕 Speed boost**: Combine with shrink for maximum agility

## 🎮 Game Modes

### 🐍 Single Player Mode
- Classic snake experience with power-ups
- Progressive difficulty scaling
- High score tracking
- Perfect for skill building

### ⚔️ Multiplayer Mode
- Head-to-head competitive battles
- Shared power-ups create strategic decisions
- Cross-collision mechanics
- Winner-takes-all gameplay

## 🛠️ Customization

Want to modify the game? Here are some easy tweaks you can make:

### Change Colors
```python
# In the __init__ method, modify these values:
self.bg_color = "#1a1a2e"          # Background color
self.snake_head_color = "#4ecca3"   # Player 1 snake head
self.snake2_head_color = "#ff6b6b"  # Player 2 snake head
self.food_color = "#ff6b6b"         # Regular food color
```

### Adjust Difficulty
```python
# Modify these values for different difficulty:
self.delay = 0.12        # Starting speed (lower = faster)
self.wrap_mode = False   # Set to True for wrap-around walls
```

### Power-up Settings
```python
# In spawn_powerup method:
if random.randint(1, 15) == 1:  # Power-up spawn chance (1 in 15)

# In apply_powerup method, adjust durations:
self.powerup_timers[player_key]["speed_boost"] = 50  # 5 seconds
self.powerup_timers[player_key]["shield"] = 100      # 10 seconds
```

### Golden Food Rarity
```python
# In check_collisions method, change the spawn chance:
if random.randint(1, 8) == 1:  # 1 in 8 chance (12.5%)
```

## 📁 Project Structure

```
Snake_Game/
│
├── snake_game.py          # Main game file with all features
├── snake_high_score.txt   # High score storage (auto-generated)
├── README.md             # You are here!
└── LICENSE               # No License
```

## 🎯 Feature Highlights

### Power-up System Architecture
- **Modular Design**: Easy to add new power-ups
- **Timer Management**: Precise duration control
- **Visual Feedback**: Clear status indicators
- **Balanced Gameplay**: Carefully tuned spawn rates and effects

### Multiplayer Implementation
- **Dual Snake Logic**: Independent movement and collision systems
- **Shared Environment**: Common food and power-up spawning
- **Cross-Interaction**: Players can affect each other's gameplay
- **Fair Competition**: Equal access to all game elements

## 🤝 Contributing

We love contributions! Here's how you can help make Snake Master even better:

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Ideas for Contributions
- 🎵 Add sound effects and background music
- 🏅 Implement achievement and trophy system
- 🌈 More color themes and visual effects
- 🎯 Additional power-ups (freeze, teleport, ghost mode)
- 📱 Mobile-friendly touch controls
- 🕹️ Tournament mode and AI opponents
- 🌐 Online multiplayer capabilities
- 📊 Detailed statistics and analytics
- 🎨 Particle effects and enhanced animations

## 🐛 Bug Reports

Found a bug? We want to hear about it! Please open an issue with:
- Description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Game mode (single/multiplayer)
- Active power-ups when bug occurred

## 🙏 Acknowledgments

- Inspired by the classic Snake game from Nokia phones
- Built with Python's Turtle graphics library
- Power-up system inspired by modern arcade games
- Multiplayer mechanics inspired by competitive gaming
- Thanks to the open-source community for continuous inspiration

## 📊 Stats

- **Lines of Code**: ~500+
- **Features**: 15+
- **Game Modes**: 2 (Single Player, Multiplayer)
- **Power-ups**: 3 (Speed Boost, Shield, Shrink)
- **Supported Python Versions**: 3.7+
- **Dependencies**: 0 (uses only standard library)
- **Max Players**: 2 simultaneous

## 🏆 Achievements to Unlock

Try to accomplish these challenges:

### Single Player Challenges
- 🥉 **Beginner**: Reach 100 points
- 🥈 **Intermediate**: Reach 500 points  
- 🥇 **Expert**: Reach 1000 points
- 💎 **Master**: Use all power-ups in a single game
- 🌟 **Speed Demon**: Win using only speed boost power-ups

### Multiplayer Challenges
- ⚔️ **First Blood**: Win your first multiplayer match
- 🛡️ **Shield Master**: Win a match using only shield power-ups
- 📉 **Size Matters**: Win with the shortest snake possible
- 🏆 **Champion**: Win 5 consecutive multiplayer matches
- 🎯 **Power Player**: Collect 10 power-ups in a single multiplayer game

## 🌟 Show Your Support

If you enjoyed this game, please consider:
- ⭐ **Starring** this repository
- 🍴 **Forking** for your own modifications
- 📢 **Sharing** with friends who love retro and multiplayer games
- 🐛 **Reporting** any issues you find
- 💡 **Suggesting** new features and power-ups

---

<div align="center">

**Made with ❤️, Python, and lots of gameplay testing**

[Report Bug](https://github.com/Arman-Sadeghi-2003/Snake_Game/issues) • [Request Feature](https://github.com/Arman-Sadeghi-2003/Snake_Game/issues) • [Contribute](https://github.com/Arman-Sadeghi-2003/Snake_Game/pulls)

</div>

---

### 🎮 Ready to become the Snake Master? Challenge your friends and dominate the arena!

**Single Player Mode:**
```bash
python snake_game.py
# Press 'M' in-game to switch to multiplayer
```

**Multiplayer Quick Start:**
```bash
python snake_game.py
# Press 'M' to enable multiplayer mode
# Player 1: WASD, Player 2: Arrow Keys
```

*Happy Gaming! 🐍✨🎯⚔️*

---

## 📈 Version History

### v2.0.0 - Enhanced Edition
- ✨ Added Power-up System (Speed Boost, Shield, Shrink)
- 👥 Added Multiplayer Mode with competitive gameplay
- 🎨 Enhanced UI with power-up status displays
- ⚡ Improved collision detection for multiplayer
- 🛡️ Added shield mechanics with visual feedback
- 📊 Dynamic status display for both game modes

### v1.0.0 - Original Release
- 🐍 Core snake gameplay
- 🍎 Food and golden food system
- 💾 High score persistence
- 🎨 Modern UI design
