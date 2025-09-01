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
        
        # Colors
        self.bg_color = "#1a1a2e"
        self.snake_head_color = "#4ecca3"
        self.snake_body_color = "#45b7d1"
        self.food_color = "#ff6b6b"
        self.gold_food_color = "#feca57"
        self.text_color = "#ffffff"
        self.border_color = "#16213e"
        
        self.setup_screen()
        self.create_game_objects()
        self.create_ui_elements()
        self.setup_controls()
        
    def setup_screen(self):
        """Initialize the game screen with enhanced visuals"""
        self.wn = turtle.Screen()
        self.wn.title("🐍 SNAKE MASTER - Enhanced Edition")
        self.wn.bgcolor(self.bg_color)
        self.wn.setup(width=800, height=700)
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
        # Snake head with enhanced design
        self.head = turtle.Turtle()
        self.head.speed(0)
        self.head.shape("square")
        self.head.color(self.snake_head_color)
        self.head.penup()
        self.head.goto(0, 0)
        self.head.direction = "stop"
        
        # Normal food with glow effect
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
        
        self.segments = []
        
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
        self.info_pen.write("WASD to move • SPACE to pause • R to restart", 
                           align="center", font=("Arial", 12, "normal"))
        
        # Game status indicator
        self.status_pen = turtle.Turtle()
        self.status_pen.speed(0)
        self.status_pen.color("#4ecca3")
        self.status_pen.penup()
        self.status_pen.hideturtle()
        self.status_pen.goto(-380, 300)
        
        self.update_display()
        
    def update_display(self):
        """Update all display elements"""
        # Clear and update score
        self.score_pen.clear()
        self.score_pen.write(f"SCORE: {self.score:04d} • HIGH SCORE: {self.high_score:04d}", 
                            align="center", font=("Arial", 18, "bold"))
        
        # Update status
        self.status_pen.clear()
        if self.paused:
            self.status_pen.write("⏸ PAUSED", align="center", font=("Arial", 14, "bold"))
        elif self.game_running:
            length = len(self.segments) + 1
            speed = int((0.12 - self.delay) * 1000)
            self.status_pen.write(f"LENGTH: {length} • SPEED: {speed}", 
                                 align="center", font=("Arial", 12, "normal"))
            
    def setup_controls(self):
        """Setup keyboard controls"""
        self.wn.listen()
        self.wn.onkeypress(self.go_up, "w")
        self.wn.onkeypress(self.go_down, "s")
        self.wn.onkeypress(self.go_left, "a")
        self.wn.onkeypress(self.go_right, "d")
        self.wn.onkeypress(self.toggle_pause, "space")
        self.wn.onkeypress(self.restart_game, "r")
        
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
            
    def toggle_pause(self):
        self.paused = not self.paused
        self.update_display()
        
    def restart_game(self):
        """Restart the game"""
        self.head.goto(0, 0)
        self.head.direction = "stop"
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.score = 0
        self.delay = 0.12
        self.paused = False
        self.gold_food.hideturtle()
        self.update_display()
        
    def move(self):
        """Move the snake head"""
        if self.head.direction == "up":
            self.head.sety(self.head.ycor() + 20)
        elif self.head.direction == "down":
            self.head.sety(self.head.ycor() - 20)
        elif self.head.direction == "left":
            self.head.setx(self.head.xcor() - 20)
        elif self.head.direction == "right":
            self.head.setx(self.head.xcor() + 20)
            
    def spawn_food(self):
        """Spawn food at random location"""
        while True:
            x = random.randint(-280, 280)
            y = random.randint(-280, 280)
            x = (x // 20) * 20
            y = (y // 20) * 20
            
            # Check if position conflicts with snake
            if (x, y) != (self.head.xcor(), self.head.ycor()):
                valid = True
                for segment in self.segments:
                    if (x, y) == (segment.xcor(), segment.ycor()):
                        valid = False
                        break
                if valid:
                    self.food.goto(x, y)
                    break
                    
    def create_segment(self, color=None):
        """Create a new snake segment"""
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(color or self.snake_body_color)
        new_segment.penup()
        # Create gradient effect
        if len(self.segments) > 0:
            alpha = max(0.3, 1 - len(self.segments) * 0.05)
            # This would be more complex to implement true transparency
            # For now, we'll use different shades
            shade_colors = ["#45b7d1", "#3da0c7", "#358abd", "#2d73b3", "#255ca9"]
            color_index = min(len(self.segments) % len(shade_colors), len(shade_colors) - 1)
            new_segment.color(shade_colors[color_index])
        self.segments.append(new_segment)
        
    def check_collisions(self):
        """Check for all types of collisions"""
        # Border collision
        if not self.wrap_mode:
            if (self.head.xcor() > 290 or self.head.xcor() < -290 or 
                self.head.ycor() > 290 or self.head.ycor() < -290):
                self.game_over()
                return
        else:
            # Wrap around walls
            if self.head.xcor() > 290:
                self.head.setx(-290)
            elif self.head.xcor() < -290:
                self.head.setx(290)
            elif self.head.ycor() > 290:
                self.head.sety(-290)
            elif self.head.ycor() < -290:
                self.head.sety(290)
                
        # Food collision
        if self.head.distance(self.food) < 20:
            self.spawn_food()
            self.create_segment()
            self.score += 10
            
            if self.score > self.high_score:
                self.high_score = self.score
                
            # Progressive speed increase
            self.delay = max(0.05, self.delay - 0.001)
            
            # Chance for golden food
            if random.randint(1, 8) == 1 and not self.gold_food.isvisible():
                self.spawn_golden_food()
                
            self.update_display()
            
        # Golden food collision
        if self.gold_food.isvisible() and self.head.distance(self.gold_food) < 20:
            self.gold_food.hideturtle()
            self.score += 50
            if self.score > self.high_score:
                self.high_score = self.score
            self.delay = max(0.05, self.delay - 0.005)
            self.update_display()
            
        # Self collision
        for segment in self.segments:
            if segment.distance(self.head) < 20:
                self.game_over()
                return
                
    def spawn_golden_food(self):
        """Spawn golden special food"""
        while True:
            gx = random.randint(-280, 280)
            gy = random.randint(-280, 280)
            gx = (gx // 20) * 20
            gy = (gy // 20) * 20
            
            # Check if position is clear
            if ((gx, gy) != (self.head.xcor(), self.head.ycor()) and
                (gx, gy) != (self.food.xcor(), self.food.ycor())):
                valid = True
                for segment in self.segments:
                    if (gx, gy) == (segment.xcor(), segment.ycor()):
                        valid = False
                        break
                if valid:
                    self.gold_food.goto(gx, gy)
                    self.gold_food.showturtle()
                    self.gold_timer = 80  # frames until disappears
                    break
                    
    def game_over(self):
        """Handle game over"""
        self.save_high_score()
        
        # Game over animation
        self.head.color("#ff4757")
        time.sleep(0.5)
        
        # Show game over message
        game_over_pen = turtle.Turtle()
        game_over_pen.speed(0)
        game_over_pen.color("#ff4757")
        game_over_pen.penup()
        game_over_pen.hideturtle()
        game_over_pen.goto(0, 0)
        game_over_pen.write("GAME OVER", align="center", font=("Arial", 32, "bold"))
        
        restart_pen = turtle.Turtle()
        restart_pen.speed(0)
        restart_pen.color("#ffffff")
        restart_pen.penup()
        restart_pen.hideturtle()
        restart_pen.goto(0, -50)
        restart_pen.write("Press 'R' to restart", align="center", font=("Arial", 16, "normal"))
        
        time.sleep(1)
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
                # Golden food timer
                if self.gold_food.isvisible():
                    self.gold_timer -= 1
                    if self.gold_timer <= 0:
                        self.gold_food.hideturtle()
                        
                # Move segments
                for index in range(len(self.segments) - 1, 0, -1):
                    x = self.segments[index - 1].xcor()
                    y = self.segments[index - 1].ycor()
                    self.segments[index].goto(x, y)
                    
                if len(self.segments) > 0:
                    self.segments[0].goto(self.head.xcor(), self.head.ycor())
                    
                self.move()
                self.check_collisions()
                
            time.sleep(self.delay)

# Run the game
if __name__ == "__main__":
    game = SnakeGame()
    game.run()