from pydantic import BaseModel
from typing import List

class ScenePrompt(BaseModel):
    scene_type:str
    emotion: str
    camera:str
    characters: List[str]
    setting: str
    time: str
    weather: str
    focus: str