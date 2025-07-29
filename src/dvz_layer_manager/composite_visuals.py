"""Functions to support creating composite visuals."""

import numpy as np


def vector_field_visuals(
    positions,
    directions,
    arrow_length=0.03,
    arrow_head_base_length=0.01,
    arrow_head_length=0.01,
    color=(255, 255, 255, 255),
    mask=None,
):
    # If no mask is provided, use all positions
    if mask is None:
        mask = np.ones(positions.shape[0], dtype=bool)

    # Define start and end points for the arrows
    start_points = positions[mask]
    end_points = start_points + arrow_length * directions[mask]

    # Create arrow heads
    # Calculate orthonormal basis for the arrow heads
    up = np.tile(np.array([0.0, 0.0, 1.0], dtype=np.float32), (end_points.shape[0], 1))
    dot = np.abs(np.sum(directions[mask] * up, axis=1))
    parallel_mask = dot > 0.99
    if np.any(parallel_mask):
        up[parallel_mask] = np.array([0.0, 1.0, 0.0], dtype=np.float32)
    n1 = np.cross(directions[mask], up)
    n1 /= np.linalg.norm(n1, axis=1, keepdims=True)

    # Calculate points for the arrow head triangles
    base_center = end_points - arrow_head_length * directions[mask]
    P1 = base_center + (arrow_head_base_length / 2) * n1
    P2 = base_center - (arrow_head_base_length / 2) * n1

    # Concatenate points in a triangle list format
    arrowhead_triangles = np.concatenate(
        [end_points[:, np.newaxis, :], P1[:, np.newaxis, :], P2[:, np.newaxis, :]],
        axis=1,
    )
    arrow_heads = arrowhead_triangles.reshape(-1, 3)

    # Create arrow shafts using start and end points
    arrow_shafts = np.insert(
        start_points, np.arange(len(end_points)), end_points, axis=0
    )

    # Uniform colors for the arrow shafts and heads
    arrow_shaft_colors = np.tile(color, (len(arrow_shafts), 1))
    arrow_head_colors = np.tile(color, (len(arrow_heads), 1))

    return arrow_shafts, arrow_shaft_colors, arrow_heads, arrow_head_colors

