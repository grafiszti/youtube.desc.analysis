from typing import Callable

import numpy as np
import pandas as pd


def clusters_overlapping(original_classes: pd.Series, predicted_classes: pd.Series) -> pd.DataFrame:
    result = []

    rows = list(sorted(set(original_classes)))
    columns = list(sorted(set(predicted_classes)))

    for original_class in rows:
        row = []
        for predicted_class in columns:
            row.append(
                ((original_classes == original_class) & (predicted_classes == predicted_class)).sum()
            )
        result.append(row)

    result = pd.DataFrame(result, columns=columns)
    result.index = rows

    return result


def mean_distance_from_centroid(metric: Callable, labels: pd.Series, embeddings: np.array) -> pd.DataFrame:
    label_indexes = []

    for original_label in labels.unique().tolist():
        current_label_vectors = embeddings[labels == original_label, :]
        centroid_vector = current_label_vectors.mean(axis=0)
        distances_from_centroid = np.array(
            list(map(lambda vec: metric(vec, centroid_vector), current_label_vectors))
        )
        label_indexes.append(
            {
                "label": original_label,
                "mean distance": distances_from_centroid.mean(),
                "median distance": np.median(distances_from_centroid)
            }
        )

    return pd.DataFrame(label_indexes)
