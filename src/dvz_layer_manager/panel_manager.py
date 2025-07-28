"""Manage visuals and layers in a panel."""


class PanelManager:
    def __init__(self, panel):
        self.panel = panel  # the panel to manage (dvz.Panel)

        self.visuals = {}  # string -> visual (dvz.Visual)
        self.layers = {}  # string -> list of strings (visual names)

    def add_visual(self, name, visual):
        self.visuals[name] = visual
        self.panel.add(visual)

    def update_visual(self, name, property_name, value):
        # Handle special cases that go directly to set_data parameters
        if property_name == "depth_test":
            self.visuals[name].set_data(depth_test=value)
        elif property_name == "cull":
            self.visuals[name].set_data(cull=value)
        else:
            # Handle dynamic properties via kwargs
            kwargs = {property_name: value}
            self.visuals[name].set_data(**kwargs)

    def init_layer(self, name):
        self.layers[name] = []

    def add_to_layer(self, layer_name, key):
        if key not in self.visuals:
            raise ValueError(f"Key '{key}' not found in visuals.")
        if layer_name not in self.layers:
            self.init_layer(layer_name)
        if key not in self.layers[layer_name]:
            self.layers[layer_name].append(key)
        else:
            print(
                f"[PanelManager] Warning: Key '{key}' already exists in layer '{layer_name}'."
            )

    def show_layer(self, layer_name):
        if layer_name not in self.layers:
            raise ValueError(f"Layer '{layer_name}' does not exist.")
        # Hide all visuals
        for key in self.visuals:
            self.visuals[key].show(False)
        # Show the visuals in the specified layer
        for key in self.layers[layer_name]:
            self.visuals[key].show(True)
