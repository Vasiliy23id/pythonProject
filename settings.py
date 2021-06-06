class Settings():
    def __init__(self):
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 69, 60)
        self.bullets_allowed = 3

        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (25, 25, 112)

        self.ship_limit = 3

        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.enemy_speed = 1.0

        self.enemy_points = 50

        self.fleet_direction = 1

    def increase_speed(self):

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.enemy_speed *= self.speedup_scale

        self.enemy_points = int(self.enemy_points * self.score_scale)

