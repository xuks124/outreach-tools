# 海外接单自动化工具集

一套帮独立开发者海外接单的自动化工具。

## 工具清单

### 1. Cold Email生成器 (`outreach_tool.py`)
批量生成定制化冷邮件，可追踪发送统计。

```bash
python outreach_tool.py send     # 生成示例邮件
python outreach_tool.py stats    # 查看发送统计
python outreach_tool.py search   # 搜索潜在客户
```

### 2. 落地页服务 (`landing.py`)
AI编程服务展示页，收集客户需求。

```bash
python landing.py
# 访问 http://localhost:8080
```

### 3. 部署到云
```bash
# 使用gunicorn部署
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8080 landing:app
```

## 文件结构
```
├── outreach_tool.py    # 冷邮件工具
├── landing.py          # 落地页服务
├── one-api-guide-en.md # 技术文章(英文)
├── leads_data.json     # 客户需求数据
└── tracking.json       # 发送追踪
```

## License
MIT
