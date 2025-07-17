from schema import ScenePrompt
import yaml
# TODO: Replace this with LLM later
def generate_prompt(summary: str) -> str:
    prompt = ScenePrompt(
        scene_type="flashback",
        emotion="melancholy",
        camera = "wide shot",
        characters=["kurome","mio"],
        setting="ruined shrine",
        time="dusk",
        weather="snow",
        focus="internal conflict"
    )
    return yaml.dump(prompt.model_dump(),sort_keys=False)