#!/usr/bin/env python3
"""AI辅助编程接单页面 - FastAPI服务"""
import json
import os
from datetime import datetime

# 单文件HTML应用，用FastAPI启动
HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI辅助编程服务</title>
<style>
*{margin:0;padding:0;box-sizing:border-box;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
body{background:#f5f5f7;color:#1d1d1f;min-height:100vh}
.header{background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:#fff;padding:60px 20px;text-align:center}
.header h1{font-size:2.2em;margin-bottom:10px}
.header p{font-size:1.1em;opacity:.9}
.container{max-width:1100px;margin:0 auto;padding:40px 20px}
.services{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;margin-bottom:40px}
.card{background:#fff;border-radius:16px;padding:24px;box-shadow:0 2px 12px rgba(0,0,0,.08);transition:transform .2s}
.card:hover{transform:translateY(-4px);box-shadow:0 8px 24px rgba(0,0,0,.12)}
.card h3{font-size:1.2em;margin-bottom:8px;color:#1d1d1f}
.card p{color:#6e6e73;font-size:.95em;line-height:1.5;margin-bottom:12px}
.card .price{display:inline-block;background:#667eea;color:#fff;padding:4px 12px;border-radius:20px;font-size:.85em;font-weight:600}
.contact-form{background:#fff;border-radius:16px;padding:32px;box-shadow:0 2px 12px rgba(0,0,0,.08);max-width:600px;margin:0 auto}
.contact-form h2{text-align:center;margin-bottom:24px;font-size:1.4em}
.form-group{margin-bottom:16px}
.form-group label{display:block;margin-bottom:6px;font-weight:600;font-size:.9em;color:#1d1d1f}
.form-group input,.form-group select,.form-group textarea{width:100%;padding:12px;border:2px solid #e8e8ed;border-radius:10px;font-size:1em;transition:border-color .2s}
.form-group input:focus,.form-group select:focus,.form-group textarea:focus{border-color:#667eea;outline:none}
.form-group textarea{min-height:120px;resize:vertical}
.btn{background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;border:none;padding:14px 32px;border-radius:10px;font-size:1em;font-weight:600;cursor:pointer;width:100%;transition:opacity .2s}
.btn:hover{opacity:.9}
.stats{text-align:center;margin-top:20px;color:#86868b;font-size:.9em}
.footer{text-align:center;padding:40px 20px;color:#86868b;font-size:.85em}
.notification{display:none;padding:16px;border-radius:10px;margin-bottom:16px;text-align:center;font-weight:600}
.notification.success{display:block;background:#e8f5e9;color:#2e7d32}
.notification.error{display:block;background:#ffebee;color:#c62828}
</style>
</head>
<body>
<div class="header">
<h1>‍ AI 辅助编程服务</h1>
<p>专业Python/FastAPI开发 | 5年+经验 | 48小时启动</p>
</div>
<div class="container">
<div class="services" id="services"></div>
<form class="contact-form" id="contactForm">
<h2>提交需求</h2>
<div id="notification" class="notification"></div>
<div class="form-group">
<label>您的称呼</label>
<input type="text" id="name" required placeholder="姓名 / 公司名">
</div>
<div class="form-group">
<label>邮箱 / 联系方式</label>
<input type="email" id="email" required placeholder="your@email.com">
</div>
<div class="form-group">
<label>服务类型</label>
<select id="service">
<option value="fastapi_dev">FastAPI后端开发</option>
<option value="ai_integration">AI API集成&自动化</option>
<option value="code_review">代码审查&优化</option>
<option value="data_pipeline">数据管道&ETL</option>
<option value="custom">自定义需求</option>
</select>
</div>
<div class="form-group">
<label>预算范围</label>
<select id="budget">
<option value="$200-500">$200-500</option>
<option value="$500-1000">$500-1000</option>
<option value="$1000-3000">$1000-3000</option>
<option value="$3000+">$3000+</option>
<option value="待沟通">待沟通</option>
</select>
</div>
<div class="form-group">
<label>项目描述</label>
<textarea id="description" required placeholder="请描述您的项目需求..."></textarea>
</div>
<button type="submit" class="btn">提交需求</button>
</form>
<div class="stats">已服务 <span id="projectCount">5</span>+ 个海外项目</div>
</div>
<div class="footer">
<p>联系邮箱：shanai.dev@proton.me | 响应时间：24小时内</p>
</div>
<script>
const services=[
{title:'FastAPI后端开发',desc:'高性能API后端，FastAPI+SQLAlchemy+PostgreSQL，从设计到部署全流程',price:'$50-80/h'},
{title:'AI API集成',desc:'对接GPT/Claude等AI API，构建智能工作流和自动化系统',price:'$60-100/h'},
{title:'代码审查优化',desc:'深度代码审计、性能调优、安全加固、技术债务清理',price:'$40-60/h'},
{title:'数据管道构建',desc:'Python + Airflow打造可靠数据管道，ETL自动化处理',price:'$60-90/h'}
];
const container=document.getElementById('services');
services.forEach(s=>{
container.innerHTML+=`<div class="card"><h3>${s.title}</h3><p>${s.desc}</p><span class="price">${s.price}</span></div>`;
});
document.getElementById('contactForm').addEventListener('submit',async function(e){
e.preventDefault();
const btn=this.querySelector('.btn');
btn.disabled=true;btn.textContent='发送中...';
const data={name:document.getElementById('name').value,email:document.getElementById('email').value,service:document.getElementById('service').value,budget:document.getElementById('budget').value,description:document.getElementById('description').value};
try{
const res=await fetch('/submit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});
const result=await res.json();
if(result.success){
showNotification('需求已收到！我将24小时内通过'+data.email+'联系您。','success');
this.reset();
}else{
showNotification('提交失败，请重试','error');
}
}catch(e){
showNotification('服务暂不可用，请直接发送邮件至 shanai.dev@proton.me','error');
}
btn.disabled=false;btn.textContent='提交需求';
});
function showNotification(msg,type){
const el=document.getElementById('notification');
el.textContent=msg;el.className='notification '+type;
setTimeout(()=>{el.className='notification'},5000);
}
</script>
</body>
</html>"""

def serve():
    """启动Web服务"""
    try:
        from http.server import HTTPServer, BaseHTTPRequestHandler
    except:
        os.system("pip3 install -q flask 2>/dev/null; exit 0")
        from flask import Flask, request, jsonify, send_from_directory
        app = Flask(__name__)
        
        @app.route('/')
        def index():
            return HTML
        
        @app.route('/submit', methods=['POST'])
        def submit():
            data = request.json
            # 记录需求
            record = {
                "name": data.get("name"),
                "email": data.get("email"),
                "service": data.get("service"),
                "budget": data.get("budget"),
                "description": data.get("description"),
                "timestamp": datetime.now().isoformat()
            }
            # 保存到文件
            leads = []
            if os.path.exists("leads_data.json"):
                with open("leads_data.json") as f:
                    leads = json.load(f)
            leads.append(record)
            with open("leads_data.json", "w") as f:
                json.dump(leads, f, indent=2, ensure_ascii=False)
            print(f"[LEAD] {record['name']} | {record['email']} | {record['service']}")
            return jsonify({"success": True, "message": "需求已收到"})
        
        print("服务运行中: http://localhost:8080")
        app.run(host="0.0.0.0", port=8080)
        
    except ImportError:
        # 纯Python fallback
        import http.server
        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/':
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(HTML.encode())
                else:
                    self.send_response(404)
                    self.end_headers()
            
            def do_POST(self):
                if self.path == '/submit':
                    content_len = int(self.headers.get('Content-Length', 0))
                    body = self.rfile.read(content_len)
                    data = json.loads(body.decode())
                    record = {
                        "name": data.get("name", ""),
                        "email": data.get("email", ""),
                        "service": data.get("service", ""),
                        "budget": data.get("budget", ""),
                        "description": data.get("description", ""),
                        "timestamp": datetime.now().isoformat()
                    }
                    leads = []
                    if os.path.exists("leads_data.json"):
                        with open("leads_data.json") as f:
                            leads = json.load(f)
                    leads.append(record)
                    with open("leads_data.json", "w") as f:
                        json.dump(leads, f, indent=2, ensure_ascii=False)
                    print(f"[LEAD] {record['name']} | {record['email']} | {record['service']}")
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({"success": True}).encode())
        
        server = http.server.HTTPServer(('0.0.0.0', 8080), Handler)
        print("服务运行中: http://localhost:8080")
        server.serve_forever()

if __name__ == '__main__':
    serve()
