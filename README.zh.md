# iPyGIRS

#### 介绍
iPyGIRS是一个具有数据批量处理、机器学习模型自动调参、模型应用等特点的软件。该软件以栅格图像处理和机器学习建模为核心功能，集成了数据预处理、样本创建、像元值提取、波段计算、经验模型建模、方程应用、MySQL数据库、GeoServer数据发布等功能，可应用于多种遥感监测研究中。后续保持持续更新，目前最新可用版本为V0.2.0-Beta。

#### 软件架构
iPyGIRS完全基于Python开发，界面部分使用PyQT，包含了文件IO、数据预处理、栅格图像处理、机器学习、图表绘制等核心模块。具体的架构如下图所示：

![iPyGIRS软件架构](./images/SoftwareArchitecture.jpg)

#### 安装

1.  从Python官网[Python官网](https://www.python.org/)下载嵌入式(绿色)版Python，即下载“Windows x86-64 embeddable zip file”链接下的文件;
2.  将下载的“Windows x86-64 embeddable zip file”解压到iPyGIRS根目录下，如果，下载的3.7.5版本的embeddable Python，则应该在如下图所示的目录中有“python-3.7.5-embed-amd64”文件夹：

``` file directory tree

|- iPyGIRS
    |- iPyGIRS
        |- appUI
        |- bin
        |- chart
        |- data
        |- fileIO
        |- MathLib
        |- model
        |- python-3.7.5-embed-amd64
        |- raster
        |- resource
        |- util
    |- InstallPackages.bat
    |- iPyGIRS.bat
```

3.  为刚解压的文件夹中的嵌入式（embeddable）Python安装pip工具;
4.  使用刚安装的嵌入式（embeddable）Python的pip工具安装iPyGIRS所需的Python依赖包，依赖包的名称和安装脚本详见“InstallPackages.bat”。

#### 使用说明

该软件目前只支持Windows系统，双击iPyGIRS.bat,即可运行程序。

1.  关于iPyGIRS的使用说明文档，会在将来的推出。