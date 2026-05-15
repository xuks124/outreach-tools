<div align="center">

# 海外接单自动化工具集 🌐

### Cold Email + 落地页 + 客户管理 — 自动化从海外接单赚钱

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/xuks124/outreach-tools)](https://github.com/xuks124/outreach-tools)

</div>

---

## 🎯 这是干嘛的？

一套帮你**从海外接单**的自动化工具。你不需要会写英文邮件、不需要一个个手动找客户，这个工具全帮你干了。

**适合谁：**
- 👨‍💻 **独立开发者** — 想接海外项目但英文不行
- 🏢 **外包团队** — 需要批量开发海外客户
- 🚀 **初创公司** — 出海获客不想花冤枉钱

## 🧰 工具有什么？

### 1️⃣ Cold Email 自动生成 + 发送

```bash
# 生成并发送批量冷邮件
python outreach_tool.py send

# 查看发送统计（打开率、回复率）
python outreach_tool.py stats

# 搜索潜在客户邮箱
python outreach_tool.py search
```

**能做什么：**
- ✅ 批量生成定制化英文开发信（AI写，不像模板）
- ✅ 自动追踪打开发/回复率
- ✅ 客户分类管理
- ✅ 防封号（随机间隔 + 自定义模板轮换）
- ✅ 一天发几百封不费劲

### 2️⃣ 落地页服务

```bash
python landing.py
# 浏览器打开 http://localhost:8080
```

**能做什么：**
- ✅ 专业的AI编程服务展示页
- ✅ 客户需求收集表单
- ✅ 手机端自适应
- ✅ 部署到生产就一行命令

### 3️⃣ 一键部署

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8080 landing:app
```

## 🚀 3 分钟上手

```bash
# 1. 安装
git clone https://github.com/xuks124/outreach-tools.git
cd outreach-tools
pip install -r requirements.txt

# 2. 配置邮箱（修改 outreach_tool.py 中的 SMTP 设置）
#    发件人地址、SMTP服务器

# 3. 导入客户列表（支持 CSV 或手动输入）

# 4. 开跑！
python outreach_tool.py send
```

## 📊 效果数据（参考）

| 指标 | 手动 | 用这个工具 |
|------|------|-----------|
| 每天发邮件数 | 20-30 封 | **300-500 封** |
| 写一封开发信 | 15 分钟 | **0 分钟（自动生成）** |
| 打开率 | 20-30% | **35-50%（AI定制化内容）** |
| 回复率 | 1-3% | **3-8%** |
| 月均询盘 | 3-5 个 | **20-50 个** |

## 💰 怎么用它赚钱？

| 场景 | 操作 | 预期效果 |
|------|------|----------|
| **接海外外包** | 批量发给欧美小公司 → 客户回复 → 接单 | 月均 20-50 个询盘 |
| **卖 SaaS 产品** | 冷邮件推广 → 落地页转化 | 转化率 2-5% |
| **自由职业者** | 找 Upwork/Fiverr 上客户 → 直接联系 | 跳过平台抽成 20% |
| **本地服务出海** | 帮国内公司发海外开发信 | 收服务费 ¥2000-5000/月 |

## 📁 项目结构

```
├── outreach_tool.py     # 冷邮件工具（核心）
├── landing.py           # 落地页服务
├── one-api-guide-en.md  # 配套英文技术文章
├── leads_data.json      # 客户需求数据模板
├── tracking.json        # 发送跟踪数据
└── README.md            # 本文件
```

## 📄 License

MIT — 随便用，随便改。

---

**觉得有用点个 ⭐，祝你早日接到海外大单！**
