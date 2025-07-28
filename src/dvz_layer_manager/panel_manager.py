"""Manage visuals and layers in a panel."""

import datoviz as dvz


class PanelManager:
    def __init__(self, panel: dvz.DvzPanel):
        self.panel: dvz.DvzPanel = panel

        self.visuals: dict[str, dvz.DvzVisual] = {}
        self.layers: dict[str, list[str]] = {}

    def add_visual(self, name: str, visual: dvz.DvzVisual):
        self.visuals[name] = visual
        self.panel.add(visual)

    def update_visual(self, name: str, property_name: str, value: any):
        if property_name == "depth_test":
            self.visuals[name].set_data(depth_test=value)
        elif property_name == "cull":
            self.visuals[name].set_data(cull=value)
        else:
            kwargs: dict[str, any] = {property_name: value}
            self.visuals[name].set_data(**kwargs)

    def init_layer(self, name: str):
        self.layers[name] = []

    def add_to_layer(self, layer_name: str, key: str):
        if key not in self.visuals:
            raise ValueError(f"Key '{key}' not found in visuals.")
        if layer_name not in self.layers:
            self.init_layer(layer_name)
        if key not in self.layers[layer_name]:
            self.layers[layer_name].append(key)
        else:
            raise RuntimeError(f"Key '{key}' already exists in layer '{layer_name}'.")

    def show_layer(self, layer_name: str):
        if layer_name not in self.layers:
            raise ValueError(f"Layer '{layer_name}' does not exist.")
        for key in self.visuals:
            self.visuals[key].show(False)
        for key in self.layers[layer_name]:
            self.visuals[key].show(True)
