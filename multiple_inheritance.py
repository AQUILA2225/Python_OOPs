class Camera:
    def __init__(self, camera_mp):
        self.camera_mp = camera_mp
    
    def take_photo(self):
        print(f"Take Photo with:", {self.camera_mp},"Mega Pixel Camera" )
    
class MusicPlayer:
    def __init__(self, brand):
        self.brand = brand
    
    def play_music(self):
        print("Play Music in", self.brand)

class SmartPhone(Camera, MusicPlayer):
    def __init__(self, model_name, camera_mp, brand):
        self.model_name = model_name
        
        Camera.__init__(self, camera_mp)
        MusicPlayer.__init__(self, brand)
        
    def show_details(self):
        print("Model Name:", self.model_name)
        print("Camera:", self.camera_mp)
        print("Music Brand:", self.brand)
        
sp1 = SmartPhone("iPhone 14", 48, "Apple Music")
sp2 = SmartPhone("Samsung S23", 50, "Spotify")
sp1.show_details()
sp1.take_photo()
sp1.play_music()

sp2.show_details()
sp2.take_photo()
sp2.play_music()
        
        
