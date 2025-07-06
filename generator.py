import json
import os
from datetime import datetime
import git

# 加载配置
with open('config.json') as f:
    config = json.load(f)

def generate_md(title, content, author=None):
    """生成Markdown文件"""
    author = author or config["default_author"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # 读取模板
    with open(os.path.join("docs", config["template"]), "r") as f:
        template = f.read()
    
    # 填充内容
    md_content = template.format(
        title=title,
        author=author,
        date=timestamp,
        content=content
    )
    
    # 保存文件
    filename = f"{title.replace(' ', '_')}.md"
    output_path = os.path.join("output", filename)
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    
    print(f"已生成: {output_path}")
    return output_path

def git_push(filepath, message="Add new markdown file"):
    """提交到Git仓库"""
    repo = git.Repo(".")
    repo.git.add(filepath)
    repo.index.commit(message)
    origin = repo.remote(name="origin")
    origin.push()
    print("已推送到Git仓库")

if __name__ == "__main__":
    # 示例使用
    title = input("请输入标题: ")
    content = input("请输入内容: ")
    author = input("请输入作者(可选): ") or None
    
    md_file = generate_md(title, content, author)
    
    if input("是否推送到Git仓库? (y/n): ").lower() == "y":
        git_push(md_file)