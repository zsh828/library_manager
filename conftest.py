import sys
import os

# 将项目根目录添加到 Python 路径中，以便能够导入 src 包
# 这解决了 "ModuleNotFoundError: No module named 'src'" 的问题
# conftest.py 在 pytest 收集测试阶段就会被执行
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))