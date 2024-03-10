from pathlib import Path

from fastapi import FastAPI, Body

from models.config import Config
from models.models import IdModel
from utils.target_logger import get_logger
from hierarchy_search import HierarchySearch


app = FastAPI(title='Hierarchy Search')

cfg = Config.parse_file(Path(__file__).parent.resolve() / 'Config.yaml')
logger = get_logger(name='Hierarchy Search', session_id='Hierarchy Search')

hierarchy_search = HierarchySearch(cfg=cfg, logger=logger)


@app.post(path='/get_path')
async def get_path(id_model: IdModel = Body(...)):
    path = await hierarchy_search.find_path(id_model.elem_id)
    if path:
        return {"path": path}
    else:
        return {"path": f"{id_model.elem_id} Not found in structure"}
