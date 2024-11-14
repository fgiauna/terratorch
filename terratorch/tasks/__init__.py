from terratorch.tasks.classification_tasks import ClassificationTask
from terratorch.tasks.regression_tasks import PixelwiseRegressionTask
from terratorch.tasks.segmentation_tasks import SemanticSegmentationTask
from terratorch.tasks.multilabel_classification_tasks import MultiLabelClassificationTask
from terratorch.tasks.wxc_downscaling_task import WxCDownscalingTask 

__all__ = (
    "SemanticSegmentationTask",
    "PixelwiseRegressionTask",
    "ClassificationTask",
    "MultiLabelClassificationTask"
    "BATCH_IDX_FOR_VALIDATION_PLOTTING",
    "WxCDownscalingTask",
)
