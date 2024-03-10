from pydantic_yaml import YamlModel


class Config(YamlModel):
    structure_name: str
