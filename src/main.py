# -*- coding: utf-8 -*-
"""
Copyright 2023 JerryHao
@Time ： 2023/12/3 19:09
@Auth ： JerryHao
"""
from qtpy.QtWidgets import QWidget, QHBoxLayout, QLabel
from qtpy.QtCore import QObject, QEvent, Qt, QRect


class DevTool(QWidget):
    DEFAULT_WIDTH = 200

    def __init__(self, widget: QWidget, is_embed: bool = False):
        super().__init__()
        assert isinstance(widget, QWidget), "Widget type should be QWidget"
        self._widget = widget
        if not is_embed:
            widget.installEventFilter(self)
            self._on_widget_resize()
        self._init()
        self.hide()

    def _init(self):
        layout = QHBoxLayout(self)
        layout.addWidget(QLabel("This is Qss dev tool"))

    def _on_widget_resize(self):
        geometry = self._widget.geometry()
        rect = QRect(geometry.left() + geometry.width(), geometry.top(), self.DEFAULT_WIDTH, geometry.height())
        self.setGeometry(rect)

    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Type.Resize:
            self._on_widget_resize()
        elif event.type() == QEvent.Type.Resize:
            self._on_widget_resize()
        elif event.type() == QEvent.Type.Close:
            self.close()
        return super().eventFilter(obj, event)
