# 使用方法

## 项目说明

* 本项目使用 flask 框架
* 验证过可以正常使用的 python 版本为3.7.3
* 安装依赖：pip3 install -r requirements.txt，增加了依赖需要即时更新 requirement.txt 文件，命令为：pip3 freeze > requirements.txt
*

## 注意事项

* html文件放在 templates 下面，然后在代码中用 render_template 返回

## VSCODE使用方法

* 注意在vscode中配置python可执行文件的路径，一般为/bin/python3
* 在运行和调试中增加配置，选择调试flask服务，vscode会自动生成文件，指定入口文件为main.py，如下：

```json
{
    // 使用 IntelliSense 了解相关属性。
    // 悬停以查看现有属性的描述。
    // 欲了解更多信息，请访问: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python 调试程序: Flask",
            "type": "debugpy",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "main.py",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true,
            "autoStartBrowser": false
        }
    ]
}
```
