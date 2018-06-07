

class Settings():
    """存储《外星人入侵》的所有设置"""

    def __init__(self):
    	"""从初始化游戏的设置"""
    	# 屏幕设置
    	self.screen_width = 500;
    	self.screen_height = 500;
    	self.bg_color = (230, 230, 230);
    	# 飞船的设置
    	self.ship_speed_factor = 0.5;
    	# 子弹设置
    	self.bullet_speed_factor = 0.2;
    	self.bullet_width = 5;
    	self.bullet_height = 15;
    	self.bullet_color = 60, 60, 60;
    	self.bullets_allowed = 4;
    	# 外星人设置
    	self.alien_speed_factor = 1;