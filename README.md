<div align="center">

# 海外接单自动化工具集 🌐

### Cold Email + 落地页 + 客户管理 — 帮你从海外市场接单赚钱

</div>

---

## 🎯 这工具是干嘛的？

一套帮你 **从海外接单** 的自动化工具。适合：

- 👨‍💻 **独立开发者** — 想接海外项目但不会写英文邮件
- 🏢 **外包团队** — 需要批量开发海外客户
- 🚀 **初创公司** — 出海获客测试

**解决的问题：** 写开发信费时费力 → 自动批量生成 → 落地页收需求 → 管理跟进

## 🧰 工具清单

### 1️⃣ Cold Email 生成器

```bash
python outreach_tool.py send     # 生成并发送批量冷邮件
python outreach_tool.py stats    # 查看发送统计（打开率、回复率）
python outreach_tool.py search   # 搜索潜在客户邮箱
```

**功能：**
- 批量生成定制化英文开发信
- 自动追踪发送统计（打开率、回复率）
- 客户分类管理
- 防封号策略（随机间隔、自定义模板）

### 2️⃣ 落地页服务

```bash
python landing.py
# 访问 http://localhost:8080
```

**功能：**
- AI 编程服务展示页
- 客户需求收集表单
- 响应式设计，手机端适配

### 3️⃣ 部署到生产

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8080 landing:app
```

## 📁 项目结构

```
├── outreach_tool.py     # 冷邮件工具（核心）
├── landing.py           # 落地页服务
├── one-api-guide-en.md  # 配套英文技术文章
├── leads_data.json      # 客户需求数据模板
└── requirements.txt     # 依赖清单
```

## 💰 怎么用这个赚钱？

| 场景 | 操作 | 预期效果 |
|------|------|----------|
| 接海外外包 | 批量发开发信 → 客户回复 → 接单 | 月均 3-10 个询盘 |
| 卖 SaaS 产品 | 冷邮件推广 → 落地页转化 | 转化率 2-5% |
| 自由职业者 | 找 Upwork/Fiverr 客户 → 私单 | 跳过平台抽成 |

## 🚀 快速开始

```bash
# 1. 安装依赖
pip install -r requirements.txt

# 2. 配置邮箱（在 outreach_tool.py 中设置）
#    SMTP 服务器、发件人地址

# 3. 导入客户列表
#    支持 CSV / 手动输入

# 4. 开跑！
python outreach_tool.py send
```

## 📄 License

MIT
