from logging import Logger
from pathlib import Path
import json

from models.config import Config


class HierarchySearch:

    def __init__(self, cfg: Config, logger: Logger):
        self._cfg = cfg
        self._logger = logger
        self._structure = None
        self._init_structure()

    def _is_valid_structure(self):
        if not isinstance(self._structure, list):
            return False
        for item in self._structure:
            if not isinstance(item, dict) or "uuid" not in item or "children" not in item or not isinstance(item["children"], list):
                return False
        self._logger.info(f"[HierarchySearch:_is_valid_structure] - Valid structure format")
        return True

    def _init_structure(self):
        log_header = '[HierarchySearch:_init_structure]'
        structure_path = Path(__file__).parent.resolve() / 'assets' / f'{self._cfg.structure_name}.json'
        if structure_path.exists():
            with open(structure_path, 'r') as f:
                self._structure = json.load(f)
                self._logger.info(f"{log_header} - Successfully initialized structure")
                if not self._is_valid_structure():
                    self._logger.error(f"[HierarchySearch:_is_valid_structure] - Invalid structure format")
                    raise ValueError(f"[HierarchySearch:_is_valid_structure] - Invalid structure format")
        else:
            self._logger.error(f"{log_header} - Structure file '{structure_path}.json' not found")
            raise FileNotFoundError(f"{log_header} - Structure file '{structure_path}.json' not found")

    async def find_path(self, elem_id: str) -> list | None:
        log_header = '[HierarchySearch:find_path]'
        def dfs(node, path):
            if node["uuid"] == elem_id:
                return path + [node["uuid"]]
            for child in node["children"]:
                result = dfs(child, path + [node["uuid"]])
                if result:
                    return result
            return None

        if self._structure is None:
            self._logger.error("Structure not initialized.")
            raise RuntimeError("Structure not initialized.")

        self._logger.info(f"{log_header} - Received {elem_id}")

        for node in self._structure:
            path = dfs(node, [])
            if path:
                self._logger.info(f"{log_header} - Found path: {path}")
                return path
        self._logger.error(f"{log_header} - Path not found")
        return None
