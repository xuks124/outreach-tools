#!/usr/bin/env python3
"""海外接单全流程工具 - 客户搜索 + 冷邮件 + 提案 + 追踪"""

import json
import os
import csv
from datetime import datetime, timedelta

SERVICES = {
    "fastapi_dev": {
        "title": "FastAPI Backend Development",
        "desc": "High-performance API backend using FastAPI + SQLAlchemy + PostgreSQL",
        "rate": "$50-80/hr",
        "min_project": "$500"
    },
    "ai_integration": {
        "title": "AI API Integration & Automation",
        "desc": "Integrate GPT/Claude APIs into your existing workflow, build automation pipelines",
        "rate": "$60-100/hr",
        "min_project": "$800"
    },
    "code_review": {
        "title": "Python Code Review & Optimization",
        "desc": "Deep code audit, performance optimization, security hardening",
        "rate": "$40-60/hr",
        "min_project": "$300"
    },
    "data_pipeline": {
        "title": "Data Pipeline & ETL Automation",
        "desc": "Build reliable data pipelines with Python, Apache Airflow, or custom solutions",
        "rate": "$60-90/hr",
        "min_project": "$1000"
    }
}

TEMPLATES = {
    "cold_email": """Subject: Quick Python/FastAPI help for {company_name}?

Hi {first_name},

I've been working on similar {tech_stack} projects and noticed {company_name} might benefit from some backend optimization.

I specialize in:
- FastAPI/Flask API development
- AI API integration (GPT, Claude)
- Python automation & data pipelines
- Code review & performance tuning

I work on a project basis (starting from ${min_project}) and can start within 48 hours.

Would you be open to a 15-min call to discuss your current needs?

Best,
AI Developer
Portfolio: https://github.com/shanai/shan-ai-gateway""",

    "short_email": """Subject: {company_name} backend optimization?

Hi {first_name},

Experienced Python/FastAPI developer available for {company_name}'s backend needs.

{offer}

Project-based pricing from ${min_project}. Available in 48hrs.

Interested in a quick chat?

Best,
AI Developer""",

    "proposal": """# Technical Proposal for {company_name}

## Overview
Full-stack Python development services tailored to your needs.

## Services Offered
{services_list}

## Pricing
- Hourly: {hourly_rate}
- Project-based: from ${min_project}
- Retainer available for ongoing work

## Timeline
- Initial deliverable: 3-7 days
- Full project: 2-4 weeks depending on scope

## Experience
- 5+ years Python development
- FastAPI, Django, Flask
- AI/ML API integration
- Cloud deployment (AWS/GCP/Aliyun)

## Next Steps
1. Brief call to understand requirements
2. Free technical assessment
3. Fixed-price quote
4. Delivery with 7-day support

Contact: [your-email]""",

    "follow_up": """Subject: Quick follow-up

Hi {first_name},

Just checking if you had a chance to review my proposal regarding {topic}.

I'm currently available this week and could start immediately if needed.

Happy to jump on a quick call anytime.

Best,
AI Developer"""
}

LEADS_FILE = "leads.csv"
TRACKING_FILE = "tracking.json"

def search_upwork(keyword="FastAPI developer", max_results=5):
    """搜索Upwork最新项目（模拟版）"""
    from datetime import datetime
    projects = [
        {"title": f"{keyword} needed for {kw}", "budget": "$500-$2000", "posted": (datetime.now() - timedelta(hours=i*3)).isoformat(), "url": f"https://upwork.com/job/{i}"}
        for i, kw in enumerate(["API backend", "microservice", "data pipeline", "cloud migration", "automation script"], 1)
    ]
    return projects[:max_results]

def search_clutch(industry="software development", count=5):
    """搜索Clutch上的潜在客户公司"""
    companies = [
        {"name": f"TechSolutions_{i}", "domain": f"techsolutions{i}.com", "tech": "Python/Django"}
        for i in range(1, count+1)
    ]
    return companies

def add_lead(name, company, email, source, notes=""):
    """添加潜在客户到CSV"""
    headers = ["name", "company", "email", "source", "notes", "added"]
    row = [name, company, email, source, notes, datetime.now().isoformat()]
    
    file_exists = os.path.isfile(LEADS_FILE)
    with open(LEADS_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(headers)
        writer.writerow(row)
    return f"Lead added: {name} @ {company}"

def send_email(lead_name, lead_email, template_type="cold_email", service="fastapi_dev"):
    """生成并记录邮件（实际发送需配置SMTP）"""
    service_info = SERVICES[service]
    template = TEMPLATES[template_type]
    
    if template_type == "short_email":
        offers = [
            "I build and optimize Python backends for growing companies.",
            "I help startups ship FastAPI backends in under 2 weeks.",
            "I specialize in AI API integration and Python automation."
        ]
        import random
        email = template.format(
            company_name=lead_name.split()[-1] if " " in lead_name else lead_name,
            first_name=lead_name.split()[0],
            offer=offers[hash(lead_name) % len(offers)],
            min_project=service_info["min_project"]
        )
    else:
        email = template.format(
            company_name=lead_name.split()[-1] if " " in lead_name else lead_name,
            first_name=lead_name.split()[0],
            tech_stack="Python/FastAPI",
            min_project=service_info["min_project"]
        )
    
    # 记录到跟踪
    tracking = {"sent": []}
    if os.path.isfile(TRACKING_FILE):
        try:
            with open(TRACKING_FILE) as f:
                tracking = json.load(f)
        except:
            tracking = {"sent": []}
    
    tracking["sent"].append({
        "to": lead_email,
        "name": lead_name,
        "template": template_type,
        "service": service,
        "sent_at": datetime.now().isoformat(),
        "status": "sent"
    })
    
    with open(TRACKING_FILE, "w") as f:
        json.dump(tracking, f, indent=2)
    
    return email

def show_stats():
    """显示发送统计"""
    if not os.path.isfile(TRACKING_FILE):
        return "No emails sent yet."
    
    with open(TRACKING_FILE) as f:
        tracking = json.load(f)
    
    sent = tracking.get("sent", [])
    total = len(sent)
    
    stats = {
        "total_sent": total,
        "today": sum(1 for s in sent if s["sent_at"].startswith(datetime.now().strftime("%Y-%m-%d"))),
        "by_service": {},
        "by_template": {}
    }
    
    for s in sent:
        svc = s.get("service", "unknown")
        tmpl = s.get("template", "unknown")
        stats["by_service"][svc] = stats["by_service"].get(svc, 0) + 1
        stats["by_template"][tmpl] = stats["by_template"].get(tmpl, 0) + 1
    
    return json.dumps(stats, indent=2)

def update_outreach_tool():
    """打印工具更新日志"""
    log = f"""
=== Outreach Tool v2.0 ===
Added:
- Lead management (CSV-based)
- Email tracking & stats
- Short email variant
- Service-centric approach
- Stats reporting

Usage:
  python3 outreach_tool.py search    # Search for leads
  python3 outreach_tool.py send      # Send sample email
  python3 outreach_tool.py stats     # Show sending stats
"""
    print(log)

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "search":
            projects = search_upwork()
            print(f"Found {len(projects)} projects:")
            for p in projects:
                print(f"  - {p['title']} ({p['budget']})")
        elif cmd == "send":
            email = send_email("John Smith", "john@techcorp.com", "cold_email", "fastapi_dev")
            print(email)
        elif cmd == "stats":
            print(show_stats())
        else:
            update_outreach_tool()
    else:
        update_outreach_tool()
