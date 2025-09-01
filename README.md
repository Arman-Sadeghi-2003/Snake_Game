# 🐍 Snake Master - Enhanced Edition

A modern, feature-rich implementation of the classic Snake game built with Python and Turtle graphics. Experience smooth gameplay, beautiful visuals, and enhanced features that bring this timeless game to life!

![Snake Game Demo](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## ✨ Features

### 🎮 **Enhanced Gameplay**
- **Smooth Controls**: WASD movement with responsive input
- **Progressive Difficulty**: Speed increases as you grow longer
- **Smart Collision**: Precise collision detection system
- **Pause Function**: Take a break anytime with SPACE
- **Instant Restart**: Press R to start fresh immediately

### 🎨 **Beautiful UI Design**
- **Modern Color Scheme**: Eye-friendly dark theme with vibrant accents
- **Gradient Snake Body**: Different shades create visual depth
- **Professional Border**: Sleek rounded border design
- **Real-time Stats**: Live display of score, length, and speed
- **Visual Feedback**: Smooth animations and color transitions

### 🏆 **Special Features**
- **Golden Food**: Rare special food worth 50 points
- **High Score Persistence**: Your best scores are saved automatically
- **Game Over Animation**: Satisfying visual feedback
- **Smart Food Spawning**: Food never spawns inside the snake
- **Wrap Mode**: Optional wall wrap-around (configurable)

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

### Controls
| Key | Action |
|-----|--------|
| `W` | Move Up |
| `S` | Move Down |
| `A` | Move Left |
| `D` | Move Right |
| `SPACE` | Pause/Resume |
| `R` | Restart Game |

### Objective
- **Eat the red food** to grow your snake and increase your score (+10 points)
- **Catch golden food** when it appears for bonus points (+50 points)
- **Avoid hitting** walls and your own tail
- **Beat your high score** and become the Snake Master!

### Pro Tips 💡
- Golden food appears randomly and disappears after a few seconds
- The game speeds up as your snake grows longer
- Plan your moves ahead to avoid getting trapped
- Use the pause feature to strategize your next move

## 🛠️ Customization

Want to modify the game? Here are some easy tweaks you can make:

### Change Colors
```python
# In the __init__ method, modify these values:
self.bg_color = "#1a1a2e"          # Background color
self.snake_head_color = "#4ecca3"   # Snake head color
self.food_color = "#ff6b6b"         # Regular food color
```

### Adjust Difficulty
```python
# Modify these values for different difficulty:
self.delay = 0.12        # Starting speed (lower = faster)
self.wrap_mode = False   # Set to True for wrap-around walls
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
├── snake_game.py          # Main game file
├── snake_high_score.txt   # High score storage (auto-generated)
├── README.md             # You are here!
└── LICENSE               # No License
```

## 🤝 Contributing

We love contributions! Here's how you can help make Snake Master even better:

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Ideas for Contributions
- 🎵 Add sound effects
- 🏅 Implement achievement system
- 🌈 More color themes
- 🎯 Power-ups and obstacles
- 📱 Mobile-friendly controls
- 🕹️ Multiple game modes

## 🐛 Bug Reports

Found a bug? We want to hear about it! Please open an issue with:
- Description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS

## 🙏 Acknowledgments

- Inspired by the classic Snake game from Nokia phones
- Built with Python's Turtle graphics library
- Thanks to the open-source community for continuous inspiration

## 📊 Stats

- **Lines of Code**: ~250
- **Features**: 10+
- **Supported Python Versions**: 3.7+
- **Dependencies**: 0 (uses only standard library)

## 🌟 Show Your Support

If you enjoyed this game, please consider:
- ⭐ **Starring** this repository
- 🍴 **Forking** for your own modifications
- 📢 **Sharing** with friends who love retro games
- 🐛 **Reporting** any issues you find

---

<div align="center">

**Made with ❤️ and Python**

[Report Bug](https://github.com/Arman-Sadeghi-2003/Snake_Game/issues) • [Request Feature](https://github.com/Arman-Sadeghi-2003/Snake_Game/issues) • [Contribute](https://github.com/Arman-Sadeghi-2003/Snake_Game/pulls)

</div>

---

### 🎮 Ready to become the Snake Master? Run the game and start your journey!

```bash
python snake_game.py
```

*Happy Gaming! 🐍✨*
