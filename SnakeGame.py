import turtle
import time
import random
import math

class SnakeGame:
    def __init__(self):
        self.delay = 0.12
        self.score = 0
        self.high_score = self.load_high_score()
        self.wrap_mode = False
        self.game_running = True
        self.paused = False
        self.multiplayer = False
        self.player2_score = 0
        
        # Colors
        self.bg_color = "#1a1a2e"
        self.snake_head_color = "#4ecca3"
        self.snake_body_color = "#45b7d1"
        self.snake2_head_color = "#ff6b6b"
        self.snake2_body_color = "#ff9f43"
        self.food_color = "#ff6b6b"
        self.gold_food_color = "#feca57"
        self.text_color = "#ffffff"
        self.border_color = "#16213e"
        
        # Power-up colors
        self.speed_boost_color = "#9b59b6"
        self.shield_color = "#1dd1a1"
        self.shrink_color = "#fd79a8"
        
        # Power-up states
        self.active_powerups = {"player1": {}, "player2": {}}
        self.powerup_timers = {"player1": {}, "player2": {}}
        
        self.setup_screen()
        self.create_game_objects()
        self.create_ui_elements()
        self.setup_controls()
        
    def setup_screen(self):
        """Initialize the game screen with enhanced visuals"""
        self.wn = turtle.Screen()
        self.wn.title("🐍 SNAKE MASTER - Enhanced Edition with Power-ups & Multiplayer")
        self.wn.bgcolor(self.bg_color)
        self.wn.setup(width=1000, height=800)
        self.wn.tracer(0)
        
        # Add border
        self.draw_border()
        
    def draw_border(self):
        """Draw decorative border around game area"""
        border = turtle.Turtle()
        border.speed(0)
        border.color(self.border_color)
        border.penup()
        border.goto(-310, -310)
        border.pendown()
        border.pensize(3)
        
        # Draw border with rounded corners effect
        for _ in range(4):
            border.forward(620)
            border.circle(10, 90)
        
        border.hideturtle()
        
    def create_game_objects(self):
        """Initialize snake, food, and game segments"""
        # Player 1 Snake head
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color(self.snake_head_color)
        self.head.penup()
        self.head.goto(-50, 0)
        self.head.direction = "stop"
        
        # Player 2 Snake head
        self.head2 = turtle.Turtle()
        self.head2.speed(0)
        self.head2.shape("square")
        self.head2.color(self.snake2_head_color)
        self.head2.penup()
        self.head2.goto(50, 0)
        self.head2.direction = "stop"
        self.head2.hideturtle()  # Hidden in single player mode
        
        # Normal food
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape("circle")
        self.food.color(self.food_color)
        self.food.penup()
        self.food.goto(0, 100)
        self.food.shapesize(1.2, 1.2)
        
        # Golden special food
        self.gold_food = turtle.Turtle()
        self.gold_food.speed(0)
        self.gold_food.shape("circle")
        self.gold_food.color(self.gold_food_color)
        self.gold_food.penup()
        self.gold_food.hideturtle()
        self.gold_food.shapesize(1.5, 1.5)
        self.gold_timer = 0
        
        # Power-ups
        self.powerups = []
        self.create_powerups()
        
        self.segments = []
        self.segments2 = []
        
    def create_powerups(self):
        """Create different power-up objects"""
        # Speed Boost Power-up
        self.speed_boost = turtle.Turtle()
        self.speed_boost.speed(0)
        self.speed_boost.shape("triangle")
        self.speed_boost.color(self.speed_boost_color)
        self.speed_boost.penup()
        self.speed_boost.hideturtle()
        self.speed_boost.shapesize(1.2, 1.2)
        
        # Shield Power-up
        self.shield = turtle.Turtle()
        self.shield.speed(0)
        self.shield.shape("square")
        self.shield.color(self.shield_color)
        self.shield.penup()
        self.shield.hideturtle()
        self.shield.shapesize(1.2, 1.2)
        
        # Shrink Power-up
        self.shrink = turtle.Turtle()
        self.shrink.speed(0)
        self.shrink.shape("circle")
        self.shrink.color(self.shrink_color)
        self.shrink.penup()
        self.shrink.hideturtle()
        self.shrink.shapesize(0.8, 0.8)
        
        self.powerups = [
            {"obj": self.speed_boost, "type": "speed_boost", "timer": 0},
            {"obj": self.shield, "type": "shield", "timer": 0},
            {"obj": self.shrink, "type": "shrink", "timer": 0}
        ]
        
    def create_ui_elements(self):
        """Create enhanced UI elements"""
        # Main scoreboard
        self.score_pen = turtle.Turtle()
        self.score_pen.speed(0)
        self.score_pen.color(self.text_color)
        self.score_pen.penup()
        self.score_pen.hideturtle()
        self.score_pen.goto(0, 320)
        
        # Instructions panel
        self.info_pen = turtle.Turtle()
        self.info_pen.speed(0)
        self.info_pen.color("#a0a0a0")
        self.info_pen.penup()
        self.info_pen.hideturtle()
        self.info_pen.goto(0, -340)
        
        # Game status indicator
        self.status_pen = turtle.Turtle()
        self.status_pen.speed(0)
        self.status_pen.color("#4ecca3")
        self.status_pen.penup()
        self.status_pen.hideturtle()
        self.status_pen.goto(-420, 300)
        
        # Power-up status display
        self.powerup_pen = turtle.Turtle()
        self.powerup_pen.speed(0)
        self.powerup_pen.color("#e17055")
        self.powerup_pen.penup()
        self.powerup_pen.hideturtle()
        self.powerup_pen.goto(-420, 250)
        
        self.update_display()
        
    def update_display(self):
        """Update all display elements"""
        # Clear and update score
        self.score_pen.clear()
        if self.multiplayer:
            self.score_pen.write(f"P1: {self.score:04d} • P2: {self.player2_score:04d} • HIGH: {self.high_score:04d}", 
                                align="center", font=("Arial", 16, "bold"))
        else:
            self.score_pen.write(f"SCORE: {self.score:04d} • HIGH SCORE: {self.high_score:04d}", 
                                align="center", font=("Arial", 18, "bold"))
        
        # Update instructions
        self.info_pen.clear()
        if self.multiplayer:
            self.info_pen.write("P1: WASD • P2: Arrow Keys • SPACE: pause • R: restart • M: toggle multiplayer", 
                               align="center", font=("Arial", 10, "normal"))
        else:
            self.info_pen.write("WASD to move • SPACE: pause • R: restart • M: multiplayer mode", 
                               align="center", font=("Arial", 12, "normal"))
        
        # Update status
        self.status_pen.clear()
        if self.paused:
            self.status_pen.write("⏸ PAUSED", align="center", font=("Arial", 14, "bold"))
        elif self.game_running:
            length = len(self.segments) + 1
            speed = int((0.12 - self.delay) * 1000)
            mode = "MULTIPLAYER" if self.multiplayer else "SINGLE PLAYER"
            self.status_pen.write(f"{mode}\nLENGTH: {length}\nSPEED: {speed}", 
                                 align="center", font=("Arial", 10, "normal"))
        
        # Update power-up status
        self.powerup_pen.clear()
        active_text = "ACTIVE POWER-UPS:\n"
        p1_powers = []
        p2_powers = []
        
        for power, timer in self.powerup_timers["player1"].items():
            if timer > 0:
                p1_powers.append(f"P1-{power.upper()}: {timer//10}s")
                
        for power, timer in self.powerup_timers["player2"].items():
            if timer > 0:
                p2_powers.append(f"P2-{power.upper()}: {timer//10}s")
        
        all_powers = p1_powers + p2_powers
        if all_powers:
            active_text += "\n".join(all_powers)
            self.powerup_pen.write(active_text, align="center", font=("Arial", 9, "normal"))
            
    def setup_controls(self):
        """Setup keyboard controls"""
        self.wn.listen()
        # Player 1 controls
        self.wn.onkeypress(self.go_up, "w")
        self.wn.onkeypress(self.go_down, "s")
        self.wn.onkeypress(self.go_left, "a")
        self.wn.onkeypress(self.go_right, "d")
        
        # Player 2 controls
        self.wn.onkeypress(self.go_up2, "Up")
        self.wn.onkeypress(self.go_down2, "Down")
        self.wn.onkeypress(self.go_left2, "Left")
        self.wn.onkeypress(self.go_right2, "Right")
        
        # Game controls
        self.wn.onkeypress(self.toggle_pause, "space")
        self.wn.onkeypress(self.restart_game, "r")
        self.wn.onkeypress(self.toggle_multiplayer, "m")
        
    # Player 1 movement
    def go_up(self):
        if self.head.direction != "down":
            self.head.direction = "up"
    def go_down(self):
        if self.head.direction != "up":
            self.head.direction = "down"
    def go_left(self):
        if self.head.direction != "right":
            self.head.direction = "left"
    def go_right(self):
        if self.head.direction != "left":
            self.head.direction = "right"
    
    # Player 2 movement
    def go_up2(self):
        if self.multiplayer and self.head2.direction != "down":
            self.head2.direction = "up"
    def go_down2(self):
        if self.multiplayer and self.head2.direction != "up":
            self.head2.direction = "down"
    def go_left2(self):
        if self.multiplayer and self.head2.direction != "right":
            self.head2.direction = "left"
    def go_right2(self):
        if self.multiplayer and self.head2.direction != "left":
            self.head2.direction = "right"
            
    def toggle_pause(self):
        self.paused = not self.paused
        self.update_display()
        
    def toggle_multiplayer(self):
        """Toggle between single and multiplayer modes"""
        self.multiplayer = not self.multiplayer
        if self.multiplayer:
            self.head2.showturtle()
            self.head.goto(-50, 0)
            self.head2.goto(50, 0)
            self.player2_score = 0
        else:
            self.head2.hideturtle()
            self.head.goto(0, 0)
            # Clear player 2 segments
            for segment in self.segments2:
                segment.goto(1000, 1000)
            self.segments2.clear()
        self.restart_game()
        
    def restart_game(self):
        """Restart the game"""
        start_pos = (0, 0) if not self.multiplayer else (-50, 0)
        self.head.goto(start_pos[0], start_pos[1])
        self.head.direction = "stop"
        self.head.color(self.snake_head_color)
        
        if self.multiplayer:
            self.head2.goto(50, 0)
            self.head2.direction = "stop"
            self.head2.color(self.snake2_head_color)
            self.player2_score = 0
            for segment in self.segments2:
                segment.goto(1000, 1000)
            self.segments2.clear()
        
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        
        self.score = 0
        self.delay = 0.12
        self.paused = False
        self.gold_food.hideturtle()
        
        # Reset power-ups
        for powerup in self.powerups:
            powerup["obj"].hideturtle()
            powerup["timer"] = 0
        self.active_powerups = {"player1": {}, "player2": {}}
        self.powerup_timers = {"player1": {}, "player2": {}}
        
        self.update_display()
        
    def move(self):
        """Move snake heads"""
        # Move player 1
        if self.head.direction == "up":
            self.head.sety(self.head.ycor() + 20)
        elif self.head.direction == "down":
            self.head.sety(self.head.ycor() - 20)
        elif self.head.direction == "left":
            self.head.setx(self.head.xcor() - 20)
        elif self.head.direction == "right":
            self.head.setx(self.head.xcor() + 20)
            
        # Move player 2
        if self.multiplayer:
            if self.head2.direction == "up":
                self.head2.sety(self.head2.ycor() + 20)
            elif self.head2.direction == "down":
                self.head2.sety(self.head2.ycor() - 20)
            elif self.head2.direction == "left":
                self.head2.setx(self.head2.xcor() - 20)
            elif self.head2.direction == "right":
                self.head2.setx(self.head2.xcor() + 20)
            
    def spawn_food(self):
        """Spawn food at random location"""
        while True:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            x = (x // 20) * 20
            y = (y // 20) * 20
            
            # Check if position conflicts with snakes
            if self.is_position_clear(x, y):
                self.food.goto(x, y)
                break
                
    def is_position_clear(self, x, y):
        """Check if a position is clear of snakes and other objects"""
        if (x, y) == (self.head.xcor(), self.head.ycor()):
            return False
        if self.multiplayer and (x, y) == (self.head2.xcor(), self.head2.ycor()):
            return False
        
        for segment in self.segments + self.segments2:
            if (x, y) == (segment.xcor(), segment.ycor()):
                return False
        return True
                
    def create_segment(self, player=1):
        """Create a new snake segment"""
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        
        if player == 1:
            segments_list = self.segments
            base_color = self.snake_body_color
            shade_colors = ["#45b7d1", "#3da0c7", "#358abd", "#2d73b3", "#255ca9"]
        else:
            segments_list = self.segments2
            base_color = self.snake2_body_color
            shade_colors = ["#ff9f43", "#ff8c42", "#ff7675", "#fd79a8", "#e84393"]
        
        new_segment.color(base_color)
        new_segment.penup()
        
        # Create gradient effect
        if len(segments_list) > 0:
            color_index = min(len(segments_list) % len(shade_colors), len(shade_colors) - 1)
            new_segment.color(shade_colors[color_index])
            
        segments_list.append(new_segment)
        
    def spawn_powerup(self):
        """Randomly spawn a power-up"""
        if random.randint(1, 15) == 1:  # 1 in 15 chance
            available_powerups = [p for p in self.powerups if not p["obj"].isvisible()]
            if available_powerups:
                powerup = random.choice(available_powerups)
                
                # Find clear position
                attempts = 0
                while attempts < 20:
                    x = random.randint(-280, 280)
                    y = random.randint(-280, 280)
                    x = (x // 20) * 20
                    y = (y // 20) * 20
                    
                    if self.is_position_clear(x, y) and (x, y) != (self.food.xcor(), self.food.ycor()):
                        powerup["obj"].goto(x, y)
                        powerup["obj"].showturtle()
                        powerup["timer"] = 100  # 10 seconds at 10 FPS
                        break
                    attempts += 1
                    
    def apply_powerup(self, powerup_type, player):
        """Apply power-up effect to player"""
        player_key = f"player{player}"
        
        if powerup_type == "speed_boost":
            self.active_powerups[player_key]["speed_boost"] = True
            self.powerup_timers[player_key]["speed_boost"] = 50  # 5 seconds
            if player == 1:
                self.delay = max(0.03, self.delay * 0.5)
                
        elif powerup_type == "shield":
            self.active_powerups[player_key]["shield"] = True
            self.powerup_timers[player_key]["shield"] = 100  # 10 seconds
            # Visual indicator - make head slightly larger
            head = self.head if player == 1 else self.head2
            head.shapesize(1.3, 1.3)
            
        elif powerup_type == "shrink":
            # Shrink the snake by removing segments
            segments = self.segments if player == 1 else self.segments2
            if len(segments) > 2:
                for _ in range(min(3, len(segments) - 1)):
                    segment = segments.pop()
                    segment.goto(1000, 1000)
                    
    def update_powerups(self):
        """Update power-up timers and effects"""
        # Update powerup spawn timers
        for powerup in self.powerups:
            if powerup["obj"].isvisible():
                powerup["timer"] -= 1
                if powerup["timer"] <= 0:
                    powerup["obj"].hideturtle()
                    
        # Update active powerup timers
        for player in ["player1", "player2"]:
            for power_type in list(self.powerup_timers[player].keys()):
                if self.powerup_timers[player][power_type] > 0:
                    self.powerup_timers[player][power_type] -= 1
                    
                    # Remove expired powerups
                    if self.powerup_timers[player][power_type] <= 0:
                        if power_type == "speed_boost" and player == "player1":
                            self.delay = min(0.12, self.delay * 2)
                        elif power_type == "shield":
                            head = self.head if player == "player1" else self.head2
                            head.shapesize(1.0, 1.0)
                        
                        del self.active_powerups[player][power_type]
                        del self.powerup_timers[player][power_type]
                        
    def check_collisions(self):
        """Check for all types of collisions"""
        # Check border collisions
        for player, head in [(1, self.head), (2, self.head2)]:
            if player == 2 and not self.multiplayer:
                continue
                
            if not self.wrap_mode:
                if (head.xcor() > 290 or head.xcor() < -290 or 
                    head.ycor() > 290 or head.ycor() < -290):
                    # Check for shield protection
                    player_key = f"player{player}"
                    if "shield" not in self.active_powerups[player_key]:
                        if self.multiplayer and player == 2:
                            self.player2_loses()
                        else:
                            self.game_over()
                        return
                    else:
                        # Bounce back with shield
                        if head.xcor() > 290: head.setx(270)
                        elif head.xcor() < -290: head.setx(-270)
                        elif head.ycor() > 290: head.sety(270)
                        elif head.ycor() < -290: head.sety(-270)
                        
        # Food collisions
        if self.head.distance(self.food) < 20:
            self.spawn_food()
            self.create_segment(1)
            self.score += 10
            if self.score > self.high_score:
                self.high_score = self.score
            self.delay = max(0.05, self.delay - 0.001)
            if random.randint(1, 8) == 1 and not self.gold_food.isvisible():
                self.spawn_golden_food()
            self.spawn_powerup()
            self.update_display()
            
        if self.multiplayer and self.head2.distance(self.food) < 20:
            self.spawn_food()
            self.create_segment(2)
            self.player2_score += 10
            self.spawn_powerup()
            self.update_display()
            
        # Power-up collisions
        for powerup in self.powerups:
            if powerup["obj"].isvisible():
                if self.head.distance(powerup["obj"]) < 20:
                    self.apply_powerup(powerup["type"], 1)
                    powerup["obj"].hideturtle()
                    self.update_display()
                elif self.multiplayer and self.head2.distance(powerup["obj"]) < 20:
                    self.apply_powerup(powerup["type"], 2)
                    powerup["obj"].hideturtle()
                    self.update_display()
                    
        # Golden food collision
        if self.gold_food.isvisible():
            if self.head.distance(self.gold_food) < 20:
                self.gold_food.hideturtle()
                self.score += 50
                if self.score > self.high_score:
                    self.high_score = self.score
                self.delay = max(0.05, self.delay - 0.005)
                self.update_display()
            elif self.multiplayer and self.head2.distance(self.gold_food) < 20:
                self.gold_food.hideturtle()
                self.player2_score += 50
                self.update_display()
                
        # Self and cross collision
        # Player 1 collisions
        for segment in self.segments:
            if segment.distance(self.head) < 20:
                if "shield" not in self.active_powerups["player1"]:
                    self.game_over()
                    return
                    
        # Player 2 collisions (in multiplayer)
        if self.multiplayer:
            for segment in self.segments2:
                if segment.distance(self.head2) < 20:
                    if "shield" not in self.active_powerups["player2"]:
                        self.player2_loses()
                        return
                        
            # Cross collisions
            if self.head.distance(self.head2) < 20:
                self.game_over()  # Both lose if heads collide
                return
                
            # Player 1 hits Player 2's body
            for segment in self.segments2:
                if self.head.distance(segment) < 20:
                    if "shield" not in self.active_powerups["player1"]:
                        self.game_over()
                        return
                        
            # Player 2 hits Player 1's body
            for segment in self.segments:
                if self.head2.distance(segment) < 20:
                    if "shield" not in self.active_powerups["player2"]:
                        self.player2_loses()
                        return
                        
    def spawn_golden_food(self):
        """Spawn golden special food"""
        attempts = 0
        while attempts < 20:
            gx = random.randint(-280, 280)
            gy = random.randint(-280, 280)
            gx = (gx // 20) * 20
            gy = (gy // 20) * 20
            
            if self.is_position_clear(gx, gy) and (gx, gy) != (self.food.xcor(), self.food.ycor()):
                self.gold_food.goto(gx, gy)
                self.gold_food.showturtle()
                self.gold_timer = 80
                break
            attempts += 1
                    
    def player2_loses(self):
        """Handle Player 2 losing in multiplayer"""
        self.head2.color("#ff4757")
        time.sleep(0.5)
        
        # Show winner message
        winner_pen = turtle.Turtle()
        winner_pen.speed(0)
        winner_pen.color("#4ecca3")
        winner_pen.penup()
        winner_pen.hideturtle()
        winner_pen.goto(0, 0)
        winner_pen.write("PLAYER 1 WINS!", align="center", font=("Arial", 32, "bold"))
        
        time.sleep(2)
        winner_pen.clear()
        self.restart_game()
        
    def game_over(self):
        """Handle game over"""
        self.save_high_score()
        
        # Game over animation
        self.head.color("#ff4757")
        if self.multiplayer:
            self.head2.color("#ff4757")
        time.sleep(0.5)
        
        # Show game over message
        game_over_pen = turtle.Turtle()
        game_over_pen.speed(0)
        game_over_pen.color("#ff4757")
        game_over_pen.penup()
        game_over_pen.hideturtle()
        game_over_pen.goto(0, 0)
        
        if self.multiplayer:
            game_over_pen.write("GAME OVER - TIE!", align="center", font=("Arial", 32, "bold"))
        else:
            game_over_pen.write("GAME OVER", align="center", font=("Arial", 32, "bold"))
        
        restart_pen = turtle.Turtle()
        restart_pen.speed(0)
        restart_pen.color("#ffffff")
        restart_pen.penup()
        restart_pen.hideturtle()
        restart_pen.goto(0, -50)
        restart_pen.write("Press 'R' to restart", align="center", font=("Arial", 16, "normal"))
        
        time.sleep(2)
        game_over_pen.clear()
        restart_pen.clear()
        
        self.restart_game()
        
    def load_high_score(self):
        """Load high score from file"""
        try:
            with open("snake_high_score.txt", "r") as file:
                return int(file.read())
        except:
            return 0
            
    def save_high_score(self):
        """Save high score to file"""
        try:
            with open("snake_high_score.txt", "w") as file:
                file.write(str(self.high_score))
        except:
            pass
            
    def run(self):
        """Main game loop"""
        while True:
            self.wn.update()
            
            if not self.paused and self.game_running:
                # Update power-ups
                self.update_powerups()
                
                # Golden food timer
                if self.gold_food.isvisible():
                    self.gold_timer -= 1
                    if self.gold_timer <= 0:
                        self.gold_food.hideturtle()
                        
                # Move segments for player 1
                for index in range(len(self.segments) - 1, 0, -1):
                    x = self.segments[index - 1].xcor()
                    y = self.segments[index - 1].ycor()
                    self.segments[index].goto(x, y)
                    
                if len(self.segments) > 0:
                    self.segments[0].goto(self.head.xcor(), self.head.ycor())
                
                # Move segments for player 2
                if self.multiplayer:
                    for index in range(len(self.segments2) - 1, 0, -1):
                        x = self.segments2[index - 1].xcor()
                        y = self.segments2[index - 1].ycor()
                        self.segments2[index].goto(x, y)
                        
                    if len(self.segments2) > 0:
                        self.segments2[0].goto(self.head2.xcor(), self.head2.ycor())
                    
                self.move()
                self.check_collisions()
                
            time.sleep(self.delay)

# Run the game
if __name__ == "__main__":
    game = SnakeGame()
    game.run()