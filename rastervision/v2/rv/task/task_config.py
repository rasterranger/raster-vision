from os.path import join

from rastervision.v2.core.pipeline_config import PipelineConfig
from rastervision.v2.rv.data import DatasetConfig
from rastervision.v2.rv.backend import BackendConfig
from rastervision.v2.core.config import register_config

@register_config('task')
class TaskConfig(PipelineConfig):
    dataset: DatasetConfig
    backend: BackendConfig

    debug: bool = False
    train_chip_sz: int = 200
    predict_chip_sz: int = 800
    predict_batch_sz: int = 8

    analyze_uri: str = None
    chip_uri: str = None
    train_uri: str = None
    predict_uri: str = None
    eval_uri: str = None

    def update(self, parent=None):
        if self.analyze_uri is not None:
            self.analyze_uri = join(self.root_uri, 'analyze')
        if self.chip_uri is not None:
            self.chip_uri = join(self.root_uri, 'chip')
        if self.train_uri is not None:
            self.train_uri = join(self.root_uri, 'train')
        if self.predict_uri is not None:
            self.predict_uri = join(self.root_uri, 'predict')
        if self.eval_uri is not None:
            self.eval_uri = join(self.root_uri, 'eval')
        
        super().update(parent)
