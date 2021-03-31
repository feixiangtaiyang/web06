#项目描述

这个是web的自动化项目，基于selenium+pytest框架


#环境准备
1. python 3.6
2. pytest 4.5.0



依赖包安装
>pip install -r requirements.txt



#运行用例
>pytest


#生成报告

>pytest  --alluredir ./allure_report   -v  --clean-alluredir
>copy environment.properties allure_report\environment.properties

>allure serve ./allure_report



#pytest.ini配置
pytest.ini配置的描述
