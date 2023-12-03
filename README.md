# Qss DevTool

作为有一年多前端经验的开发者，在接触Qt后的几年间。我经常会有一个想法：**那就是qss太难用了！！**Qss的开发几乎完全依赖经验，我相信大部分开发者都遇到过类似的问题：明明写了background-color却没有生效；只改动一个属性却因为没有热更而必须重启程序；代码中的盒子模型默认值和Qss的叠加导致界面显示不符合预期等等。这些坑都让我有强烈的开发愿望：Qt应该有类似前端的DevTool。

我相信这个想法并不是我特有的，因为我不仅仅和同事沟通过，并且根据[提问记录](https://forum.qt.io/topic/84028/qt-application-css-debugger-needed)，他们都有同样的痛点。

我的目标是不仅仅实现类似qss属性的实时显示和修改，还支持widget以树形结构显示，盒子模型显示。
