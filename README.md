# Datoviz Layer Manager
This is a wrapper over Datoviz (https://datoviz.org) that enables keeping track of "layers" of visualization. Each layer can consist of several "visuals".

`PanelManager`: For a single datoviz panel `dvz.Panel`, we have:
- `visuals` are stored in a string-keyed dictionary (i.e. `string -> dvz.Visual`)
- `layers` are stored in a string-keyed list-valued dictionary (i.e. `string -> List(string)`), where each item in the value is one of the keys in the `visuals` dictionary.
- Helper functions to show/hide content on the screen.
