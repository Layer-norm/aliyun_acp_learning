import json
import sys

def extract_toc(notebook_path):
    """从 Jupyter Notebook 中提取所有 Markdown 标题，生成带单元格编号的目录。"""
    # .ipynb 本质是 JSON 文件，cells 数组包含所有单元格
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    toc = []
    for i, cell in enumerate(nb['cells']):
        # 只关注 Markdown 单元格，跳过代码和输出
        if cell['cell_type'] == 'markdown':
            # cell['source'] 是行列表，拼接后按行扫描标题
            source = ''.join(cell['source'])
            for line in source.split('\n'):
                if line.startswith('#'):
                    # 记录单元格编号，方便后续定位
                    toc.append(f"[Cell {i}] {line}")
    return '\n'.join(toc)

if __name__ == '__main__':
    print(extract_toc(sys.argv[1]))
